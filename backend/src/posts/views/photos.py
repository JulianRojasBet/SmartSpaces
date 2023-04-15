# Django
from django.db.models import Prefetch

# DRF
from rest_framework import viewsets

# Permissions
from rest_framework.permissions import AllowAny

# Models
from src.posts.models import Photos

# Serializers
from src.posts.serializers import PhotosModelSerializer

# Utilities
from src.utils.mixins import DeactivateModelMixin


class PhotosViewSet(DeactivateModelMixin, viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Photos.objects.filter(active=True)
    serializer_class = PhotosModelSerializer

    def get_queryset(self):
        # Return a queryset for the photos of a post
        post_pk = self.kwargs.get('post_pk', None)
        if post_pk:
            return (
                Photos.objects.filter(active=True, post_id=post_pk)
            )
        # If a post_pk is not specified, return all active photos
        else:
            return Photos.objects.filter(active=True)