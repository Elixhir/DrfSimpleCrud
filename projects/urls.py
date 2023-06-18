from rest_framework import routers
from .viewsets import ProjectViewSet
router=routers.DefaultRouter()

router.register('viewsets/project',ProjectViewSet,'projects')

urlpatterns =router.urls

