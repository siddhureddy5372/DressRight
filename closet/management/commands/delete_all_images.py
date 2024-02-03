from django.core.management.base import BaseCommand
from closet.models import UploadedImage
import os

class Command(BaseCommand):
    help = 'Deletes all images and related database records'

    def handle(self, *args, **kwargs):
        # Get all UploadedImage instances
        images = UploadedImage.objects.all()

        # Iterate through instances and delete records and files
        for image in images:
            image_path = image.image.path
            self.stdout.write(f'Deleting image at path: {image_path}')

            # Delete the image file
            if os.path.exists(image_path):
                os.remove(image_path)

            # Delete the database record
            image.delete()

        self.stdout.write(self.style.SUCCESS('All images deleted successfully.'))
