from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Обязательное поле')
    password1 = forms.CharField(required=True, help_text='Введите пароль')
    password2 = forms.CharField(required=True, help_text='Повторите пароль')


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form_control','placeholder':'Введите свой email'}),
            'password1':forms.PasswordInput(attrs={'class':'form_control','placeholder':'Введите пароль'}),
            'password2':forms.PasswordInput(attrs={'class':'form_control','placeholder':'Повторите пароль'})
        }
        
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Данный email зарегестрирован.')
        return email
    
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).exists():
            raise ValidationError('Такой пользователь уже существует.')
        return username
    
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают.')
        return password2
    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите имя пользователя.'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Введите пароль'}))
    
    
class LogoutForm(forms.Form):
    pass