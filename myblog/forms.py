from django import forms

from .models import Story

class MainForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'text', 'genre_id')
