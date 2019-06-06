from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView

from django.conf import settings
from . import models

class OwnerCreate(CreateView):
    template_name = 'owner/create.html'
    model = models.Owner
    fields = ['name']

