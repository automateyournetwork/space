from django.contrib import admin
from . import models
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def login(): pass

admin.site.register(models.Space_Credentials)
