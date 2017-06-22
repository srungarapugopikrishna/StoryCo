from django import forms

from .models import Story

class MainForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'text')

class SomeForm(forms.Form):
    CHOICES = ((1,1),
               (2,2),
               (3,3),
               (4,4),)
    
    like = forms.MultipleChoiceField(choices=CHOICES, widget=forms.RadioSelect())
