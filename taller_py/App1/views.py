from django.shortcuts import render
import django.http import HttpResponse

# Create your views here.
def IndexView(request):
    '''Esto es un ejemplo de pagina principal'''
    return HttpResponse("Hola mundo")
