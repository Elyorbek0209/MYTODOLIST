from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 

def homeView(request):
    return HttpResponse("<h1>Hello LorcaCoffeeBar</h1>") 