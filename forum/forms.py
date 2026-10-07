from django import forms 
from .models import Post


class PostAddForm(forms.ModelForm):
    # Form to add a new article by user
    class Meta:
        model = Post 
        fields = ['title', 'content', 'photo', 'category']