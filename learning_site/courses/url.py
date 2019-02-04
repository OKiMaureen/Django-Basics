from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.course_list),
]
