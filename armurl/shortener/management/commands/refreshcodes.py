from django.core.management.base import BaseCommand, CommandError

from shortener.models import armURL

class Command(BaseCommand):
    help = 'Refreshes all shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return armURL.objects.refresh_shortcodes(items=options['items'])

