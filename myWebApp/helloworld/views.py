from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from helloworld.models import People, Order
from helloworld.forms import ContactUsForm, PeopleForm

def hello(request):
	x = People.objects.all()
	return render(request, 'helloworld/hello.html', {'xs': x})
	
def helloDetail(request, id):
	person = People.objects.get(id=id)
	return render(request, 'helloworld/person.html', {'person': person})
	
def order(request):
	y = Order.objects.all()
	return render(request, 'helloworld/order.html', context = {'ys': y})
		
def contact(request):
	if request.method == 'POST':
		form = ContactUsForm(request.POST)
		if form.is_valid():
			send_mail(
				subject = f'Message from {form.cleaned_data["name"] or "anonymous"} via Hello Contact Us form',
				
				message=form.cleaned_data['message'],
				from_email =form.cleaned_data['email'],
				recipient_list=['someemail@email.com']
			)
			return redirect(order)
	else:
		form = ContactUsForm()
	return render(request, 'helloworld/contact.html', {'form':form})

def add(request):
	if request.method == 'POST':
		form = PeopleForm(request.POST)
		if form.is_valid():
			people = form.save()
			return redirect('person', people.id)
	else:
		form = PeopleForm()
	return render(request, 'helloDetail', {'form':form})
	
def updat(requst, id)
	person = People.objects.get(id=id)
	form = PeopleFomr(requst.POST, instance=person)
	if form.is_valid();
		person = form.save()
		return redirect('person', people.id)
	else:
		form = PeopleForm(instance = person)
	return render(request, Working on)
		