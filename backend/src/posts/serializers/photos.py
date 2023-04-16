# DRF
from rest_framework import serializers

# Models
from src.posts.models import Photos


class PhotosModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photos
        exclude = ['modified', 'active']
        read_only_fields = ['id', 'created_by', 'created']


class SuggestionsSerializer(serializers.Serializer):

    photo_url = serializers.URLField(max_length=255, allow_blank=False)
    action = serializers.CharField(max_length=255, allow_blank=False)