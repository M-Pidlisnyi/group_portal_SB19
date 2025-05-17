from django import forms
from forms.models import Message
class Message(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        exclude = ['user']