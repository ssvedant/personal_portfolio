from django.db import models

# Create your models here.

class Project(models.Model):   # here i have created a class by the name Project and inherited the models class that django has inbuilt for us. this will help us to interact with the database create table and bring things in and out
    title=models.CharField(max_length=100)   # we have to be very specific about the use of field (property) in django class, that is if we are going to have string as a field then we must specify what type of string ex charfield or textfield etc. Whenever we want to add a field (property) to our class then refer to the page https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types on internet and choose the field you want to use. Inside the ()of a field we can have its customization
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images/') # the value of upload_to should be the path of the folder where your images you want to be upladed
    url=models.URLField(blank=True) # blan is a property which can be used with any field. It is actually used to make the use of field optional for the user. Default value of blank is False.

    def __str__(self):
       return self.title
