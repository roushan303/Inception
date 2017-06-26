from django import forms
from polls.models import Question,Choice

class Question_Name(forms.Form):
    question_text = forms.CharField(max_length=100)
    pub_date = forms.DateTimeField()


class Choice_Name(forms.Form):
    choice_text = forms.CharField(max_length=200)
