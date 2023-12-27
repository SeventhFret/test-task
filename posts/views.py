from django.shortcuts import render
from posts.models import Post

def index_view(request):
    posts = Post.objects.all()
    return render(request, "index.html", {'posts': posts})
