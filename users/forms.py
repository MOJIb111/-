from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UserCreationForm
from users.models import User

GENDER_CHOICES = (
    ('M', 'Мужской'),
    ('Ж', 'Женский')
)

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=
    {'class': 'form-control py-4', 'placeholder' : 'Введите имя пользователя' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs=
    {'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'profile__form__label'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'col-md-12', 'readonly' : True}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class' : 'custom-file'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(), choices=GENDER_CHOICES)
    date = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1940, 2080),
        empty_label=('Год', 'Месяц', 'День')),
        required=True)
    
    
    class Meta:
        model = User
        fields = ('name', 'email', 'image', 'gender', 'date')