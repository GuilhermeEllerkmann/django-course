from django import forms
from utils.django_forms import add_placeholder


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Type your Username')
        add_placeholder(self.fields['password'], 'Type your Password')

    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
