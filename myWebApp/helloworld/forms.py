from django import forms

from .models import People

class ContactUsForm(forms.Form):
	name = forms.CharField(required = False)
	email = forms.EmailField()
	message = forms.CharField(max_length = 1000)
	
class PeopleForm(forms.ModelForm):
	class Meta:
		model = People
		fields = '__all__'
