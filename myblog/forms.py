from django import forms

from .models import Story,Item,Episode

class MainForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'text', 'genre_id')

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_title','item_type', 'item_description')

class EpisodeForm(forms.ModelForm):

    class Meta:
        model = Episode
        fields = ('episode_description','episode_type','episode_content_type','episode_content','episode_content_relative_url','categories')
