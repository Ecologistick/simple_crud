from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from django.shortcuts import get_object_or_404
from .serializers import MeasurementSerializer, ProjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    """ViewSet для измерения."""

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
