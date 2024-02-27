from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import NoteForm, CategoryForm
from .models import Note, Category
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "memora/index.html")


def notes(request):
    notes = Note.objects.all()
    context = {"notes": notes}
    return render(request, "memora/list.html", context)


def categorys(request):
    category = Category.objects.all()
    context = {"categorys": category}
    return render(request, "memora/list_category.html", context)


def delete(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("La nota no existe")
    if request.user == note.user:
        note.delete()
    else:
        raise PermissionDenied()
    return redirect(reverse("memora:notes"))


def detail(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("La nota no existe")
    context = {"note": note.note, "category": note.category.name}
    return render(request, "memora/detail.html", context)


@login_required
def create_note(request):
    if request.POST:
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data["note"]
            category = form.cleaned_data["category"]
            Note.objects.create(
                note=note, user=request.user, category=category, pub_date=timezone.now()
            )
            return redirect(reverse("memora:notes"))
    else:
        form = NoteForm()

    return render(request, "memora/note_form.html", {"form": form})


def edit_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("La nota no existe")
    if request.POST:
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse("memora:notes"))
    else:
        form = NoteForm(instance=note)

    return render(request, "memora/note_form.html", {"form": form})


def create_category(request):
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data["name"]
            Category.objects.create(name=category)
            return redirect(reverse("memora:categorys"))
    else:
        form = CategoryForm()

    return render(request, "memora/category_form.html", {"form": form})
