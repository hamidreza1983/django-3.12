from django.core.management.base import BaseCommand
from root.models import Skills
from faker import Faker




class Command(BaseCommand):
    help = 'text test command'

    def handle(self, *args, **kwargs):
        faker = Faker()
        for _ in range(5):
            Skills.objects.get_or_create(
                title = faker.name(),
                status = faker.pybool()
            )
            
        print ("objects create successfully")