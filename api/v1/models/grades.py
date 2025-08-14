from django.db import models
from django.utils.translation import gettext_lazy as _
from v1.models import CreateAndUpdateDateTimeMixin


class Grades(CreateAndUpdateDateTimeMixin):
    """成績DB"""

    player = models.ForeignKey(
        "v1.Player", on_delete=models.PROTECT, verbose_name=_("選手")
    )
    year = models.PositiveIntegerField(verbose_name=_("年度"))

    # 野手成績
    average = models.FloatField(verbose_name=_("打率"), null=True, default=None)
    games = models.IntegerField(verbose_name=_("試合"), null=True, default=None)
    plate_appearances = models.IntegerField(
        verbose_name=_("打席"), null=True, default=None
    )
    at_bats = models.IntegerField(verbose_name=_("打数"), null=True, default=None)
    hits = models.IntegerField(verbose_name=_("安打"), null=True, default=None)
    doubles = models.IntegerField(verbose_name=_("二塁打"), null=True, default=None)
    triples = models.IntegerField(verbose_name=_("三塁打"), null=True, default=None)
    home_runs = models.IntegerField(verbose_name=_("本塁打"), null=True, default=None)
    total_bases = models.IntegerField(verbose_name=_("塁打"), null=True, default=None)
    runs_batted_in = models.IntegerField(
        verbose_name=_("打点"), null=True, default=None
    )
    runs = models.IntegerField(verbose_name=_("得点"), null=True, default=None)
    strikeouts = models.IntegerField(verbose_name=_("三振"), null=True, default=None)
    walks = models.IntegerField(verbose_name=_("四球"), null=True, default=None)
    hit_by_pitch = models.IntegerField(verbose_name=_("死球"), null=True, default=None)
    sacrifice_bunts = models.IntegerField(
        verbose_name=_("犠打"), null=True, default=None
    )
    sacrifice_flies = models.IntegerField(
        verbose_name=_("犠飛"), null=True, default=None
    )
    stolen_bases = models.IntegerField(verbose_name=_("盗塁"), null=True, default=None)
    caught_stealing = models.IntegerField(
        verbose_name=_("盗塁死"), null=True, default=None
    )
    double_plays = models.IntegerField(
        verbose_name=_("併殺打"), null=True, default=None
    )
    on_base_percentage = models.FloatField(
        verbose_name=_("出塁率"), null=True, default=None
    )
    slugging_percentage = models.FloatField(
        verbose_name=_("長打率"), null=True, default=None
    )
    ops = models.FloatField(verbose_name=_("OPS"), null=True, default=None)
    runners_in_scoring_position = models.FloatField(
        verbose_name=_("得点圏"), null=True, default=None
    )
    errors = models.IntegerField(verbose_name=_("失策"), null=True, default=None)

    # 投手成績
    era = models.FloatField(verbose_name=_("防御率"), null=True, default=None)
    appearances = models.IntegerField(verbose_name=_("登板"), null=True, default=None)
    starts = models.IntegerField(verbose_name=_("先発"), null=True, default=None)
    complete_games = models.IntegerField(
        verbose_name=_("完投"), null=True, default=None
    )
    shutouts = models.IntegerField(verbose_name=_("完封"), null=True, default=None)
    no_walks = models.IntegerField(verbose_name=_("無四球"), null=True, default=None)
    quality_starts = models.IntegerField(verbose_name=_("QS"), null=True, default=None)
    relief_finishes = models.IntegerField(
        verbose_name=_("交代完了"), null=True, default=None
    )
    wins = models.IntegerField(verbose_name=_("勝利"), null=True, default=None)
    losses = models.IntegerField(verbose_name=_("敗戦"), null=True, default=None)
    holds = models.IntegerField(verbose_name=_("ホールド"), null=True, default=None)
    hold_points = models.IntegerField(verbose_name=_("HP"), null=True, default=None)
    saves = models.IntegerField(verbose_name=_("セーブ"), null=True, default=None)
    win_percentage = models.FloatField(verbose_name=_("勝率"), null=True, default=None)
    innings_pitched = models.FloatField(
        verbose_name=_("投球回"), null=True, default=None
    )
    batters_faced = models.IntegerField(verbose_name=_("打者"), null=True, default=None)
    hits_allowed = models.IntegerField(
        verbose_name=_("被安打"), null=True, default=None
    )
    home_runs_allowed = models.IntegerField(
        verbose_name=_("被本塁打"), null=True, default=None
    )
    strikeouts_pitched = models.IntegerField(
        verbose_name=_("奪三振"), null=True, default=None
    )
    strikeout_rate = models.FloatField(
        verbose_name=_("奪三振率"), null=True, default=None
    )
    walks_allowed = models.IntegerField(
        verbose_name=_("与四球"), null=True, default=None
    )
    hit_by_pitch_allowed = models.IntegerField(
        verbose_name=_("与死球"), null=True, default=None
    )
    wild_pitches = models.IntegerField(verbose_name=_("暴投"), null=True, default=None)
    balks = models.IntegerField(verbose_name=_("ボーク"), null=True, default=None)
    runs_allowed = models.IntegerField(verbose_name=_("失点"), null=True, default=None)
    earned_runs = models.IntegerField(verbose_name=_("自責点"), null=True, default=None)
    quality_start_percentage = models.FloatField(
        verbose_name=_("QS率"), null=True, default=None
    )
    batting_average_against = models.FloatField(
        verbose_name=_("被打率"), null=True, default=None
    )
    strikeout_to_walk_ratio = models.FloatField(
        verbose_name=_("K/BB"), null=True, default=None
    )
    whip = models.FloatField(verbose_name=_("WHIP"), null=True, default=None)

    class Meta:
        verbose_name = _("成績")
        verbose_name_plural = _("成績")

    def __str__(self):
        return f"{self.player.name} - {self.subject}: {self.score}"

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        CreateAndUpdateDateTimeMixin.save(self, *args, **kwargs)


class GradesHistory(Grades):
    """成績履歴DB"""

    date = models.DateField(_("日付"), auto_now_add=True)

    class Meta:
        verbose_name = _("成績履歴")
        verbose_name_plural = _("成績履歴")

    def __str__(self):
        return f"{self.player.name} - {self.year}年: {self.average}打率"
