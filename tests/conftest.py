from pytest_factoryboy import register

from tests.factories import AdFactory, SelectionFactory, UserFactory, CategoryFactory

pytest_plugins = 'tests.fixtures'

register(AdFactory)
register(SelectionFactory)
register(UserFactory)
register(CategoryFactory)