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
    def validate_order(self,value):
        if value < 0:
            raise serializers.ValidationError(
                'Order cannot be a negative number'
            )
        return value

class CourseSerializer(serializers.ModelSerializer):
    steps = serializers.PrimaryKeyRelatedField(
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
