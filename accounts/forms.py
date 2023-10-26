from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CreateCustomUser(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'last_name','first_name','email','age']

class ChangeCustomUser(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'last_name','first_name','email','age']