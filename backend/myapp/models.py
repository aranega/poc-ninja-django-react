from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
