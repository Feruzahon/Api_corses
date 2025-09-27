from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    p2 = serializers.CharField(min_length = 8,max_length = 20, required = True, write_only = True)
    role = serializers.ChoiceField(choices = [('teacher','учитель'),('students','Студент')], default = 'student')

    class Meta:
        model = User
        fields = ('email','password','p2','role')


    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('p2')

        if p1 != p2 :
            raise serializers.ValidationError('Пароль не совпал!!!')
        return attrs
        
    
    def create(self, validated_data):
        user =User.objects.create_user(**validated_data)# здесь хэшируем пароль 
        return user