from django.urls import path

from . import views

app_name = "memora"

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("notes/<int:note_id>/", views.detail, name="detail"),
    path("notes/create/", views.create_note, name="create_note"),
    path("category/create/", views.create_category, name="create_category"),
    path("categorys/", views.categorys, name="categorys"),
    path("note/delete/<int:note_id>/", views.delete, name="delete"),
    path("note/edit/<int:note_id>/", views.edit_note, name="edit"),
]
