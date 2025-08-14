import glob
import os
from logging import getLogger

from django.core.management.base import BaseCommand
from django.conf import settings

from v1.constance import Constants
from v1.models import Team, Player
import csv

logger = getLogger(__name__)


class Command(BaseCommand):
    help = "初期データを作成します"

    def handle(self, *args, **options) -> None:
        """初期データを作成する"""
        self.__create_team()
        self.__create_player()

    def __create_team(self) -> None:
        """チームを作成"""
        logger.info("初期データを作成中...")
        for team_data in Constants.TEAM:
            team, created = Team.objects.get_or_create(
                id=team_data["id"],
                name=team_data["name"],
                alphabet=team_data["alphabet"],
                short_name=team_data["short_name"],
                key=team_data["key"],
                league=team_data["league"],
            )
            if created:
                logger.info(f"チーム {team.name} を作成しました。")
            else:
                logger.info(f"チーム {team.name} は既に存在します。")
        logger.info("初期データが作成されました。")

    def __create_player(self) -> None:
        """選手を作成"""
        logger.info("選手の初期データを作成中...")
        path_list = sorted(
            glob.glob(os.path.join(settings.BASE_DIR, "v1/management/ini/*.csv"))
        )
        objects = []
        for path in path_list:
            filename = os.path.basename(path)
            key = filename.split(".")[0]
            team = Team.objects.get(key=key)
            with open(path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    objects.append(Player(team=team, **row))

        Player.objects.bulk_create(objects)
        logger.info("選手の初期データが作成されました。")
