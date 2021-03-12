from django.db import models

# Create your models here.


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)


class Heroes(models.Model):
    HeroId = models.AutoField(primary_key=True)
    HeroName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
    Rank = models.PositiveIntegerField(null=True, blank=True)