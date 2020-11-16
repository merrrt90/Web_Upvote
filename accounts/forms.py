from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input email-input', 'type': 'text', 'name': 'email', 'placeholder': 'Email'}),
        label="Email")
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input email-input', 'type': 'text', 'name': 'username', 'placeholder': 'Enter Username'}),
        label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input password-input', 'type': 'password', 'name': 'password1', 'placeholder': 'Enter Your Password'}),
        label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input password-input', 'type': 'password', 'name': 'password2', 'placeholder': 'Email', 'placeholder': 'Re-Enter Your Password'}),
        label="Password (again)")

    '''added attributes so as to customise for styling, like bootstrap'''
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        field_order = ['email', 'username', 'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match
        NOTE : errors here will appear in 'non_field_errors()'
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    "Passwords don't match. Please try again!")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

# The save(commit=False) tells Django to save the new record, but dont commit it to the database yet


class AuthenticationForm(forms.Form):  # Note: forms.Form NOT forms.ModelForm
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input email-input', 'type': 'text', 'name': 'email', 'placeholder': 'Email'}),
        label='Email')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input password-input', 'type': 'password', 'name': 'password', 'placeholder': '●●●●●●●'}),
        label='Password')

    class Meta:
        fields = ['email', 'password']


"""from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Valid E-mail Adrress Required.')

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', )


class LoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password')"""
