from django.urls import path, include

from .views import (
    CourseListCreateAPIView,CourseDetailAPIView,
    LessonListCreateAPIView,LessonDetailAPIView,
    TestListCreateAPIView,TestDetailAPIView


)
urlpatterns = [
    
    path('',CourseListCreateAPIView.as_view()),
    path('<int:pk>/',CourseDetailAPIView.as_view()),

    path('lessons/',LessonListCreateAPIView.as_view()),
    path('lessons/<int:pk>/',LessonDetailAPIView.as_view()),

    path('tests/',TestListCreateAPIView.as_view()),
    path('tests/<int:pk>/',TestDetailAPIView.as_view())
]