# Django
from django.db import models

# PostgreSQL
from django.contrib.postgres.fields import ArrayField

# Utilities
from src.utils.models import BaseModel


class Posts(BaseModel):

    cover_photo_url = models.URLField(
        max_length=255,
        blank=True,
        default=''
    )

    description = models.TextField(
        blank=True,
        default=''
    )

    reviews = ArrayField(
        models.TextField(max_length=500),
        null=True,
    )


    class Meta:
        get_latest_by = 'created'
        ordering = ['-created', '-modified']