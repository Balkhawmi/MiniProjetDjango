from rest_framework import viewsets
from .models import Employe, Dirigeant, Conge
from .serializers import EmployeSerializer, DirigeantSerializer, CongeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response 

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsAuthenticated]

class DirigeantViewSet(viewsets.ModelViewSet):
    queryset = Dirigeant.objects.all()
    serializer_class = DirigeantSerializer
    permission_classes = [IsAuthenticated]

class CongeViewSet(viewsets.ModelViewSet):
    queryset = Conge.objects.all()
    serializer_class = CongeSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Dirigeant').exists():
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        employe = self.request.query_params.get('employe')
        if employe:
            queryset = queryset.filter(employe__id=employe)
        return queryset
