from django import forms
from django.forms.models import inlineformset_factory
from django.conf import settings

from . import models

class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owner
        fields = '__all__'


class AggregateInlineForm(forms.ModelForm):
    class Meta:
        model = models.Aggregate
        fields = '__all__'


AggregateInlineFormset = inlineformset_factory(
    models.Owner,
    models.Aggregate,
    form=AggregateInlineForm,
    extra=3,
    can_delete=False,
    can_order=False
)
