from django.contrib import admin

from .models import Book, Car

# Register your models here.

admin.site.register(Car)
admin.site.register(Book)