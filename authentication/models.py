from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AuthenticationModel(models.Model):

    User = models.OneToOneField(User , on_delete = models.CASCADE) 
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default = False)
    class Meta:
        db_table = 'authentication'