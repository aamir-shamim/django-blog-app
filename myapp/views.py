from django.shortcuts import render, redirect
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'myapp/home.html', {'posts': posts})


def add_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('/')

    return render(request, 'myapp/add_post.html')


def edit_post(request, id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/')

    return render(request, 'myapp/edit_post.html', {'post': post})


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')

