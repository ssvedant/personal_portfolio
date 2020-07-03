from django.contrib import admin

# Register your models here.
from .models import Blog  # first we need to import the class that we want to add to admin login page
admin.site.register(Blog)
