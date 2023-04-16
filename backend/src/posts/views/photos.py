# DRF
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import AllowAny

# Models
from src.posts.models import Posts, Photos

# Serializers
from src.posts.serializers import PhotosModelSerializer, SuggestionsSerializer

# Utilities
from src.utils.mixins import DeactivateModelMixin

# AI
from AI.api import suggestions

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

    def get_serializer_class(self):
        ''' Return serializer based on action. '''
        if self.action == 'suggestions':
            return SuggestionsSerializer
        else:
            return PhotosModelSerializer

    @action(detail=True, methods=['get', 'post'], url_path='suggestions')
    def suggestions(self, request, *args, **kwargs):

        if request.method == 'GET':
            post_id = kwargs.get('post_pk')
            post = Posts.objects.get(id=post_id)
            reviews = post.reviews
            actions = suggestions(reviews)
            return Response(actions, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            # TODO: transformar la imagen y obtener sugerencias
            # data = request.data
            return Response("Sugerencias generadas", status=status.HTTP_200_OK)