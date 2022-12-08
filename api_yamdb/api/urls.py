from django.urls import include, path
from api.v1.urls import router_v1
from api.v1.views import SignupViewSet, TokenViewSet

auth = [
    path('auth/signup/', SignupViewSet.as_view()),
    path('auth/token/', TokenViewSet.as_view()),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include(auth)),
]
