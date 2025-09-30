from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from  .models import Course,Lesson,Test
from  .serializers import CourseSerializer,LessonSerializer,TestSerializer
from  .permissions import IsTeacher

#grud - для курса
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all() 
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'user']   
    search_fields = ['title', 'description'] 
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request}) 
        return context

class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):#получение, обновление и удаление (GET,PUT,PATCH,DELETE)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer    

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request}) 
        return context

#grud - для уроков
class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['course', 'title']  
    search_fields = ['title', 'content'] 
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]
    

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request}) 
        return context
        


class LessonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})  
        return context


#grud - для тестов

class TestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request}) 
        return context


class TestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated()]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request}) 
        return context
