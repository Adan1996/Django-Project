from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'judul': 'Blog Page',
        'content': 'This blog has been created from blog folder'
    }
    return render(request, 'blog/index.html', context)


def cerita(request):
    context = {
        'judul': 'Story',
        'content': 'Page of story has been created'
    }
    return render(request, 'blog/index.html', context)
