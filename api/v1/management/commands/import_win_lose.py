from logging import getLogger

from django.core.management.base import BaseCommand

from v1.tasks.import_win_lose import import_win_lose_task

logger = getLogger(__name__)


class Command(BaseCommand):
    help = "順位表を取得してDBに保存する"

    def handle(self, *args, **options) -> None:
        import_win_lose_task.delay()
