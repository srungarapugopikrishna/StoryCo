from django import forms

from .models import Story,Item

class MainForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'text', 'genre_id')

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_title', 'item_description')
