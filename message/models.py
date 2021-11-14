from django.db import models

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    content = models.TextField()
    
    class Meta:
          db_table = 'message' #建立資料表