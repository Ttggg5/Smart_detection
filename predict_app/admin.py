from django.contrib import admin
from .models import Post, Account, AccountAdmin
# Register your models here.

admin.site.register(Post)
#admin.site.register(Account, AccountAdmin)