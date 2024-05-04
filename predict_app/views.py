from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # 如果您使用 Django 内置的 User 模型
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password  # 用于加密密码
from django.contrib import messages  # 顯示成功或錯誤訊息
from .models import Account
from django.contrib.auth.hashers import check_password  # 加密密碼
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
# Create your views here.
def home(request):
    username = request.session.get('username', 'Guest')  # 获取存储的用户名
    return render(request, 'index.html', {'username': username})
def logout_view(request):
    logout(request)  # 终止用户会话
    request.session.flush()  # 清除所有会话数据
    messages.success(request, "您已成功登出。")  # 显示登出成功的消息
    return redirect('login')  # 重定向到登录页
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # 获取用户名
        raw_password = request.POST.get('password')  # 获取密码

        # 尝试根据用户名查找用户
        try:
            account = Account.objects.get(username=username)
        except Account.DoesNotExist:
            account = None

        # 如果用户存在，并且密码匹配
        if account and check_password(raw_password, account.password):
            # 可以在这里处理会话或重定向
            request.session['user_id'] = account.id  # 将用户 ID 存储在会话中
            request.session['username'] = account.username  # 将用户名存储在会话中
            return redirect('home')  # 重定向到首页，或其他页面
        else:
            # 显示错误信息
            messages.error(request, '用戶名或密碼錯誤，请重试。')

    return render(request, 'login.html')  # 渲染登录页面


def register(request):
    if request.method == 'POST':
        # 获取用户名和密码
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        # 检查用户名是否已存在
        if Account.objects.filter(username=username).exists():  # 用户名是否存在
            messages.error(request, "用戶名已存在，請選擇其他用戶名。")  # 显示错误消息
            return render(request, 'register.html')  # 返回注册页面

        # 对密码进行加密
        hashed_password = make_password(raw_password)  # 加密密码
        # 创建用户帐户
        account = Account(username=username, password=hashed_password)
        account.save()  # 保存到数据库

        messages.success(request, "註冊成功！")  # 成功消息
        return redirect('login')  # 或者其他页面

    return render(request, 'register.html')  # 渲染注册页面

def user_list(request):
    accounts = Account.objects.all()  # 获取所有帐户
    return render(request, 'user.html', {'accounts': accounts})  # 渲染模板

def delete_user(request, user_id):
    try:
        # 查找用户
        account = Account.objects.get(id=user_id)
        # 删除用户
        account.delete()
        messages.success(request, "用戶已成功刪除。")
    except Account.DoesNotExist:
        messages.error(request, "用戶不存在。")

    # 重定向到用户列表
    return HttpResponseRedirect(reverse('user_list'))