from django.contrib import admin
from myToDo.models import ToDo
# Register your models here.
admin.site.register(ToDo)  #this code we use to register our database with django admin page
                           # here we passed the model database class name (ToDo)