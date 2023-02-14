from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

from utils import BaseModel

User = get_user_model()


class Post(BaseModel):
    author = models.ForeignKey(
        User,
        verbose_name=_('Author'),
        on_delete=models.CASCADE,
        related_name='posts',
    )
    title = models.CharField(
        max_length=64,
    )
    body = models.TextField(
        verbose_name=_('Body'),
    )

    def __str__(self) -> str:
        return self.title
