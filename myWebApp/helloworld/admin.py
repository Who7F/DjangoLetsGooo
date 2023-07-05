from django.contrib import admin

from helloworld.models import People, Order

class PeopleAdmin(admin.ModelAdmin):
	list_display = ('name', 'yeahBirth')
	
class OrderAdmin(admin.ModelAdmin):
	list_display = ('item', 'people')

admin.site.register(People, PeopleAdmin)

admin.site.register(Order, OrderAdmin)

