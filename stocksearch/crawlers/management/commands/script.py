from django.core.management.base import BaseCommand, CommandError
from crawlers.models import Image
from django.db.utils import IntegrityError
import pdb
import requests

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass
        # Named (optional) arguments

    def handle(self, *args, **options):
        images = Image.objects.filter(origin='TP')
        deleted = 0
        for i, image in enumerate(images):
            response = requests.get(image.page_url)
            r.raise_for_status()
            if 'This is a premium photo' in response.text:
                image.delete()
                deleted +=1
                print('deleted '+deleted+' photos from tookapic')
            print('checking photo {} of {}'.format(i+1,len(images)))