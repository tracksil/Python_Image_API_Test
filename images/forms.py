from django.forms import ModelForm
from django import forms
from .models import Images


class UploadForm(ModelForm):
    title = forms.TextInput()
    album_id = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = Images
        fields = ['title', 'album_id', 'image']
