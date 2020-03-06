from django import forms
from mptt.forms import TreeNodeChoiceField

from .models import File_or_Folder


class add_form(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    category = TreeNodeChoiceField(queryset=File_or_Folder.objects.all())

class create_form(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class signup_form(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())