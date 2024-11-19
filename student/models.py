from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.CharField(max_length = 255)
    sname = models.CharField(max_length = 100)
    semail = models.EmailField(max_length = 100)
    scontact = models.CharField(max_length = 50)
    sdelete = models.BooleanField(default=False)
    class meta:
        db_table = "student"
    


    
