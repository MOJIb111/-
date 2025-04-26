from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tast.models import Quiz, Question
from users.models import UserAnswer
from tast.forms import AnswerForm

def index(request):
    context = {'title' : 'Онлайн тесты c точным результатом от психологических до психологических'}
    return render(request, 'tast/index.html', context)

def testicals(request):
    context = {'title': 'Тест-ички'}
    return render(request, 'tast/testicals.html', context)

def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    request.session['quiz_id'] = quiz_id
    request.session['question_ids'] = list(quiz.questions.values_list('id', flat=True))
    request.session['current_question_index'] = 0
    return redirect('answer_question')

def answer_question(request):
    question_id = request.session['question_ids'][request.session['current_question_index']]
    question = Question.objects.get(id=question_id)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST, question=question)
        if form.is_valid():
            selected_answer = form.cleaned_data['answer']
            UserAnswer.objects.create(
                user = request.user,
                question = question,
                answer = selected_answer,
                is_correct = selected_answer.is_correct
            )
            
            request.session['current_question_index'] += 1
            if request.session['current_question_index'] >= len(request.session['question_ids']):
                return redirect('quiz_results')
            return redirect('answer_question')
        
    else:
        form = AnswerForm(question=question)
        context = {'title' : 'Атвичай',
                   'question' : question,
                   'form' : form,
                   'progress' : f'{request.session["current_question_index"] + 1}/{len(render.session["question_ids"])}'
                   }
    return render(request, 'tast/answer_question', context)
    

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, )
def quiz_results(request):
    context = {'title': 'Ризультаты'}
    return render(request,'tast/quiz_results.html', context)