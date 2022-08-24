from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name


class User(models.Model):
    ROLE = [('admin', 'Администратор'),
            ('member', 'Участник'),
            ('moderator', 'Модератор')]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLE, default='member')
    age = models.SmallIntegerField()
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
