from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'judul': 'Test a New Page',
        'subtitle': 'Page of a new for this practice',
        'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog'],
            ['/newpage', 'This page']
        ]
    }
    return render(request, 'newpage/index.html', context)
