from django.db import models
from django.utils.translation import gettext_lazy as _


class CreateAndUpdateDateTimeMixin(models.Model):
    """CreateAndUpdateDateTimeMixin"""

    created_at = models.DateTimeField(_("作成日時"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_("更新日時"), auto_now=True, null=True)

    class Meta:
        abstract = True
