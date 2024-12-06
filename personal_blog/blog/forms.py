from django import forms
from .models import User, Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title', 'content', 'content_img','category','author']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment


        fields = ['content']
        
       
        
