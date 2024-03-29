"""
Django command to wait for the databse to be available

"""
from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Psycop2Error

from django.db.utils import OperationalError

import time


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("Waiting for database ...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycop2Error, OperationalError):
                self.stdout.write('Database unvaibale, attendez vous une \
                                   second ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database Ok!"))
