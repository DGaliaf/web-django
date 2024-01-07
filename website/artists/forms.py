import re

from django import forms
from .models import SubscribeForm

class SubscriberForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = SubscribeForm
        fields = ["email", "phone", "receive_adv"]

    def clean(self):
        if re.findall(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", self.cleaned_data["phone"]):
            raise forms.ValidationError('Неверный номер телефона')

        return self.cleaned_data
