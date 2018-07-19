from django import forms
from django.contrib.auth import get_user_model
from authtools.forms import UserCreationForm


class SignupForm(UserCreationForm):
    agreed_to_terms = forms.BooleanField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'agreed_to_terms')
