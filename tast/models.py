from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название теста')
    description = models.TextField(verbose_name='Описание теста', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
    related_name='questions', verbose_name='Тест')
    text = models.TextField(verbose_name='Текст вопроса')
    
    def __str__(self):
        return f'Вопрос:  {self.quiz[:50]}...'
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
    related_name='answers', verbose_name='Вопрос')
    text = models.CharField(max_length=200, verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный ответ')
    
    def __str__(self):
        return f'Ответ {self.text[:20]}...'
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        
