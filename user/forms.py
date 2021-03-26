from django import forms
from django.core.exceptions import ValidationError
from user import models

class LoginForm(forms.ModelForm):
    username = forms.CharField(
        label='用户',
        required=True,
        min_length=4,
        max_length=12,
        error_messages={'min_length': '最小长度4位', 'max_length': '最大长度12位'},
    )
    password = forms.CharField(
        label='密码',
        required=True,
        min_length=6,
        max_length=12,
        error_messages={'min_length': '最小长度6位', 'max_length': '最大长度12位'},
        widget=forms.PasswordInput()
    )

    class Meta:
        model = models.UserInfo
        fields = '__all__'


class RegisterForm(forms.Form):

    username = forms.CharField(
        label='用户',
        required=True,
        min_length=4,
        max_length=12,
        error_messages={'min_length': '最小长度4位', 'max_length': '最大长度12位'},
    )

    email = forms.EmailField(
        label= '邮箱',
        required=True,
        widget=forms.EmailInput()
    )

    password1= forms.CharField(
        label='密码',
        required=True,
        min_length=6,
        max_length=12,
        error_messages={'min_length': '最小长度6位', 'max_length': '最大长度12位'},
        widget=forms.PasswordInput()
    )

    password2= forms.CharField(
        label='确认密码',
        required=True,
        min_length=6,
        max_length=12,
        error_messages={'min_length': '最小长度6位', 'max_length': '最大长度12位'},
        widget=forms.PasswordInput()
    )

    def clean(self):
        pwd1=self.cleaned_data.get('password1')
        pwd2=self.cleaned_data.get('password2')

        if pwd1 == pwd2:
            return self.cleaned_data
        self.add_error('password2',ValidationError('密码不一致！'))
        return self.cleaned_data



