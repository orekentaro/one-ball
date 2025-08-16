from rest_framework import serializers

from v1.models import WinLose, WinLoseHistory


class ImportWinLoseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WinLose
        fields = "__all__"

    def save(self, **kwargs):
        """save"""
        try:
            win_lose = WinLose.objects.get(
                team=self.validated_data["team"], year=self.validated_data["year"]
            )
            for k, v in self.validated_data.items():
                if hasattr(win_lose, k):
                    setattr(win_lose, k, v)
            win_lose.save()
        except WinLose.DoesNotExist:
            WinLose.objects.create(**self.validated_data)

        WinLoseHistory.objects.create(**self.validated_data)
