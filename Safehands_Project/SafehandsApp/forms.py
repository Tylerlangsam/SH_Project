from django import forms
from .models import Babysitter

class ChildForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    age = forms.CharField(max_length=25, required=True)
    choices = []
    for babysitter in Babysitter.objects.all():
        choices.append((babysitter.babysitter_id, babysitter.name + ", " + babysitter.gender + ", " + babysitter.age ))
    babysitters = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices, required=False)