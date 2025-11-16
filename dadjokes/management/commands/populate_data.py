from django.core.management.base import BaseCommand
from dadjokes.models import Joke, Picture


class Command(BaseCommand):
    help = 'Populate database with initial jokes and pictures'

    def handle(self, *args, **options):
        # Clear existing data
        Joke.objects.all().delete()
        Picture.objects.all().delete()

        # Create jokes
        jokes_data = [
            {
                'text': 'Why don\'t scientists trust atoms? Because they make up everything!',
                'contributor_name': 'Dad Jones'
            },
            {
                'text': 'What do you call a fake noodle? An impasta!',
                'contributor_name': 'Papa Smith'
            },
            {
                'text': 'Why did the scarecrow win an award? Because he was outstanding in his field!',
                'contributor_name': 'Father Brown'
            },
            {
                'text': 'What do you call cheese that isn\'t yours? Nacho cheese!',
                'contributor_name': 'Pop Wilson'
            },
            {
                'text': 'Why don\'t eggs tell jokes? They\'d crack each other up!',
                'contributor_name': 'Dad Davis'
            },
            {
                'text': 'What do you call a bear with no teeth? A gummy bear!',
                'contributor_name': 'Papa Garcia'
            },
            {
                'text': 'How do you organize a space party? You planet!',
                'contributor_name': 'Father Martinez'
            },
            {
                'text': 'Why did the bicycle fall over? Because it was two-tired!',
                'contributor_name': 'Dad Rodriguez'
            }
        ]

        for joke_data in jokes_data:
            Joke.objects.create(**joke_data)

        # Create pictures (using placeholder image URLs)
        pictures_data = [
            {
                'image_url': 'https://picsum.photos/id/10/400/300',
                'contributor_name': 'Dad Jones'
            },
            {
                'image_url': 'https://picsum.photos/id/20/400/300',
                'contributor_name': 'Papa Smith'
            },
            {
                'image_url': 'https://picsum.photos/id/30/400/300',
                'contributor_name': 'Father Brown'
            },
            {
                'image_url': 'https://picsum.photos/id/40/400/300',
                'contributor_name': 'Pop Wilson'
            },
            {
                'image_url': 'https://picsum.photos/id/50/400/300',
                'contributor_name': 'Dad Davis'
            },
            {
                'image_url': 'https://picsum.photos/id/60/400/300',
                'contributor_name': 'Papa Garcia'
            },
            {
                'image_url': 'https://picsum.photos/id/70/400/300',
                'contributor_name': 'Father Martinez'
            }
        ]

        for picture_data in pictures_data:
            Picture.objects.create(**picture_data)

        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {len(jokes_data)} jokes and {len(pictures_data)} pictures'
        ))
