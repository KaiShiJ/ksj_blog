#*--coding:utf-8--*
from django.contrib.auth.forms import User
from django import forms

class RegisterForm(forms.Form):
    username =forms.CharField(
        label=u'昵称',
        help_text=u'昵称可用于登录，不能包含空格和@字符。',
        max_length=20,
        initial='',
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    email=forms.EmailField(
        label=u'邮箱',
        help_text=u'邮箱可用于登录，不能包含空格和@字符',
        max_length=20,
        initial='',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password=forms.EmailField(
        label=u'密码',
        help_text=u'密码长度6~18位',
        min_length=6,
        max_length=18,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )