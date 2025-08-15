from logging import getLogger

from django.core.management.base import BaseCommand
from django.utils.timezone import localdate

from v1.utils.web_crawling import get_table_to_list
from v1.models.team import Team, WinLose

logger = getLogger(__name__)


class Command(BaseCommand):
    help = "初期データを作成します"

    def handle(self, *args, **options) -> None:
        data = get_table_to_list("https://baseball.yahoo.co.jp/npb/standings/")
        if not data:
            logger.error("データの取得に失敗しました。URLを確認してください。")
            return
        today = localdate()
        for d in data[1:]:
            team = Team.objects.get(short_name=d[1])
            todays_data = {
                "rank": d[0],
                "games": d[2],
                "wins": d[3],
                "losses": d[4],
                "draws": d[5],
                "win_rate": d[6],
                "games_behind": d[7],
                "remaining_games": d[8],
                "runs_scored": d[9],
                "runs_allowed": d[10],
                "home_runs": d[11],
                "stolen_bases": d[12],
                "batting_average": d[13],
                "era": d[14],
                "errors": d[15],
            }
            try:
                win_lose = WinLose.objects.get(team=team, year=today.year)
                for k, v in todays_data.items():
                    if hasattr(win_lose, k):
                        setattr(win_lose, k, v)
                win_lose.save()
                logger.info(f"Updated WinLose for {team.short_name} in {today.year}.")

            except WinLose.DoesNotExist:
                WinLose.objects.create(team=team, year=today.year, **todays_data)
                logger.info(f"Created WinLose for {team.short_name} in {today.year}.")
