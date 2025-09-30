from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course,Lesson

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments')
    body = models.TextField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name = 'comments',null = True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, related_name='comments', null = True, blank= True)
    created_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        target = self.course if self.course else self.lesson
        return f'Коментарии от {self.user } к {target}'

