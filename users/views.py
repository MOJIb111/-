from django.shortcuts import render
from users.forms import UserProfileForm


def profile(request):
    
    context = {
        'title' : 'Абоба - Профиль',
    }
    return render(request, 'users/profile.html', context)
