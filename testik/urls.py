"""
URL configuration for testik project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tast.views import index, testicals, start_quiz, answer_question, quiz_results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('testicals/', include('tast.urls', namespace='tast')),
    path('start_quiz/', include('tast.urls', namespace='start_quiz')),
    path('answer_question/', include('tast.urls', namespace='answer_question')),
    path('quiz_results/', include('tast.urls', namespace='quiz_results')),
    path('users/', include('users.urls', namespace='users'))
]
