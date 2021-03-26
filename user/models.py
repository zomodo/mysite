from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserInfo(AbstractUser):
    username = models.CharField(max_length=12,unique=True,verbose_name='用户名称')
    password = models.CharField(max_length=128,verbose_name='用户密码')
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(max_length=13,verbose_name='手机')


    def __str__(self):
        return self.username

    class Meta:
        verbose_name=verbose_name_plural='用户信息'
