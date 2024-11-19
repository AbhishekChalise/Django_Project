from django.db import models

# Create your models here.

class AuthenticationModel(models.Model):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default = False)
    
    class Meta:
        db_table = 'authentication'