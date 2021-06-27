from django import forms
from django.forms import fields, models
from blog.models import BlogPost

class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image'] 
