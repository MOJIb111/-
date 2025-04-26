from django.urls import path
from tast.views import testicals, start_quiz, answer_question, quiz_results

app_name='tast'

urlpatterns=[
    path('testicals/', testicals, name='testicals'),
    path('start_quiz/', start_quiz, name='start_quiz'),
    path('answer_question/', answer_question, name='answer_question'),
    path('quiz_results/', quiz_results, name='quiz_results'),
]