from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from  .models import Course,Lesson,Test
from  .serializers import CourseSerializer,LessonSerializer,TestSerializer
from  .permissions import IsTeacher

#grud - для курса
class CourseListCreateAPIView(generics.ListCreateAPIView):# добавляет обьек и возвращает список всех обьектов GET
    queryset = Course.objects.all() # возвращает все обьекты  из БД
    serializer_class = CourseSerializer#данные превращаем на json  и наоборот

    def get_permissions(self):
        if self.request.method == "POST":# если создание курса то тут означает только авторизованным и для учителя 
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)#берем из токена

class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):#получение, обновление и удаление (GET,PUT,PATCH,DELETE)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer    

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]

#grud - для уроков
class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]
        


class LessonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]


#grud - для тестов

class TestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]


class TestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]
