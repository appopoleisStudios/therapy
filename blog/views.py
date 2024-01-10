# views.py
from django.shortcuts import render
from .models import Post, Discussion

def post_list(request):
    posts = Post.objects.all()
    discussions = Discussion.objects.all()
    return render(request, 'index.html', {'posts': posts, 'discussions': discussions})


