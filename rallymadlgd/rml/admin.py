from django.contrib import admin

from .models import News, Pilot, Car

# Register your models here.

admin.site.register(News)
admin.site.register(Pilot)
admin.site.register(Car)

