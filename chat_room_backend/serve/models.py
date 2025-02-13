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
