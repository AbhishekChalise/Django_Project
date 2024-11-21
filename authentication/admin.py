from django.contrib import admin

# Register your models here.

from .models import AuthenticationModel

admin.site.register(AuthenticationModel)
