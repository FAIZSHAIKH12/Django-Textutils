from django.db import models

# Create your models here.

class ExamCenter(models.Model):
    cname=models.CharField(max_length=70)
    city=models.CharField(max_length=80)



class Student(ExamCenter):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()


    
