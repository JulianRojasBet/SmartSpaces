# Django
from django.urls import include, path

# DRF
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter

# Views
from src.posts import views

router = DefaultRouter()

router.register(r'posts', views.PostsViewSet, basename='posts')
router.register(r'photos', views.PhotosViewSet, basename='photos')

# Nested Routes
posts = routers.SimpleRouter()
posts.register(r'posts', views.PostsViewSet, basename='posts')

photos = routers.NestedSimpleRouter(posts, r'posts', lookup='post')
photos.register(r'photos', views.PhotosViewSet, basename='posts-photos')


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(posts.urls)),
    path(r'', include(photos.urls))
]
