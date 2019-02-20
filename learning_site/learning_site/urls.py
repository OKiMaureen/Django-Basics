"""learning_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from . import views
from courses import views as view


router = routers.SimpleRouter()
router.register('courses', view.CourseViewSet)
router.register('step', view.StepViewSet)

urlpatterns = [
    path('courses/', include(('courses.url', 'courses'), namespace='courses')),
    path('admin/', admin.site.urls),
    path('', views.index),
    
    path('auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework')),
    path('api/v1/courses/', include(('courses.url', 'courses_api'), namespace='courses_api')),
    path('api/v2/', include((router.urls, 'courses_v2_api'), namespace='courses_v2_api')),
]

urlpatterns += staticfiles_urlpatterns()
