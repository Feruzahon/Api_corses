from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email','username','role','is_active','is_staff')
    list_filter = ('role','is_active','is_staff')
    search_fields = ('email','username')
    fieldsets = UserAdmin.fieldsets+(
        (None,{'fields':('role','activation_code')}),
        )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('role',)}),
        )