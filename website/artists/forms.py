import re

from django import forms
from .models import SubscribeForm

class SubscriberForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = SubscribeForm
        fields = ["email", "phone", "receive_adv"]
