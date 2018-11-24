from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    sname = models.CharField(max_length=30)
    slastname = models.CharField(max_length=30)
    smarks = models.IntegerField()
    sclass = models.CharField(max_length=30)
