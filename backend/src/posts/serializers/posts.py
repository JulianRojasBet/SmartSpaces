# DRF
from rest_framework import serializers

# Models
from src.posts.models import Posts


class PostsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        exclude = ['modified', 'active']
        read_only_fields = ['id', 'created_by', 'created']