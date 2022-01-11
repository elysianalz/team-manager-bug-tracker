from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=60)

class User(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)

class Project(models.Model):
    name = models.CharField(max_length=30)

class Status(models.Model):
    status = models.CharField(max_length=20)

class Flag(models.Model):
    flag = models.IntegerField()

class Employment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)

class Assignment(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Report(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField("date published")
    tite = models.CharField(max_length=100)
    description = models.TextField()

class Bug(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    report_id = models.ForeignKey(Report, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.PROTECT)
    flag_id = models.ForeignKey(Flag, on_delete=models.PROTECT)

class Activity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    bug_id = models.ForeignKey(Bug, on_delete=models.PROTECT)
    description = models.CharField(max_length=30)

class BugAssign(models.Model):
    bug_id = models.ForeignKey(Bug, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
