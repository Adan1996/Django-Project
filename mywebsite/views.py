from django.shortcuts import render

# method view


def index(request):
    context = {
        'judul': 'Home',
        'content': 'Welcome to my website'
    }
    return render(request, 'index.html', context)
