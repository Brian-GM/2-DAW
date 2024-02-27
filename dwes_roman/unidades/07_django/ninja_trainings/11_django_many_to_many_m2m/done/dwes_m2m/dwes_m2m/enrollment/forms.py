from django import forms

from .models import Subject, Student


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "description"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surname", "age"]
