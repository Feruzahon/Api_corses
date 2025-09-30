from django.urls import  path

from .views import CommentListCreateAPIView,CommentDetailAPIView
urlpatterns = [
    path('',CommentListCreateAPIView.as_view()),
    path('<int:pk>/',CommentDetailAPIView.as_view()),
]