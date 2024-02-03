from django.core.management.base import BaseCommand
from closet.models import ClosetClothes
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Add clothes to the ClosetClothes table manually'

    def handle(self, *args, **options):
        new_clothes = ClosetClothes(
            category='Shirt',
            color='Blue',
            image='image/top.jpeg',
            add_date='2024-01-28T12:00:00',  # Provide a valid date and time
            user=User.objects.get(username='admin')  # Provide the actual username
        )
        new_clothes.save()
        self.stdout.write(self.style.SUCCESS('Clothes added successfully!'))
