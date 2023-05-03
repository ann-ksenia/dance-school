from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Style_description(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    title = models.CharField(max_length=50, verbose_name='Название')
    teacher = models.OneToOneField('Teacher', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Преподаватель')


class Teacher(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя преподавателя')
    phone = models.IntegerField(verbose_name='Номер телефона')
    vk = models.URLField(verbose_name='ВК')
    youtube = models.URLField(verbose_name='Ютуб')
    telegram = models.URLField(verbose_name='Телеграм')
    video = models.URLField(verbose_name='Видео')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    phone = models.CharField(null=True, blank=True, max_length=30, default='89')
    email = models.EmailField(null=True,blank=True, default='@tpu.ru')
    ticket = models.OneToOneField('Ticket', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Абонемент')
    visits = models.TextField(verbose_name='Посещения', null=True, blank=True, default='')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('login')

class Ticket(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    amount = models.IntegerField(default=1, verbose_name='Количество занятий', null=False, blank=False)
    price = models.IntegerField(verbose_name='Стоимость', null=False, blank=False)



