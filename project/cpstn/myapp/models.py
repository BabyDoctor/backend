from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)


class Schedule(models.Model):
    scheduleId = models.AutoField(primary_key=True)
    event = models.CharField(max_length=100)
    temp = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100, null=True)
    detail = models.CharField(max_length=255, null=True)

    
class Disease(models.Model):
    name = models.CharField(max_length=255)
    detail = models.CharField(max_length=255, default= '')