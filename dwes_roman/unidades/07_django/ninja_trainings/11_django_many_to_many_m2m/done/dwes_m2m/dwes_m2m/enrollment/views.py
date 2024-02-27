from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Subject
from .forms import SubjectForm, StudentForm


def index(request):
    return render(request, "enrollment/index.html")


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, "enrollment/subject_list.html", {"subjects": subjects})


def subject_detail(request, id):
    subject = get_object_or_404(Subject, id=id)
    return render(request, "enrollment/subject_detail.html", {"subject": subject})


def subject_create(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("enrollment:subject_list"))
    else:
        form = SubjectForm()

    return render(
        request,
        "enrollment/form.html",
        {"form": form, "header": "Añadir Materia"}
    )


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("enrollment:subject_list"))
    else:
        form = StudentForm()

    return render(
        request,
        "enrollment/form.html",
        {"form": form, "header": "Añadir Alumnado"}
    )
