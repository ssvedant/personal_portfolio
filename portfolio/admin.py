from django.contrib import admin

# Register your models here.
from .models import Project  # first we need to import the class that we want to add to admin login page
admin.site.register(Project) # then we add the class to the admin page
