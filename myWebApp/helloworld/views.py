from django.http import HttpResponse
from django.shortcuts import render
from helloworld.models import People, Order

def hello(request):
	x = People.objects.all()
	return render(request, 'helloworld/hello.html', {'xs': x})
	
def helloDetail(request, id):
	person = People.objects.get(id=id)
	return render(request, 'helloworld/person.html', {'person': person})
	
def order(request):
	y = Order.objects.all()
	return render(request, 'helloworld/order.html', context = {'ys': y})
