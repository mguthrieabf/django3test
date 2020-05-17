from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('fishcake - inside command')
        os.system("env")
