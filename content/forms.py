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

    classification = forms.ChoiceField(
        choices=[(1,"Calculus"),(2,"Linear Algebra"),(3,"Probability and Statistics"),
                 (4,"Programming Fundamentals"),(5,"Data Structures and Algorithms"),(6,"Computer Organization and Architecture"),
                 (7,"Fundamentals of Machine Learning"),(8,"Deep Learning and Neural Networks"),(9,"Natural Language Processing")
                 ,(10,"Computer Vision"),(11,"Reinforcement Learning"),(12,"Data Preprocessing and Cleaning"),
                 (13,"Feature Engineering"),(14,"Data Visualization"),(15,"Data Mining and Analysis"),(16,"Autonomous Driving and Unmanned Systems")
                 ,(17,"Robotics"),(18,"Medical Image Analysis"),(19,"Financial Data Analysis and Prediction"),(20,"Intelligent Recommendation Systems"),
                 (21,"AI Ethics"),(22,"Data Privacy and Security")
                 ,(23,"Law and Artificial Intelligence"),(24,"machine learning frameworks"),(25,"Real-world Application Case Studies"),(26,"Team Collaboration and Project Management")]
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
    try_area = forms.CharField(
        min_length=10, max_length=3000,
        error_messages={
            'min_length': '',
            'max_length': 'cannot be longer than 1000 characters',
            'required': 'required',
        },
        widget=forms.Textarea(
            attrs={"placeholder": "please input something", "class": "form-control", "id": "exampleInputEmail1",
                   "name": "try_area"})
    )


class NewCoursesForm(forms.Form):
    title = forms.CharField(
        min_length=1, max_length=200,
        error_messages={
            'min_length': '',
            'max_length': 'no more than 20 characters',
            'required': 'required',
        },
        widget=forms.TextInput(attrs={"placeholder":"please input the title","class":"form-control", "id":"exampleInputEmail1", "name":"title"})
    )

    # level1 = forms.CharField(
    #
    # #     choices=[(1,"Calculus"),(2,"Linear Algebra"),(3,"Probability and Statistics"),
    # #              (4,"Programming Fundamentals"),(5,"Data Structures and Algorithms"),(6,"Computer Organization and Architecture"),
    # #              (7,"Fundamentals of Machine Learning"),(8,"Deep Learning and Neural Networks"),(9,"Natural Language Processing")
    # #              ,(10,"Computer Vision"),(11,"Reinforcement Learning"),(12,"Data Preprocessing and Cleaning"),
    # #              (13,"Feature Engineering"),(14,"Data Visualization"),(15,"Data Mining and Analysis"),(16,"Autonomous Driving and Unmanned Systems")
    # #              ,(17,"Robotics"),(18,"Medical Image Analysis"),(19,"Financial Data Analysis and Prediction"),(20,"Intelligent Recommendation Systems"),
    # #              (21,"AI Ethics"),(22,"Data Privacy and Security")
    # #              ,(23,"Law and Artificial Intelligence"),(24,"machine learning frameworks"),(25,"Real-world Application Case Studies"),(26,"Team Collaboration and Project Management")]
    # )
    #
    # level2 = forms.CharField(
    # )
    contents = forms.CharField(
        min_length=10, max_length=3000,
        error_messages={
            'min_length': '',
            'max_length': 'cannot be longer than 3000 characters',
            'required': ' required',
        },
        widget=forms.Textarea(attrs={"placeholder":"please input what it is","class":"form-control", "id":"exampleInputEmail1", "name":"what_area"})
    )

    contents1 = forms.CharField(
        min_length=10, max_length=3000,
        error_messages={
            'min_length': '',
            'max_length': 'cannot be longer than 3000 characters',
            'required': ' required',
        },
        widget=forms.Textarea(
            attrs={"placeholder": "please input what it is", "class": "form-control", "id": "exampleInputEmail1",
                   "name": "what_area"})
    )

    source = forms.CharField(
        min_length=10, max_length=300,
        error_messages={
            'min_length': '',
            'max_length': 'cannot be longer than 2000 characters',
            'required': 'required',
        },
        widget=forms.Textarea(attrs={"placeholder": "please input how to use it","class":"form-control", "id":"exampleInputEmail1", "name":"source_area"})
    )