from django.db import models
from authentication.models  import AuthenticationModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    #sid = models.CharField(max_length = 255)
    sname = models.CharField(max_length = 100)
    semail = models.EmailField(max_length = 100)
    scontact = models.CharField(max_length = 50)
    sdelete = models.BooleanField(default=False)
    class meta:
        db_table = "student"

@receiver(post_save , sender  = AuthenticationModel)
def create_Student(sender,instance,created,**kwargs):
    if created and instance.is_student:
        Student.objects.create(user = instance ,sname = instance.username)
        print('Created Students for: ',instance.username)


    


    
