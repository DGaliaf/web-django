from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import re

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    city = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = "Имя пользователя"
        self.fields['email'].label = "Почта"
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Подтверждение пароля"
        self.fields['city'].label = "Город проживания"
        self.fields['password2'].help_text = "Повторите пароль, для подтверждения"


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'lastName', 'phone', 'city']

    def clean(self):
        if len(self.cleaned_data["name"]) <= 3:
            raise forms.ValidationError('Имя должно иметь 3 или более символов')

        if has_numbers(self.cleaned_data["name"]):
            raise forms.ValidationError('Имя не должно иметь цифр')

        if has_numbers(self.cleaned_data["surname"]):
            raise forms.ValidationError('Имя не должно иметь цифр')

        if has_numbers(self.cleaned_data["lastName"]):
            raise forms.ValidationError('Имя не должно иметь цифр')

        if len(self.cleaned_data["surname"]) <= 3:
            raise forms.ValidationError('Фамилия должна иметь 3 или более символов')

        if len(self.cleaned_data["lastName"]) <= 3:
            raise forms.ValidationError('Отчество должно иметь 3 или более символов')

        return self.cleaned_data


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
