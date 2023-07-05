from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class People(models.Model):	
	name = models.fields.CharField(max_length = 100)
	class Likes(models.TextChoices):
		Like = "Li"
		Dislike = "Di"
		Other = "Ot"
	likes = models.fields.CharField(choices=Likes.choices, max_length=5)
	yeahBirth = models.fields.IntegerField( validators=[MinValueValidator(1900), MaxValueValidator(2021)])
	active = models.fields.BooleanField(default = True)
	
class Order(models.Model):
	item = models.fields.CharField(max_length = 100)
	descriotion = models.fields.CharField(max_length = 1000)
	people = models.ForeignKey(People, null=True, on_delete=models.SET_NULL)
	

	
	