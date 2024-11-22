from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, EnrollmentViewSet


router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')
router.register('lessons', LessonViewSet, basename='lessons')
router.register('enrollments', EnrollmentViewSet, basename='enrollments')

urlpatterns = [
    path('', include(router.urls)),     
]
