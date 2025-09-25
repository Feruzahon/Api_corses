from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from .views import RegistrUserView, ActivateView

urlpatterns = [
    path('register/',RegistrUserView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('activate/',ActivateView.as_view())
]
