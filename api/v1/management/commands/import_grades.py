import time
from logging import getLogger

from django.core.management.base import BaseCommand
from django.utils.timezone import localdate

from v1.models import Player, Team
from v1.serializers import PitcherGradesSerializer, FielderGradesSerializer
from v1.utils.data_fix import array_to_dict
from v1.utils.url import get_grade_url
from v1.utils.web_crawling import get_one_table_to_list

logger = getLogger(__name__)


class Command(BaseCommand):
    help = "成績をインポートします"

    def handle(self, *args, **options):
        """成績をインポートする"""
        logger.info("成績インポート処理を開始します")
        for team in Team.objects.all():
            logger.info(f"チーム: {team.name} の成績をインポートします")
            self.__save_pitcher_data(team)
            self.__save_fielder_data(team)
            time.sleep(5)

    def __get_fielder_data_header(self) -> list[str]:
        """野手データのヘッダーを取得する"""
        return [
            "position",
            "no",
            "name",
            "average",
            "games",
            "plate_appearances",
            "at_bats",
            "hits",
            "doubles",
            "triples",
            "home_runs",
            "total_bases",
            "runs_batted_in",
            "runs_scored",
            "strikeouts",
            "walks",
            "hit_by_pitch",
            "sacrifice_bunts",
            "sacrifice_flies",
            "stolen_bases",
            "caught_stealing",
            "double_plays",
            "on_base_percentage",
            "slugging_percentage",
            "ops",
            "runners_in_scoring_position",
            "errors",
        ]

    def __get_pitchers_data_header(self) -> list[str]:
        """投手データのヘッダーを取得する"""
        return [
            "no",
            "name",
            "era",
            "games",
            "starts",
            "complete_games",
            "shutouts",
            "quality_starts",
            "wins",
            "losses",
            "holds",
            "hold_points",
            "saves",
            "win_percentage",
            "innings_pitched",
            "hits_allowed",
            "home_runs_allowed",
            "strikeouts_pitched",
            "strikeout_rate",
            "walks_allowed",
            "hit_by_pitch_allowed",
            "wild_pitches",
            "balks",
            "runs_allowed",
            "earned_runs",
            "batting_average_against",
            "strikeout_to_walk_ratio",
            "whip",
        ]

    def __save_fielder_data(self, team: Team) -> None:
        """野手データを保存する"""
        url = get_grade_url(team, "b")
        table_data = get_one_table_to_list(url)
        table_data.pop(0)
        table_data.pop(len(table_data) - 1)
        table_data.insert(0, self.__get_fielder_data_header())
        year = localdate().year
        for data in array_to_dict(table_data):
            if len(no := data.pop("no", None)) < 3:
                data.pop("position", None)
                name = data.pop("name", None)
                try:
                    player = Player.objects.get(team=team, no=no, name=name)
                except Player.DoesNotExist:
                    logger.warning(
                        f"選手が見つかりません: {name} (チーム: {team.name}, 背番号: {no})"
                    )
                    continue
                serializer = FielderGradesSerializer(
                    data={**data, "player": player.pk, "year": year}
                )
                if serializer.is_valid():
                    serializer.save()
                else:
                    logger.warning(f"野手成績の保存に失敗しました: {serializer.errors}")

    def __save_pitcher_data(self, team: Team) -> None:
        """投手データを保存する"""
        url = get_grade_url(team, "p")
        table_data = get_one_table_to_list(url)
        table_data.pop(0)
        table_data.pop(len(table_data) - 1)
        table_data.insert(0, self.__get_pitchers_data_header())
        year = localdate().year
        for data in array_to_dict(table_data):
            if len(no := data.pop("no", None)) < 3:
                name = data.pop("name", None)
                try:
                    player = Player.objects.get(team=team, no=no, name=name)
                except Player.DoesNotExist:
                    logger.warning(
                        f"選手が見つかりません: {name} (チーム: {team.name}, 背番号: {no})"
                    )
                    continue
                serializer = PitcherGradesSerializer(
                    data={**data, "player": player.pk, "year": year}
                )
                if serializer.is_valid():
                    serializer.save()
                else:
                    logger.warning(f"投手成績の保存に失敗しました: {serializer.errors}")
