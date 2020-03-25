from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    # queryset
    posts = Post.objects.all()

    context = {
        'judul': 'Blog Page',
        'content': 'This blog has been created from blog folder',
        'banner': 'blog/img/banner_blog.png',
        'app_css': 'blog/css/styles.css',
        'Posts': posts
    }
    return render(request, 'blog/index.html', context)


# def cerita(request):
#     context = {
#         'judul': 'Story',
#         'content': 'Page of story has been created'
#     }
#     return render(request, 'index.html', context)
