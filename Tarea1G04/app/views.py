from django.shortcuts import render

# Create your views here.

def inicio(request):
	return render(request, 'inicio.html')

def renombrar(request):
	return render(request, 'renombrar.html')