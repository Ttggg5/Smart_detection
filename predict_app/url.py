from django.urls import path
from .views import home, login
from . import views  # 导入视图模块


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('users/', views.user_list, name='user_list'),  # 用户列表的 URL 路由
]
