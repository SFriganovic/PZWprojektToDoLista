import factory
from factory.django import DjangoModelFactory

from base.models import *

import random

class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    user = factory.Faker("first_name")
    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("sentence", nb_words=15)
    complete = factory.Faker('pybool')
    create = factory.Faker('date_time')