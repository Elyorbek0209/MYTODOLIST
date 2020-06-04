from django.urls import path
from . import views

urlpatterns = [
   # path('', views.homeView, name='home'),
    path('', views.homeView,{'pagename': ''}, name='home'),
    path('<str:pagename>', views.homeView, name='index'),
]
