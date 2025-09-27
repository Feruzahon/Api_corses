from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Course(models.Model):
    title_course = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE,related_name ='courses',blank=False,null = False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title_course
     
class Lesson(models.Model):
    title_lesson = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title_lesson}({self.course.title_course})"
    

class Test(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='tests')
    question = models.TextField()
    answer = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Test for {self.lesson.title_lesson}"
    