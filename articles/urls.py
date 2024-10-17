from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter 
from .views import ArticleViewSet
from .views import index


router = DefaultRouter()
router.register("articles",ArticleViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r'^(?!api/).*$', index),
]