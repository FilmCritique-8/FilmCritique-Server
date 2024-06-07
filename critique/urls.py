from django.urls import include, path
from .views import ReviewViewset, validate_password
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'review', ReviewViewset) # /review/로 URL 접두사로 사용됨

urlpatterns = [
    path('', include(router.urls)),
    path('review/<int:pk>/password/', validate_password),
]