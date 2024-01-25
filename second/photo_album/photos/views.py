from django.shortcuts import render
from .models import Photos


def index(request):
    projects = Photos.objects.all()
    return render(request, 'photos/index.html', {'projects': projects})


