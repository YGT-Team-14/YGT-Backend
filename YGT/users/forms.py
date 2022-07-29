
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


def student_id_validator(value):
    if len(str(value)) != 8:
        raise forms.ValidationError('본인의 학번을 입력해주세요.')

class CsRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CsRegisterForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].label = '아이디'
        self.fields['user_id'].widget.attrs.update({     
            'class': 'form-control',
            'autofocus': False
        })
        self.fields['password'].label = '비밀번호'
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = User
        fields = [ 'user_id', 'school', 'password', 'student_id', 'major']
