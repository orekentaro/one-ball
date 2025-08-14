from django.db import models
from django.utils.translation import gettext_lazy as _

from v1.constance import Constants
from v1.models import CreateAndUpdateDateTimeMixin


class Team(models.Model):
    """球団名DB"""

    name = models.CharField(max_length=100, verbose_name=_("チーム名"))
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


class WinLose(CreateAndUpdateDateTimeMixin):
    """勝敗DB"""

    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_("チーム"))
    year = models.PositiveIntegerField(verbose_name=_("年度"))
    wins = models.IntegerField(verbose_name=_("勝利"), default=0)
    losses = models.IntegerField(verbose_name=_("敗戦"), default=0)
    draws = models.IntegerField(verbose_name=_("引分"), default=0)

    class Meta:
        verbose_name = _("勝敗")
        verbose_name_plural = _("勝敗")

    def __str__(self):
        return f"{self.team.name} {self.year}年: {self.wins}勝 {self.losses}敗 {self.draws}分"


class WinLoseHistory(WinLose):
    """勝敗履歴DB"""

    date = models.DateField(verbose_name=_("日付"), auto_now_add=True)

    class Meta:
        verbose_name = _("勝敗履歴")
        verbose_name_plural = _("勝敗履歴")
        ordering = ["-year", "team__name"]

    def __str__(self):
        return f"{self.team.name} {self.year}年: {self.wins}勝 {self.losses}敗 {self.draws}分"
