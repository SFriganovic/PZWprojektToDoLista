import random

from django.db import transaction
from django.core.management.base import BaseCommand

from base.models import Task
from base.factory import (
    TaskFactory
)

NUM_TASKS = 10

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Task]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_TASKS):
            task = TaskFactory()