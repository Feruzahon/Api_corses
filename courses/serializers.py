from rest_framework.serializers import ModelSerializer

from .models import Course, Lesson,Test


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instance):#ограничение для студента отображение ответа убрала
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request and not request.user.role =="teacher" :
            rep.pop('answer',None)
        return rep



class LessonSerializer(ModelSerializer):
    tests = TestSerializer(many=True,read_only = True)

    class Meta:
        model = Lesson
        fields= '__all__'
        

class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many = True, read_only = True)
    class Meta:
        model  = Course
        fields = '__all__'
        read_only_fields = ('user',)#означает что не надо водить вручную





