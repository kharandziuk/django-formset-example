from django import forms
from django.forms.models import inlineformset_factory
from django.conf import settings

from . import models

from extra_views import InlineFormSetFactory

class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owner
        fields = '__all__'


class AggregateInlineForm(forms.ModelForm):
    class Meta:
        model = models.Aggregate
        fields = '__all__'

class AggregateInlineFormset(InlineFormSetFactory):
    form_class = AggregateInlineForm
    model = models.Aggregate
    factory_kwargs=dict(extra=3, can_delete=False, can_order=False)
