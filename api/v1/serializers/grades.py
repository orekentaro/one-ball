from typing import Type
from django.db import models

from rest_framework import serializers

from v1.models import (
    PitcherGrades,
    PitcherGradesHistory,
    FielderGrades,
    FielderGradesHistory,
)


class BaseGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = "__all__"

    def get_history_model(self) -> Type[models.Model]:
        """使用するモデルを取得する"""
        raise NotImplementedError("This method should be implemented in subclasses")

    def to_internal_value(self, data):
        """'-' を None に変換"""
        new_data = {}
        for key, value in data.items():
            if value == "-":
                new_data[key] = None
            else:
                new_data[key] = value
        return super().to_internal_value(new_data)

    def save(self, **kwargs):
        """save"""
        GradeModel = self.Meta.model
        try:
            grade = GradeModel.objects.get(
                player=self.validated_data["player"],
                year=self.validated_data["year"],
            )
            for k, v in self.validated_data.items():
                if hasattr(grade, k):
                    setattr(grade, k, v)
        except GradeModel.DoesNotExist:
            grade = GradeModel.objects.create(**self.validated_data)
        HistoryModel = self.get_history_model()
        HistoryModel.objects.create(**self.validated_data)


class PitcherGradesSerializer(BaseGradesSerializer):
    """投手の成績シリアライザ"""

    def get_history_model(self) -> Type[models.Model]:
        """使用するモデルを取得する"""
        return PitcherGradesHistory

    class Meta:
        model = PitcherGrades
        fields = "__all__"


class FielderGradesSerializer(BaseGradesSerializer):
    """野手の成績シリアライザ"""

    def get_history_model(self) -> Type[models.Model]:
        """使用するモデルを取得する"""
        return FielderGradesHistory

    class Meta:
        model = FielderGrades
        fields = "__all__"
