from django import forms
from forms.models import Mark
class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = "__all__"
        exclude = ['user']