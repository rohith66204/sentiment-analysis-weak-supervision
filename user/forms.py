from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Orders,Ratings
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django.forms.widgets import PasswordInput, TextInput,DateInput,EmailInput

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'userna','placeholder': 'User Name'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'passwo','placeholder':'Password'}))

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=TextInput(attrs={'class':'userna common','placeholder': 'First Name'}))
    last_name = forms.CharField(widget=TextInput(attrs={'class':'userna common','placeholder': 'Last Name'}))
    username = forms.CharField(widget=TextInput(attrs={'class':'userna common','placeholder': 'User Name'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'passwo common','placeholder':'Password'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'passwo common','placeholder':'Confirm Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'passwod common','placeholder':'Confirm Password'}))
    email = forms.CharField(widget=EmailInput(attrs={'class':'email common','placeholder':'Email'}))
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD',widget=DateInput(attrs={'class':'bod common','placeholder':'Date Of Birth (YYYY-MM-DD)'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'birth_date', 'password', 'password1', 'password2', 'email')
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('prodqty','location')
        
class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ('ratings','reviews')