# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Food(models.Model):
    shop = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    zone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    market_address = models.CharField(max_length=255)
    pay_list = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'food'


class Foodpanda(models.Model):
    shopname = models.CharField(db_column='shopName', max_length=255)  # Field name made lowercase.
    star = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    shopurl = models.CharField(db_column='shopUrl', max_length=255)  # Field name made lowercase.
    tag = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'foodpanda'

