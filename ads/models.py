from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLE = [('admin', 'Администратор'),
            ('member', 'Участник'),
            ('moderator', 'Модератор')]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    role = models.CharField(max_length=50, choices=ROLE, default='member')
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    is_published = models.BooleanField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    def __str__(self):
        return self.name
