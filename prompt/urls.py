from django.urls import path
# from . import views
from .views import Prompts, PromptDetail

urlpatterns = [
    path('', Prompts.as_view(), name='prompts'),
    path('<int:pk>/', PromptDetail.as_view(), name='prompt_detail'),
]

# urlpatterns = [
#     path('', views.index, name='index')
# ]
