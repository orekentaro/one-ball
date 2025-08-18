from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseGrades(models.Model):
    """成績ベースクラス"""

    player = models.ForeignKey(
        "v1.Player", on_delete=models.PROTECT, verbose_name=_("選手")
    )
    year = models.PositiveIntegerField(verbose_name=_("年度"))
    games = models.PositiveIntegerField(verbose_name=_("試合数"), null=True, default=0)

    class Meta:
        abstract = True


class BaseFielderGrades(BaseGrades):
    """野手成績ベースクラス"""

    # 野手成績
    average = models.FloatField(verbose_name=_("打率"), null=True, default=None)
    plate_appearances = models.IntegerField(
        verbose_name=_("打席"), null=True, default=0
    )
    at_bats = models.IntegerField(verbose_name=_("打数"), null=True, default=0)
    hits = models.IntegerField(verbose_name=_("安打"), null=True, default=0)
    doubles = models.IntegerField(verbose_name=_("二塁打"), null=True, default=0)
    triples = models.IntegerField(verbose_name=_("三塁打"), null=True, default=0)
    home_runs = models.IntegerField(verbose_name=_("本塁打"), null=True, default=0)
    total_bases = models.IntegerField(verbose_name=_("塁打"), null=True, default=0)
    runs_batted_in = models.IntegerField(verbose_name=_("打点"), null=True, default=0)
    runs = models.IntegerField(verbose_name=_("得点"), null=True, default=0)
    strikeouts = models.IntegerField(verbose_name=_("三振"), null=True, default=0)
    walks = models.IntegerField(verbose_name=_("四球"), null=True, default=0)
    hit_by_pitch = models.IntegerField(verbose_name=_("死球"), null=True, default=0)
    sacrifice_bunts = models.IntegerField(verbose_name=_("犠打"), null=True, default=0)
    sacrifice_flies = models.IntegerField(verbose_name=_("犠飛"), null=True, default=0)
    stolen_bases = models.IntegerField(verbose_name=_("盗塁"), null=True, default=0)
    caught_stealing = models.IntegerField(
        verbose_name=_("盗塁死"), null=True, default=0
    )
    double_plays = models.IntegerField(verbose_name=_("併殺打"), null=True, default=0)
    on_base_percentage = models.FloatField(
        verbose_name=_("出塁率"), null=True, default=0.0
    )
    slugging_percentage = models.FloatField(
        verbose_name=_("長打率"), null=True, default=0.0
    )
    ops = models.FloatField(verbose_name=_("OPS"), null=True, default=0.0)
    runners_in_scoring_position = models.FloatField(
        verbose_name=_("得点圏"), null=True, default=0.0
    )
    errors = models.IntegerField(verbose_name=_("失策"), null=True, default=0)

    class Meta:
        abstract = True


class FielderGrades(BaseFielderGrades):
    """野手成績DB"""

    class Meta:
        verbose_name = _("野手成績")
        verbose_name_plural = _("野手成績")

    def __str__(self):
        return f"{self.player.name} - {self.subject}: {self.score}"


class FielderGradesHistory(BaseFielderGrades):
    """野手成績履歴DB"""

    date = models.DateField(_("日付"), auto_now_add=True)

    class Meta:
        verbose_name = _("野手成績履歴")
        verbose_name_plural = _("野手成績履歴")

    def __str__(self):
        return f"{self.player.name} - {self.year}年: {self.average}打率"


class BasePitcherGrades(BaseGrades):
    """投手成績ベースクラス"""

    # 投手成績
    era = models.FloatField(verbose_name=_("防御率"), null=True, default=0.0)
    appearances = models.IntegerField(verbose_name=_("登板"), null=True, default=0)
    starts = models.IntegerField(verbose_name=_("先発"), null=True, default=0)
    complete_games = models.IntegerField(verbose_name=_("完投"), null=True, default=0)
    shutouts = models.IntegerField(verbose_name=_("完封"), null=True, default=0)
    no_walks = models.IntegerField(verbose_name=_("無四球"), null=True, default=0)
    quality_starts = models.IntegerField(verbose_name=_("QS"), null=True, default=0)
    relief_finishes = models.IntegerField(
        verbose_name=_("交代完了"), null=True, default=0
    )
    wins = models.IntegerField(verbose_name=_("勝利"), null=True, default=0)
    losses = models.IntegerField(verbose_name=_("敗戦"), null=True, default=0)
    holds = models.IntegerField(verbose_name=_("ホールド"), null=True, default=0)
    hold_points = models.IntegerField(verbose_name=_("HP"), null=True, default=0)
    saves = models.IntegerField(verbose_name=_("セーブ"), null=True, default=0)
    win_percentage = models.FloatField(verbose_name=_("勝率"), null=True, default=0.0)
    innings_pitched = models.FloatField(
        verbose_name=_("投球回"), null=True, default=0.0
    )
    batters_faced = models.IntegerField(verbose_name=_("打者"), null=True, default=0)
    hits_allowed = models.IntegerField(verbose_name=_("被安打"), null=True, default=0)
    home_runs_allowed = models.IntegerField(
        verbose_name=_("被本塁打"), null=True, default=0
    )
    strikeouts_pitched = models.IntegerField(
        verbose_name=_("奪三振"), null=True, default=0
    )
    strikeout_rate = models.FloatField(
        verbose_name=_("奪三振率"), null=True, default=0.0
    )
    walks_allowed = models.IntegerField(verbose_name=_("与四球"), null=True, default=0)
    hit_by_pitch_allowed = models.IntegerField(
        verbose_name=_("与死球"), null=True, default=0
    )
    wild_pitches = models.IntegerField(verbose_name=_("暴投"), null=True, default=0)
    balks = models.IntegerField(verbose_name=_("ボーク"), null=True, default=0)
    runs_allowed = models.IntegerField(verbose_name=_("失点"), null=True, default=0)
    earned_runs = models.IntegerField(verbose_name=_("自責点"), null=True, default=0)
    quality_start_percentage = models.FloatField(
        verbose_name=_("QS率"), null=True, default=0.0
    )
    batting_average_against = models.FloatField(
        verbose_name=_("被打率"), null=True, default=0.0
    )
    strikeout_to_walk_ratio = models.FloatField(
        verbose_name=_("K/BB"), null=True, default=0.0
    )
    whip = models.FloatField(verbose_name=_("WHIP"), null=True, default=0.0)

    class Meta:
        abstract = True


class PitcherGrades(BasePitcherGrades):
    """投手成績DB"""

    class Meta:
        verbose_name = _("投手成績")
        verbose_name_plural = _("投手成績")

    def __str__(self):
        return f"{self.player.name} - {self.subject}: {self.score}"


class PitcherGradesHistory(BasePitcherGrades):
    """投手成績履歴DB"""

    date = models.DateField(_("日付"), auto_now_add=True)

    class Meta:
        verbose_name = _("投手成績履歴")
        verbose_name_plural = _("投手成績履歴")

    def __str__(self):
        return f"{self.player.name} - {self.year}年: {self.era}防御率"
