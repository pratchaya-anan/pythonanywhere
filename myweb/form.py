from django.forms import ModelForm
from django import forms

from .models import Comment

class addComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['CommentName','Comment']
