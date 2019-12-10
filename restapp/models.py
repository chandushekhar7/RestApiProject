from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.AutoField(primary_key = True)
    sname = models.CharField(max_length = 40)
    sadd = models.CharField(max_length = 30)

    def __str__(self):
        return self.sname
