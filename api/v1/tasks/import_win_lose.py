from celery import shared_task
from logging import getLogger

from django.utils.timezone import localdate

from v1.utils.web_crawling import get_all_table_to_list
from v1.models import Team
from v1.serializers import ImportWinLoseSerializer

logger = getLogger(__name__)


@shared_task
def import_win_lose_task():
    "順位表を取得してDBに保存するタスク"

    table_data = get_all_table_to_list("https://baseball.yahoo.co.jp/npb/standings/")
    c_league = table_data[0]
    p_league = table_data[1]
    if not (c_league and p_league):
        logger.error("データの取得に失敗しました。URLを確認してください。")
        return
    today = localdate()
    for data in (c_league, p_league):
        for d in data[1:]:
            team = Team.objects.get(short_name=d[1])
            todays_data = {
                "team": team.id,
                "year": today.year,
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
            serializer = ImportWinLoseSerializer(data=todays_data)
            if serializer.is_valid():
                serializer.save()
                logger.info(
                    f" {team.short_name} の {today} のデータが正常に保存されました。"
                )
            else:
                logger.error(
                    f"順位の取得に失敗しました。 {team.short_name}: {serializer.errors}"
                )
