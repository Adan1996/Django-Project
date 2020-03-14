from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'judul': 'About',
        'content': 'This is About page'
    }
    return render(request, 'about.html', context)
