# DRF
from rest_framework import viewsets

# Permissions
from rest_framework.permissions import AllowAny

# Models
from src.posts.models import Posts

# Serializers
from src.posts.serializers import PostsModelSerializer

# Utilities
from src.utils.mixins import DeactivateModelMixin


class PostsViewSet(DeactivateModelMixin, viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Posts.objects.filter(active=True)
    serializer_class = PostsModelSerializer