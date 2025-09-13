from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido al endpoint Principal")