from django import forms
from .models import Car, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CarForm(forms.ModelForm): # Форма для автомобиля
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']

class CommentForm(forms.ModelForm): # Форма для комментария к автомобилю
    class Meta:
        model = Comment
        fields = ['content']


class SignUpForm(UserCreationForm): # Форма регистрации пользователя
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
