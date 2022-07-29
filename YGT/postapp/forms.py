from django import forms
from .models import Mento_Post, Friend_Post,Mento_Comment,Profile

class Mento_PostModelForm(forms.ModelForm):
    class Meta:
            model = Mento_Post
            fields=['title', 'post']

class Friend_PostModelForm(forms.ModelForm):
    class Meta:
            model = Friend_Post
            fields=['title', 'post']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Mento_Comment
        fields =["comment"]
        #field =["title","body"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =["user"]
        #field =["title","body"] 