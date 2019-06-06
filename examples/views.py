from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from extra_views import CreateWithInlinesView, InlineFormSetFactory

from django.conf import settings
from . import models, forms

class OwnerDetail(CreateView):
    model = models.Owner


class OwnerCreate(CreateWithInlinesView):
    template_name = 'owner/create.html'
    model = models.Owner
    fields = '__all__'
    inlines = [forms.AggregateInlineFormset]

