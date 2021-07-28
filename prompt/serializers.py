from rest_framework import serializers
from .models import Prompt
from django.contrib.auth import get_user_model

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = '__all__'

# class PromptReadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Prompt
#         fields = '__all__'
