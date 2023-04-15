# DRF
from rest_framework import serializers

# Models
from src.posts.models import Photos


class PhotosModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photos
        exclude = ['modified', 'active']
        read_only_fields = ['id', 'created_by', 'created']