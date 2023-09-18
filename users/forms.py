from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from users import models
from captcha.fields import CaptchaField


class loginForm(forms.Form):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(attrs={"placeholder":"Username"})
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={"placeholder":"Password"})
    )
    # 验证码尝试
    # captcha = CaptchaField(label='code')
    # code = forms.CharField(
    #     label="code",
    #     widget=forms.TextInput(attrs={'placeholder':"Input code above"})
    # )

class signUpForm(forms.Form):
    username = forms.CharField(
        min_length=4, max_length=30,
        error_messages={
            'min_length': 'Username must be at least 4 characters',
            'max_length': 'Username cannot be longer than 30 characters',
            'required': 'Username is required',
        },
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Mobile phone'})
    )
    age = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Age'})
    )
    password = forms.CharField(min_length=8, max_length=30,
                                error_messages={
                                    'min_length': 'Password must be at least 8 characters',
                                    'max_length': 'Password cannot be longer than 30 characters',
                                    'required': 'Password is required',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_confirm = forms.CharField(max_length=30,
                                error_messages={
                                    'max_length': 'Password cannot be longer than 30 characters',
                                    'required': 'Password is required',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    # class Meta:
    #     model = models.UserInfo
    #     fields = ('name', 'password1', 'password2',)
    error_messages = {'password_mismatch': 'The two passwords do not match', }

