from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, LetterViewSet, NameViewSet, LikesViewSet


router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'letters', LetterViewSet)
router.register(r'names', NameViewSet)
router.register(r'likes', LikesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
