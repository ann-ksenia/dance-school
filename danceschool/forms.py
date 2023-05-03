from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.images import get_image_dimensions

from danceschool.models import Profile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин",widget=forms.TextInput(attrs={"class": "form-control", "rows": 5, "cols": 10}))
    password = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={"class": "form-control", "rows": 5, "cols": 10}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = "Логин")
    phone = forms.CharField(label="Photo")
    photo = forms.ImageField(required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','password1', 'password2',)


class UpUser(forms.ModelForm):
    username = forms.CharField(label="Логин",widget=forms.TextInput(attrs={"class": "form-control", "rows": 5, "cols": 10}))

    class Meta:
        model = User
        fields =('username',)

class UpProfile(forms.ModelForm):
    photo = forms.ImageField(label="New photo", widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    phone = forms.CharField(label="New phone", widget=forms.TextInput(attrs={"class": "form-control", "rows": 5, "cols": 10}),
                            max_length=11, min_length=11, help_text="Input your full telephone number starting with a digit, not a '+'")
    email = forms.EmailField(label="New email", widget=forms.EmailInput(attrs={"class": "form-control", "rows": 5, "cols": 10}))

    class Meta:
        model = Profile
        fields = ('photo', 'phone','email')




