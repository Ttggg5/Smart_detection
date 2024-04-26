from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    data = {"posts": list(posts.values())}
    return JsonResponse(data)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    data = {"post": {
        "title": post.title,
        "content": post.content,
        "created_at": post.created_at
    }}
    return JsonResponse(data)
