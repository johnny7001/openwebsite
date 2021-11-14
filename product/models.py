from django.db import models

# Create your models here.

class Product(models.Model):
    shop = models.CharField(max_length=20)  #欄位名稱 / 屬性=文字(長度)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    price = models.IntegerField() #整數
    create_data = models.DateField() #時間
    
    class Meta:
        db_table = 'product' #建立資料表
        
        