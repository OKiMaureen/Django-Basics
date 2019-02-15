from django.shortcuts import get_object_or_404, render
from rest_framework import generics, viewsets, mixins, permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Course, Step
from .serializers import StepSerializer, CourseSerializer

# Create your views here.


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StepListCreateView(generics.ListCreateAPIView):
    serializer_class = StepSerializer

    def get_queryset(self):
       return Step.objects.all().filter(course_id=self.kwargs.get('course_pk'))

    def perform_create(self, serializer):
        course = get_object_or_404(
            Course, pk=self.kwargs.get('course_pk')
        )
        serializer.save(course=course)


class StepRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Step.objects.all()
   serializer_class = StepSerializer

   def get_object(self):
       return get_object_or_404(
           Step,
           course_id=self.kwargs.get('course_pk'),
           pk=self.kwargs.get('pk')
       )

class IsSuperUser (permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            if request.method == 'DELETE':
               return False
        return True

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsSuperUser,
        permissions.DjangoModelPermissions,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    @detail_route(methods=['get'])
    def steps(self, request, pk=None):
        self.pagination_class.page_size = 1
        steps = Step.objects.filter(course_id=pk)
        page = self.paginate_queryset(steps)
        if page is not None:
            serializer = StepSerializer(
               page, many=True
            )
            return self.get_paginated_response(serializer.data)
        serializer = StepSerializer(
               steps, many=True
            )
        return Response(serializer.data)

class StepViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer





    