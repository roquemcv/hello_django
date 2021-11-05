from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request,a,b):
    total = a + b
    return HttpResponse('<h1>A soma é {}'.format(total))
