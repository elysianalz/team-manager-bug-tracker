from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)

class Bug(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField('date published')

class Activity(models.Model):
    datetime = models.DateTimeField()
    acitvity_description = models.CharField(max_length=30)
    user_name = models.CharField(max_length=50)
