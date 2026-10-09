from django import forms 
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class PostAddForm(forms.ModelForm):
    # Form to add a new article by user
    class Meta:
        model = Post 
        fields = ('title', 'content', 'photo', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),


        }

class LoginForm(AuthenticationForm):
    # User authentication form
    username = forms.CharField(label="User name", 
                              max_length=40, 
                              widget=forms.TextInput(attrs={'class': 'form-control',}))
    password = forms.CharField(label="Password", 
                              max_length=40, 
                              widget=forms.PasswordInput(attrs={'class': 'form-control',}))

class RegistrationForm(UserCreationForm):
    # User registration


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(max_length=40, 
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'User name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Confirm password'}))