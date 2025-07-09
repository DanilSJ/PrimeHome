from django import forms
from .models import SupportQuestions

class SupportQuestionsForm(forms.ModelForm):
    class Meta:
        model = SupportQuestions
        fields = ['name', 'email', 'phone', 'theme', 'description'] 