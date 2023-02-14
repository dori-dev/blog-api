from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_('Created Time'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated Time'),
        auto_now=True,
    )

    class Meta:
        abstract = True
