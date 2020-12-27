from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Snippet(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    def _str_(self):
        return self.name



class ExamQ(models.Model):
    UserI = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    marks = models.IntegerField()
    q1 = models.CharField(max_length=100)
    q2 = models.CharField(max_length=100)
    q3 = models.CharField(max_length=100)
    q4 = models.CharField(max_length=100)

class ExamV(models.Model):
    UserI = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    marks = models.IntegerField()
    q1 = models.CharField(max_length=100)
    q2 = models.CharField(max_length=100)
    q3 = models.CharField(max_length=100)
    q4 = models.CharField(max_length=100)

class TMarks(models.Model):
    UserI = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    tmarks = models.IntegerField()

class Dmarks(models.Model):
    UserI = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    dmarks = models.IntegerField()
    date_now  = models.CharField(max_length=100,default='NULL')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    