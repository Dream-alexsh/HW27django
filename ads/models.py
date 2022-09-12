from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def value_is_null(value):
    if value < 0:
        raise ValidationError(f'{value} cannot be less than zero')


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

    role = models.CharField(max_length=10, choices=ROLE, default='member')
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(null=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    # date_joined = models.DateTimeField(null=True, blank=True, default=datetime.today())

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    slug = models.SlugField(max_length=10, unique=True, validators=[MinLengthValidator(5)], null=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(10)])

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[value_is_null])
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
