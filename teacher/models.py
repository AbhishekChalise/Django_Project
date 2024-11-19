from django.db import models


# Create your models here.

class Teacher(models.Model):
    Tid = models.CharField(max_length = 255)
    Tname = models.CharField(max_length = 255)
    Temail = models.EmailField(max_length = 255)
    Tcontact = models.CharField(max_length = 255)
    Tsubject = models.CharField(max_length = 255)
    Tdeleted = models.BooleanField(default = False)
    class Meta:
        db_table = "teacher"

# class meta means we are giving certain attributes to the class Teacher means we are giving the class meta and additional
# features here example we are providing the database table name to be teacher.
# The model name is Teacher and the table name is teacher.

   


