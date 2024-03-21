from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'form-control',
        'placeholder': 'Username *',
        'id': 'search-input01'
       }
    )
    
    
    self.fields['password'].widget.attrs.update(
      {'class': 'form-control', 'placeholder': 'Password *', 'id': 'search-input01'}
    )


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username *',
            'name': 'usernameeee'
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'first_name',
            'placeholder': 'First Name *',
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'last_name',
            'placeholder': 'Last Name *',
        }
    ))
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'name': 'password',
            'minlength': "8",
            'placeholder': 'Password *',
        }
    ))

    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'name': 'password',
            'minlength': "8",
            'placeholder': 'Confirm Password *',
        }
    ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont match')

