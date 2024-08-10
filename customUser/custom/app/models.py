from django.db import models

# Create your models here.
# from django.contrib.auth.models import AbstractUse

class Common(models.Model):
    cname=models.CharField(max_length=70)
    city=models.CharField(max_length=80)


class Student(Common):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    
