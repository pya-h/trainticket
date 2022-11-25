from django.contrib import admin

# Register your models here.
from .models import Train,Person

admin.site.register(Train)
admin.site.register(Person)