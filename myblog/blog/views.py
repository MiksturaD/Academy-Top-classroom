from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import title

from blog.models import Post

def post(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def detail(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
    return render(request, 'detail.html', {'posts': posts})