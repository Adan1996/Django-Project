from django.http import HttpResponse

# method view
def index(request):

    str_output = "<h1>Ini adalah halaman Home</h1>"

    return HttpResponse(str_output)

def about(request):
    return HttpResponse("This is About page")