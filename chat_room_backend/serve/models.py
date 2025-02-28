from django.db import models

# Create your models here.



class User(models.Model):
    id=models.IntegerField('账号',primary_key=True)
    name=models.CharField('昵称',max_length=32,null=False)
    password=models.CharField('密码',max_length=32)

    class Meta:
        db_table='Chat_User'



class Friend(models.Model):
    time=models.AutoField('时间',primary_key=True)
    id1=models.IntegerField('账号1')
    id2=models.IntegerField('账号2')

    class Meta:
        db_table='Chat_Friend'

class Friend_Request(models.Model):
    time=models.AutoField('时间',primary_key=True)
    user1=models.CharField('用户1',max_length=32)
    user2=models.CharField('用户2',max_length=32,)

    class Meta:
        db_table='Chat_Friend_Request'

class Messages(models.Model):
    user1=models.CharField('用户一',max_length=32)
    user2=models.CharField('用户二',max_length=32)
    Message=models.CharField('消息',max_length=128)
    time=models.CharField('时间',max_length=32)

    class Meta:
        db_table='Chat_Private_Message'
        ordering = ['time']

class Group_Messages(models.Model):
    name=models.CharField('聊天室名称',max_length=32)
    user=models.CharField('发送人',max_length=32)
    Message=models.CharField('消息',max_length=128)
    time=models.CharField('时间',max_length=32)

    class Meta:
        db_table='Chat_Group_Message'
        ordering = ['time']
