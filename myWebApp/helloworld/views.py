from django.http import HttpResponse
from django.shortcuts import render
from helloworld.models import Peopole

def hello(request):
	x = Peopole.objects.all()
	
	return render(request, 'helloworld/hello.html', context = {'xs': x})
