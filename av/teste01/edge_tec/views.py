from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def contatos(request):
    return render (request, "contatos.html")

def sobre(request):
    return render(request, "sobre.html")

def blog(request):
    return render(request, "blog.html")

def enderecos(request):
    return render(request, "enderecos.html")

def parceiros(request):
    return render(request, "parceiros.html")


# Create your views here.
