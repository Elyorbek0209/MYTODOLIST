from django.shortcuts import render
#from django.http import HttpResponse

def homeView(request):

    context = {
        'username' : "Sadaf",
		"email" : "sadaf@gmail.com"
		}
		
    return render(request, "MainApp/index.html", context)
