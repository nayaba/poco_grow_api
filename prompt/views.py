from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Prompt
from .serializers import PromptSerializer
# from .serializers import PromptReadSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


# from django.http import JsonResponse

class Prompts(APIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=PromptSerializer

    def get(self, request):
        """Index Request"""
        prompts = Prompt.objects.filter(owner=request.user.id)
        data = PromptSerializer(prompts, many=True).data
        return Response({"prompt": data})
        # prompts = Prompt.objects.filter(owner=request.user.id)

    def post(self, request):
        """Create a Prompt"""
        request.data['prompt']['owner'] = request.user.id
        serializer = PromptSerializer(data=request.data['prompt'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PromptDetail(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show one Prompt"""
        prompt = get_object_or_404(Prompt, pk=pk)

        if not request.user.id == prompt.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this prompt')
        print('request.user.id: ', request.user.id)
        print('prompt.owner.id: ', prompt.owner.id)
        data = PromptSerializer(prompt).data
        return Response({ 'prompt': data })

    def patch(self, request, pk):
        """Update a Prompt"""
        print('request: ', request.data)
        prompt = get_object_or_404(Prompt, pk=pk)
        print('prompt: ', prompt)
        ms = PromptSerializer(prompt, data=request.data['prompt'], partial=True)
        if ms.is_valid():
            ms.save()
            print('ms.data: ', ms.data)
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        prompt = get_object_or_404(Prompt, pk=pk)
        if not request.user.id == prompt.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this prompt')
        print('request.user.id: ', request.user.id)
        print('prompt.owner.id: ', prompt.owner.id)
        prompt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
