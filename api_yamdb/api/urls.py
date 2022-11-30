from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)
ENDPOINTS = [
    ('titles', TitleViewSet, 'TitleView'),
    ('genres', GenreViewSet, 'GenreView'),
    ('categories', CategoryViewSet, 'CategoryView'),
    (r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, 'reviews'),
    (
        'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
        CommentViewSet,
        'comments'
    )
]

router_v1 = DefaultRouter()

for endpoint, viewset, basename in ENDPOINTS:
    router_v1.register(endpoint, viewset, basename)



urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup', include('djoser.urls')),
    path('v1/auth/token', include('djoser.urls.jwt')),
]
