from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    email = forms.EmailField(help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class OrderInsuranceForm(forms.Form):
    object_name = forms.CharField(max_length=100)
    contract_date = forms.DateTimeField(widget=DateTimePickerInput)
    insurance_payment = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contracts
        fields = ('contract_date', 'insurance_payment')


class ChangePersonalDataForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    email = forms.EmailField(help_text='Required. Inform a valid email address.')
    passport = forms.CharField(max_length=10)

    class Meta:
        model = Clients
        fields = ('first_name', 'last_name', 'email', 'passport')
