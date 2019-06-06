from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from django.conf import settings
from . import models, forms

class OwnerDetail(CreateView):
    model = models.Owner


class OwnerCreate(CreateView):
    template_name = 'owner/create.html'
    form_class= forms.OwnerForm

    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save()
            inlines.instance = self.object
            inlines.save()
            return redirect(self.get_success_url())
        else:
            return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.POST:
            ctx['inlines'] = forms.AggregateInlineFormset(self.request.POST)
        else:
            ctx['inlines'] = forms.AggregateInlineFormset()
        return ctx
