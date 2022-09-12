import factory

from ads.models import Ad, Selection, User, Category


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    author = factory.SubFactory(UserFactory)
    price = 100
    is_published = False

class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

