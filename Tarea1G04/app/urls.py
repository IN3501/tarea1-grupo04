from django.urls import path
from .views import *
from .views import final 

urlpatterns = [
	path('/inicio/', inicio, name ='inicio'),
	path('renombrar/', renombrar, name='renombrar'),
	
	
]