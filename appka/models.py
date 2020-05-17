from django.db import models
from django.utils import timezone

gender = ( ('MALE', 'Male'),('FEMALE','Female'))
city = (('WARSAW','Warsaw'),('POZNAN','Poznan'),('WROCLAW','Wroclaw'),('CRACOW','Cracow'))

# Create your models here.
class Course(models.Model):
    enroll_date = models.TimeField(default=timezone.now())
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    post_code = models.CharField(max_length=6)
    gender = models.CharField(choices=gender, max_length=20)
    city = models.CharField(choices=city, max_length=20)
    etc = models.TextField(max_length=500)


