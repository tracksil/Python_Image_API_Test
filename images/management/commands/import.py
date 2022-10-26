from django.core.management.base import BaseCommand
import requests
from ...models import Images


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Command is executing')
        response = requests.get('https://jsonplaceholder.typicode.com/photos')
        for r in response.json():
            image = Images(title=r['title'], album_id=r['albumId'], url=r['url'])
            image.save()
        print('Command executed')
