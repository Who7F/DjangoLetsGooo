from django.contrib import admin

from helloworld.models import Peopole

class PeopoleAdmin(admin.ModelAdmin):
	list_display = ('name', 'yeahBirth')

admin.site.register(Peopole, PeopoleAdmin)


