from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# creating a form
class SignupForm(UserCreationForm):
    full_name=forms.CharField(max_length=50,required=True)
    mobile=forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    email=forms.EmailField(max_length=50,required=True)

    class Meta:
        model = User
        fields = ['full_name','mobile','email','username','password1','password2']


