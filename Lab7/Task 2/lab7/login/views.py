from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4> Empty project</h4>")


def about(request):
    return HttpResponse("<h1>About page</h1>")