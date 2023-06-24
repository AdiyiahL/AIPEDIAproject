from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from content import models

class NewContentForm(forms.Form):
    title = forms.CharField(
        min_length=1, max_length=1000,
        error_messages={
            'min_length': '',
            'max_length': 'no more than 20 characters',
            'required': 'required',
        },
        widget=forms.TextInput(attrs={"placeholder":"please input the title","class":"form-control", "id":"exampleInputEmail1", "name":"title"})
    )
    what_area = forms.CharField(
        min_length=10, max_length=3000,
        error_messages={
            'min_length': '',
            'max_length': 'cannot be longer than 3000 characters',
            'required': ' required',
        },
        widget=forms.Textarea(attrs={"placeholder":"please input what it is","class":"form-control", "id":"exampleInputEmail1", "name":"what_area"})
    )
    how_area = forms.CharField(
        min_length=10, max_length=3000,
        error_messages={
            'min_length': '',
            'max_length': 'cannot be longer than 3000 characters',
            'required': 'required',
        },
        widget=forms.Textarea(attrs={"placeholder": "please input how to use it","class":"form-control", "id":"exampleInputEmail1", "name":"how_area"})
    )
    example = forms.CharField(
        min_length=10, max_length=3000,
        error_messages={
            'min_length': '',
            'max_length': 'cannot be longer than 3000 characters',
            'required': 'required',
        },
        widget=forms.Textarea(attrs={"placeholder": "please input how to use it","class":"form-control", "id":"exampleInputEmail1", "name":"example_area"})
    )
    source = forms.CharField(
        min_length=10, max_length=2000,
        error_messages={
            'min_length': '',
            'max_length': 'cannot be longer than 2000 characters',
            'required': 'required',
        },
        widget=forms.Textarea(attrs={"placeholder": "please input how to use it","class":"form-control", "id":"exampleInputEmail1", "name":"source_area"})
    )
    try_area = forms.CharField(
        min_length=10, max_length=3000,
        error_messages={
            'min_length': '',
            'max_length': 'cannot be longer than 1000 characters',
            'required': 'required',
        },
        widget=forms.Textarea(attrs={"placeholder": "please input something","class":"form-control", "id":"exampleInputEmail1", "name":"try_area"})
    )
