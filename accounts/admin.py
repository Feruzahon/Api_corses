from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    #это какие колонки показывается в списке пользователей
    list_display = ('email','username','role','is_active','is_staff')
    #это филтры справа в админке  надо для филтирации по ролям активности и стаф
    list_filter = ('role','is_active','is_staff')
    #это поиск пользователя по почте и имени
    search_fields = ('email','username')

#это какие поля показывает при редактировании пользователя по умолчанию уже есть имя емаил пароль
    fieldsets = UserAdmin.fieldsets+(
        (None,{'fields':('role','activation_code')}),
        )
#это какие поля доступны при создание нового пользователя  через админку
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('role',)}),
        )