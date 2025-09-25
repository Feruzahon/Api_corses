from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


from .serializers import RegisterSerializer
from .models import CustomUser
from .permissions import IsAuthenticateUser,IsNotAuthenticated

class RegistrUserView(APIView):
    permission_classes = [IsNotAuthenticated]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response('Вы успешно зарегистрировались',status = 201)
    
class ActivateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        activation_code = request.query_params.get('u')
        user = get_object_or_404(CustomUser, activation_code = activation_code)
        user.is_active = True
        user.activation_code=''
        user.save()
        return redirect('https://google.com')    