# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 下午9:06
# @Author  : hai
# @FileName: forms
# @Software: 
# @github    ：https://github.com/mo-hai/

from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
