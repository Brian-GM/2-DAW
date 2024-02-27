from django.shortcuts import render
from django import HTTPResponse


def index(request):
    return HTTPResponse("Hola mundo")