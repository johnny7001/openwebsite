# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#資料庫名稱:清單  Kkday_changhua, Kkday_chiayi, Kkday_greenisland, Kkday_hsinchu, Kkday_hualien, Kkday_kaohsiung, Kkday_keelung, Kkday_kenting, Kkday_kinmen, Kkday_lanyu,
#Kkday_liouciou, Kkday_matzu, Kkday_miaoli, Kkday_nantou, Kkday_newtaipeicity, Kkday_penghu, Kkday_pingtung, Kkday_pingxi, Kkday_taichung, Kkday_tainan,
#Kkday_taipei, Kkday_taitung, Kkday_taoyuan, Kkday_yilan, Kkday_yunlin


class Kkday(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    content = models.TextField()
    rating_count = models.IntegerField()
    star = models.FloatField()
    order_count = models.IntegerField()
    market_price = models.IntegerField()
    selling_price = models.IntegerField()
    img_url = models.CharField(max_length=255)
    data_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kkday'


class Klook(models.Model):
    title = models.CharField(max_length=255)
    star = models.FloatField(blank=True, null=True)
    market_price = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField()
    img_url = models.CharField(max_length=255)
    data_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'klook'

