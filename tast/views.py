from django.shortcuts import render

def index(request):
    context = {'title' : 'Тест личности'}
    return render(request, 'tast/index.html', context)

