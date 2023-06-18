from rest_framework import viewsets,permissions
from .models import Project
from .serializers import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ProjectSerializers
