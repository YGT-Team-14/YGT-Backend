from django import forms
from .models import Mento_Post, Friend_Post

class Mento_PostModelForm(forms.ModelForm):
    class Meta:
            model = Mento_Post
            fields=['title', 'post']

class Friend_PostModelForm(forms.ModelForm):
    class Meta:
            model = Friend_Post
            fields=['title', 'post']