# Django
from django.db import models

# PostgreSQL
from django.contrib.postgres.fields import ArrayField

# Utilities
from src.utils.models import BaseModel


class Photos(BaseModel):

    post = models.ForeignKey(
        'posts.Posts',
        null=True,
        related_name='photos',
        on_delete=models.CASCADE
    )

    url = models.URLField(
        max_length=255,
        blank=True,
        default=''
    )

    tags = ArrayField(
        models.CharField(max_length=50),
        null=True,
    )


    class Meta:
        get_latest_by = 'created'
        ordering = ['-created', '-modified']