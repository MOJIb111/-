from django import forms
from django.contrib.auth.forms import UserChangeForm
from users.models import User

class UserProfileForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'profile__form__label'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'col-md-12', 'readonly' : True}))
    image = forms.FileField(widget=forms.FileInput(
        attrs={'class' : 'profile__general-info__photo'}))
    gender = forms.ChoiceField(choices=('М', 'Ж'))
    date = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': ''}))
    
    
    class Meta:
        model = User
        fields = ('name', 'email', 'image', 'gender', 'date')