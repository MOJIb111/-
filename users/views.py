from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserProfileForm, UserLoginForm, UserRegistrationForm
from django.contrib import auth,messages
from django.urls import reverse
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Лог - ин',
        'form' : form
    }
    return render(request, 'users/login.html', context)
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Реугистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    
    context = {
        'title' : 'Абоба - Профиль',
        'form': form
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))