from django.contrib import admin

# Register your models here.
from .models import Job,Person

admin.site.register(Job)
admin.site.register(Person)