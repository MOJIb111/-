from django.db import models
from users.models import User


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    
    def __str__(self):
        return f'Вопрос: {self.text[:50]}...'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    image = models.ImageField(upload_to='answers/', blank=True)
    points = models.PositiveIntegerField(default=1)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Ответ ({self.points} баллов)'


class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    total_points = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-started_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.total_points} баллов)"


class UserAnswer(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)
    earned_points = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ('attempt', 'question')
    
    def save(self, *args, **kwargs):
        self.earned_points = self.selected_answer.points
        super().save(*args, **kwargs)
        self.attempt.save()
    def __str__(self):
        return f"{self.attempt.user.username}: {self.question.text[:30]}..."