from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.views import ReviewViewSet


ENDPOINTS = [
    # (r'reviews', ReviewViewSet, 'reviews'),
]

router_v1 = DefaultRouter()

for endpoint, viewset, basename in ENDPOINTS:
    router_v1.register(endpoint, viewset, basename=basename)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', include('djoser.urls')),
    path('v1/auth/token/', include('djoser.urls.jwt')),
]
