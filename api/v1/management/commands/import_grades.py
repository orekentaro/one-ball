from logging import getLogger

from django.core.management.base import BaseCommand

from v1.tasks.import_grade import import_grade_task

logger = getLogger(__name__)


class Command(BaseCommand):
    help = "成績をインポートします"

    def handle(self, *args, **options):
        """成績をインポートする"""
        import_grade_task.delay()
