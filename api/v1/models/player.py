from django.db import models
from django.utils.translation import gettext_lazy as _


class Player(models.Model):
    """選手名DB"""

    team = models.ForeignKey(
        "v1.Team", on_delete=models.PROTECT, verbose_name=_("チーム")
    )
    no = models.CharField(max_length=3, verbose_name=_("背番号"))
    name = models.CharField(max_length=100, verbose_name=_("選手名"))
    position = models.CharField(
        max_length=50,
        verbose_name=_("登録ポジション"),
        choices=(
            ("P", _("投手")),
            ("C", _("捕手")),
            ("IF", _("内野手")),
            ("OF", _("外野手")),
        ),
    )
    height = models.PositiveIntegerField(verbose_name=_("身長"))
    weight = models.PositiveIntegerField(verbose_name=_("体重"))
    birthday = models.DateField(verbose_name=_("生年月日"))
    pitch = models.CharField(
        max_length=50,
        verbose_name=_("投球"),
        choices=(
            ("R", _("右投げ")),
            ("L", _("左投げ")),
        ),
    )
    bat = models.CharField(
        max_length=50,
        verbose_name=_("打席"),
        choices=(
            ("R", _("右打ち")),
            ("L", _("左打ち")),
        ),
    )
    salary = models.PositiveIntegerField(verbose_name=_("年俸"), default=0)

    class Meta:
        verbose_name = _("選手")
        verbose_name_plural = _("選手")

    def __str__(self):
        return self.name
