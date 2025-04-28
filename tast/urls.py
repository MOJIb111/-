from django.urls import path
from tast.views import index, testicals, start_quiz, submit_answer, complete_quiz, quiz_results, quiz_list

app_name='tast'

urlpatterns = [
    path('', index, name='index'),
    path('testicals/', testicals, name='testicals'),
    path('quizzes/', quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/start/', start_quiz, name='start_quiz'),
    path('attempt/<int:attempt_id>/submit/', submit_answer, name='submit_answer'),
    path('attempt/<int:attempt_id>/complete/', complete_quiz, name='complete_quiz'),
    path('results/<int:attempt_id>/', quiz_results, name='quiz_results'),
]