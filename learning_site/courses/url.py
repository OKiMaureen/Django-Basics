from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='list'),
    path('<int:course_pk>/<int:step_pk>/', views.step_detail, name='step'),
    path('<int:pk>/', views.course_detail, name='detail'),
    path('list/', views.CourseListCreateView.as_view(), name='course_list_api'),
    path('list/<int:pk>/', 
        views.CourseRetrieveUpdateDestroyView.as_view(), 
        name='course_list_api'
        ),
    path('list/<int:course_pk>/step/', 
        views.StepListCreateView.as_view(), 
        name='step_list_api'
        ),
    path('list/<int:course_pk>/step/<int:pk>', 
        views.StepRetrieveUpdateDestroyView.as_view(), 
        name='step_detail_api'
        ),

]
