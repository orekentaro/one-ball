from django.db import models
from django.utils.translation import gettext_lazy as _

from v1.constance import Constants
from v1.models import CreateAndUpdateDateTimeMixin


class Team(models.Model):
    """球団名DB"""

    name = models.CharField(max_length=100, unique=True, verbose_name=_("チーム名"))
    short_name = models.CharField(max_length=50, unique=True, verbose_name=_("短縮名"))
    alphabet = models.CharField(
        max_length=10, unique=True, verbose_name=_("アルファベット")
    )
    key = models.CharField(max_length=50, unique=True, verbose_name=_("キー"))
    league = models.CharField(
        max_length=50, verbose_name=_("リーグ"), choices=Constants.LEAGUE
    )

    class Meta:
        verbose_name = _("チーム")
        verbose_name_plural = _("チーム")

    def __str__(self):
        return self.name


class BaseWinLose(CreateAndUpdateDateTimeMixin):
    """勝敗ベースクラス"""

    team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name=_("チーム"))
    year = models.PositiveIntegerField(verbose_name=_("年度"))
    rank = models.PositiveIntegerField(verbose_name=_("順位"))
    games = models.PositiveIntegerField(verbose_name=_("試合"), default=0)
    wins = models.PositiveIntegerField(verbose_name=_("勝利"), default=0)
    losses = models.PositiveIntegerField(verbose_name=_("敗戦"), default=0)
    draws = models.PositiveIntegerField(verbose_name=_("引分"), default=0)
    win_rate = models.CharField(verbose_name=_("勝率"), default=".000")
    games_behind = models.CharField(verbose_name=_("勝差"), default="0.0")
    remaining_games = models.PositiveIntegerField(verbose_name=_("残試合"), default=0)
    runs_scored = models.PositiveIntegerField(verbose_name=_("得点"), default=0)
    runs_allowed = models.PositiveIntegerField(verbose_name=_("失点"), default=0)
    home_runs = models.PositiveIntegerField(verbose_name=_("本塁打"), default=0)
    stolen_bases = models.PositiveIntegerField(verbose_name=_("盗塁"), default=0)
    batting_average = models.CharField(verbose_name=_("打率"), default=".000")
    era = models.CharField(verbose_name=_("防御率"), default="0.00")
    errors = models.PositiveIntegerField(verbose_name=_("失策"), default=0)

    class Meta:
        abstract = True


class WinLose(BaseWinLose):
    """勝敗DB"""

    class Meta:
        verbose_name = _("勝敗")
        verbose_name_plural = _("勝敗")

    def __str__(self):
        return f"{self.team.name} {self.year}年: {self.wins}勝 {self.losses}敗 {self.draws}分"


class WinLoseHistory(BaseWinLose):
    """勝敗履歴DB"""

    date = models.DateField(verbose_name=_("日付"), auto_now_add=True)

    class Meta:
        verbose_name = _("勝敗履歴")
        verbose_name_plural = _("勝敗履歴")
        ordering = ["-year", "team__name"]

    def __str__(self):
        return f"{self.team.name} {self.year}年: {self.wins}勝 {self.losses}敗 {self.draws}分"
