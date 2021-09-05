from .models import Project, Measurement
from rest_framework import serializers 

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'latitude', 'longitude', 'created_at', 'updated_at']

class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = ['value', 'project', 'created_at', 'updated_at']