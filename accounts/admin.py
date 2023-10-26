from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CreateCustomUser, ChangeCustomUser
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CreateCustomUser
    form = ChangeCustomUser
    model = CustomUser
    list_display = ['username', 'email', 'first_name','last_name','age','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields' : ('age',)}),
        )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields' : ('age',)}),)

admin.site.register(CustomUser, CustomUserAdmin)

