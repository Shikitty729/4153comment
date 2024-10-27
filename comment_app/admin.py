# comment_app/admin.py
from django.contrib import admin
from .models import Comment1, Comment2

# 注册 Comment1 模型
admin.site.register(Comment1)

# 注册 Comment2 模型
admin.site.register(Comment2)
