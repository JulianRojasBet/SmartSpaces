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
    model_choices = [
        ('dalle', 'Dall-e'),
        ('replicate', 'Replicate'),
        ('stable_diffusion', 'Stable-diffusion')
    ]
    AI_model = serializers.ChoiceField(choices=model_choices)
    x1_coordinate = serializers.IntegerField(required=False)
    y1_coordinate = serializers.IntegerField(required=False)
    x2_coordinate = serializers.IntegerField(required=False)
    y2_coordinate = serializers.IntegerField(required=False)