from django.db import models

# Create your models here.

class Course(models.Model):
    cname = models.CharField(max_length = 255)
    class Meta:
        db_table = 'course'
