from django.db import models

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'message' #建立資料表

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    # class Meta:
    #     db_table = 'message_mood'

    def __str__(self):
        return self.status

class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete = models.CASCADE) #心情, Mood做完外鍵, 連結到Mood裡面的status
    nickname = models.CharField(max_length=10, default='不願意透漏身分的人')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10) #刪除此篇文章的密碼
    pub_time = models.DateTimeField(auto_now=True) #自動填入修改時間
    enabled = models.BooleanField(default=False) #至否要把資料顯示在網頁上

    # class Meta:
    #     db_table = 'message_post' #建立資料表
    def __str__(self):
        return self.message
