from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from tast.models import Quiz, Question, Answer, QuizAttempt, UserAnswer


def index(request):
    context = {'title' : 'Онлайн тесты c точным результатом от психологических до психологических'}
    return render(request, 'tast/index.html', context)

def testicals(request):
    context = {'title': 'Тест-ички'}
    return render(request, 'tast/testicals.html', context)
@login_required
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    attempt, created = QuizAttempt.objects.get_or_create(
        user = request.user,
        quiz=quiz,
        completed_at__isnull=True,
        defaults={'started_at':timezone.now()}
    )
    
    context = {'quiz' : quiz,
               'attempt': attempt}
    return render(request, 'tast/quiz.html', context)
@login_required
def submit_answer(request, attempt_id):
    attempt = get_object_or_404(QuizAttempt, pk=attempt_id, user=request.user)
    
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        answer_id = request.POST.get('answer_id')
        
        if question_id and answer_id:
            question = get_object_or_404(Question, pk=question_id)
            answer = get_object_or_404(Answer, pk=answer_id, question=question)
            
            UserAnswer.objects.update_or_create(
                attempt=attempt,
                question=question,
                defaults={
                    'selected_answer': answer,
                    'answered_at': timezone.now()
                }
            )
            return redirect('next_question', attemp_id=attempt.id)
        
    return redirect('quiz_detail', quiz_id=attempt.quiz.id)

@login_required
def complete_quiz(request, attempt_id):
    attempt = get_object_or_404(QuizAttempt, pk=attempt_id, user=request.user)
    attempt.completed_at = timezone.now()
    attempt.save()
    
    context = {
        'attempt': attempt,
        'user_answers': attempt.user_answers.select_related('question', 'selected_answer')
    }
    return render(request, 'tast/results.html', context)

@login_required
def quiz_results(request, attempt_id):
    attempt = get_object_or_404(
        QuizAttempt,
        pk=attempt_id,
        user=request.user
    )
    
    correct_answers_count = sum(
        1 for answer in attempt.user_answers.all()
        if answer.selected_answer.is_correct
    )
    context = {
        'attempt': attempt,
        'user_answers': attempt.user_answers.select_related(
            'question',
            'selected_answer'
        ),
        'correct_answers_count': correct_answers_count
    }
    return render(request, 'tast/results.html', context)

def quiz_list(request):
    quizzes = Quiz.objects.all()

    context = {
        'quizzes': quizzes
    }
    return render(request,'tast/testicals.html', context)

