from django.db import models
from django.contrib.auth.models import AbstractUser
import os



# Create your models here.
class NewUser(AbstractUser):
    employee_num = models.CharField(max_length=10)


class Report(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey(NewUser)

    def __str__(self):
        return self.user.username + '\t' + str(self.date)

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField('date commented')
    report = models.ForeignKey(Report)

    user = models.ForeignKey(NewUser)

    def __str__(self):
        return self.report.content + '\t' + self.user.username + '\t' + str(self.date)
