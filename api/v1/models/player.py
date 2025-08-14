from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete.models import SafeDeleteModel

from v1.constance import Constants
from v1.models import CreateAndUpdateDateTimeMixin


class Player(SafeDeleteModel, CreateAndUpdateDateTimeMixin):
    """選手名DB"""

    team = models.ForeignKey(
        "v1.Team", on_delete=models.PROTECT, verbose_name=_("チーム")
    )
    no = models.CharField(max_length=3, verbose_name=_("背番号"))
    name = models.CharField(max_length=100, verbose_name=_("選手名"))
    position = models.CharField(
        max_length=50,
        verbose_name=_("登録ポジション"),
        choices=Constants.POSITION,
    )
    height = models.PositiveIntegerField(verbose_name=_("身長"))
    weight = models.PositiveIntegerField(verbose_name=_("体重"))
    birthday = models.DateField(verbose_name=_("生年月日"))
    age = models.PositiveIntegerField(verbose_name=_("年齢"), default=0)
    years = models.PositiveIntegerField(verbose_name=_("年数"), default=0)
    pitch = models.CharField(
        max_length=50,
        verbose_name=_("投球"),
        choices=Constants.PITCH,
    )
    bat = models.CharField(
        max_length=50,
        verbose_name=_("打席"),
        choices=Constants.BAT,
    )
    salary = models.PositiveIntegerField(verbose_name=_("年俸"), default=0)

    class Meta:
        verbose_name = _("選手")
        verbose_name_plural = _("選手")

    def __str__(self):
        return self.name
