from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    create comment form
    '''
    class Meta:
        model = Comment
        exclude = ['user','image']