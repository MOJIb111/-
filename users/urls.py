from django.urls import path
from users.views import profile, login, registration, logout

app_name='users'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
]
