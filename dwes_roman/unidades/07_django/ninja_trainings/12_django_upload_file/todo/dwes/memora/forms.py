from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["note", "category", "image"]


class UploadImageForm(forms.Form):
    name = forms.CharField(max_length=50)
    image = forms.FileField()
