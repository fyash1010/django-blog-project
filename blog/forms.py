from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import BlogPost

# Custom user creation form for the User model
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

# Form for creating and editing blog posts
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
        }
