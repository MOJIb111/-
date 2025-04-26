from django.db import models
from django.contrib.auth.models import AbstractUser
from tast.models import Quiz, Question, Answer
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.ForeignKey)
    is_correct = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.is_correct = self.answer.is_correct
        super.save(*args, **kwargs)

class UserPassedTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)