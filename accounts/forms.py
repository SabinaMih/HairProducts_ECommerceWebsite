from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ContactUs
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'age',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = '__all__'