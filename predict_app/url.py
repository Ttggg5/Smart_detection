from django.urls import path
from .views import home, login

urlpatterns = [
    path('posts/', home, name='post_list'),
    path('posts/<int:pk>/', login, name='post_detail'),
]
