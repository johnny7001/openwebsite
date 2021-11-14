# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HinataYoutube(models.Model):
    title = models.CharField(max_length=255)
    videourl = models.CharField(db_column='videoUrl', max_length=255)  # Field name made lowercase.
    imgurl = models.CharField(db_column='imgUrl', max_length=255)  # Field name made lowercase.
    viewcount = models.IntegerField(db_column='viewCount')  # Field name made lowercase.
    likecount = models.IntegerField(db_column='likeCount')  # Field name made lowercase.
    dislikecount = models.IntegerField(db_column='dislikeCount')  # Field name made lowercase.
    commentcount = models.CharField(db_column='commentCount', max_length=255)  # Field name made lowercase.
    uploaddate = models.CharField(db_column='uploadDate', max_length=255)  # Field name made lowercase.
    published_date = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hinata_youtube'



class NogiYoutube(models.Model):
    title = models.CharField(max_length=255)
    videourl = models.CharField(db_column='videoUrl', max_length=255)  # Field name made lowercase.
    imgurl = models.CharField(db_column='imgUrl', max_length=255)  # Field name made lowercase.
    viewcount = models.IntegerField(db_column='viewCount')  # Field name made lowercase.
    likecount = models.IntegerField(db_column='likeCount')  # Field name made lowercase.
    dislikecount = models.IntegerField(db_column='dislikeCount')  # Field name made lowercase.
    commentcount = models.CharField(db_column='commentCount', max_length=255)  # Field name made lowercase.
    uploaddate = models.CharField(db_column='uploadDate', max_length=255)  # Field name made lowercase.
    published_date = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nogi_youtube'



class SakuYoutube(models.Model):
    title = models.CharField(max_length=255, db_collation='utf8_general_ci')
    videourl = models.CharField(db_column='videoUrl', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    imgurl = models.CharField(db_column='imgUrl', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    viewcount = models.IntegerField(db_column='viewCount')  # Field name made lowercase.
    likecount = models.IntegerField(db_column='likeCount')  # Field name made lowercase.
    dislikecount = models.IntegerField(db_column='dislikeCount')  # Field name made lowercase.
    commentcount = models.CharField(db_column='commentCount', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    uploaddate = models.CharField(db_column='uploadDate', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    published_date = models.CharField(max_length=255, db_collation='utf8_general_ci')

    class Meta:
        managed = False
        db_table = 'saku_youtube'



