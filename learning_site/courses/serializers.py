from rest_framework import serializers
from . import models

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'description',
            'order',
            'content',
            'course',     
        )
        model= models.Step

class CourseSerializer(serializers.ModelSerializer):
    steps = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True,
        view_name= 'courses_v2_api:step-detail')
    class Meta:
        fields = (
            'created_at',
            'title',
            'description', 
            'steps',   
        )
        model= models.Course
