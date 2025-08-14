from logging import getLogger

from django.core.management.base import BaseCommand

from v1.constance import Constants
from v1.models import Team

logger = getLogger(__name__)


class Command(BaseCommand):
    help = "初期データを作成します"

    def handle(self, *args, **options) -> None:
        """初期データを作成する"""
        self.__create_team()

    def __create_team(self) -> None:
        """チームを作成"""
        logger.info("初期データを作成中...")
        for team_data in Constants.TEAM:
            team, created = Team.objects.get_or_create(
                id=team_data["id"],
                name=team_data["name"],
                defaults={
                    "alphabet": team_data["alphabet"],
                    "short_name": team_data["short_name"],
                },
            )
            if created:
                logger.info(f"チーム {team.name} を作成しました。")
            else:
                logger.info(f"チーム {team.name} は既に存在します。")
        for team in Constants.TEAM:
            logger.info(
                f"チーム名: {team['name']}, アルファベット: {team['alphabet']}, 短縮名: {team['short_name']}"
            )
        logger.info("初期データが作成されました。")
