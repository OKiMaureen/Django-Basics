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
    steps = StepSerializer(many=True, read_only=True)
    class Meta:
        fields = (
            'created_at',
            'title',
            'description', 
            'steps',   
        )
        model= models.Course
