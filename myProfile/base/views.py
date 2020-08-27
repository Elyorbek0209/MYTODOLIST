from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def home(request):

    context={ 'name':'Elyor'}
    return render(request, 'base/home.html', context)

