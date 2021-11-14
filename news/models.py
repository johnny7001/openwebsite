from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() #文字
    file_url = models.CharField(max_length=255)
    post_date = models.DateField() #時間
    
    class Meta:
        db_table = 'news'
        
     