from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)  # 用户名
    password = models.CharField(max_length=255)  # 密码
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    def set_password(self, raw_password):
        # 使用 Django 的加密工具对密码进行加密
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        # 验证给定的密码是否与加密后的密码匹配
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username  # 返回用户名


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Account._meta.fields]

    #list_display = ['username', 'password', 'created_at']
