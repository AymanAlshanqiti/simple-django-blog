from django import forms
from django.contrib.auth import authenticate
from account.models import Account


class UserLoginForm(forms.ModelForm):
    email = forms.CharField(required=True)
    password = forms.CharField(
        required=True, label='Password', widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")
