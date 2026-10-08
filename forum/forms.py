from django import forms 
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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
    # user authentication form
    username = forms.CharField(label="User name", 
                              max_length=40, 
                              widget=forms.TextInput(attrs={'class': 'form_control',}))
