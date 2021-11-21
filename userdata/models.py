from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #一個Profile 只能對應一個User
    height = models.PositiveIntegerField(default=150)
    male = models.BooleanField(default=False)
    website = models.URLField(null=True)

    def __str__(self):
        return self.user.username

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    note = models.TextField()
    ddate = models.DateField()

    def __str__(self):
        return "{}({})".format(self.ddate, self.user)
    






#自訂User第一版
# class User(models.Model):
#     name = models.CharField(max_length=20, null=False)
#     email = models.EmailField()
#     password = models.CharField(max_length=20, null=False)
#     enabled = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name