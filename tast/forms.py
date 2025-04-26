from django import forms
from tast.models import Question

class AnswerForm(forms.Form):
   def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super.__init__(*args, **kwargs)
        
        
        self.fields['answer'] = forms.ModelChoiceField(
            queryset= question.answers.all(),
            widget= forms.RadioSelect(),
            label=question.text,
            required=True
        )