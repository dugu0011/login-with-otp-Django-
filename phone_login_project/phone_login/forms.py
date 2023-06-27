from django import forms
from phonenumber_field.formfields import PhoneNumberField


class LoginForm(forms.Form):
    phone_number = PhoneNumberField()
    # otp = forms.CharField(max_length=6)
