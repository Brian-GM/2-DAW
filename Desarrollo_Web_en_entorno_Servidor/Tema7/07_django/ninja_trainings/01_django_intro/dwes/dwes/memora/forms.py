from django import forms

from .models import Note, Category


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["note", "category"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
