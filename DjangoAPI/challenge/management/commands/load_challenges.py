import csv
from django.core.management.base import BaseCommand
from challenge.models import Challenge


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("API Test - Sheet1.csv", "rt") as file:
            reader = csv.DictReader(file)
            for c in reader:
                Challenge.objects.update_or_create(**c)
