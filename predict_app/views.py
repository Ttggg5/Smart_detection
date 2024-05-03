from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Account  # 导入 Account 模型
from django.contrib.auth.models import User  # 如果您使用 Django 内置的 User 模型
from django.contrib.auth.hashers import make_password  # 用于加密密码
from django.contrib import messages  # 用于显示成功或错误消息
from .models import Account

# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # 获取用户名和密码
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        # 检查用户名是否已存在
        if Account.objects.filter(username=username).exists():  # 用户名是否存在
            messages.error(request, "用户名已存在，请选择另一个。")  # 显示错误消息
            return render(request, 'register.html')  # 返回注册页面

        # 对密码进行加密
        hashed_password = make_password(raw_password)

        # 创建用户帐户
        account = Account(username=username, password=hashed_password)
        account.save()  # 保存到数据库

        messages.success(request, "注册成功！")  # 成功消息
        return redirect('home')  # 或者其他页面

    return render(request, 'register.html')  # 渲染注册页面

def user_list(request):
    accounts = Account.objects.all()  # 获取所有帐户
    return render(request, 'user.html', {'accounts': accounts})  # 渲染模板