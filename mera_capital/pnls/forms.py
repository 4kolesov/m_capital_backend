from django import forms

from .models import Calculation


class DateForm(forms.Form):
    # date = forms.DateTimeField(widget=forms.SelectDateWidget)
    start_date = forms.DateTimeField(widget=forms.SelectDateWidget)
    finish_date = forms.DateTimeField(widget=forms.SelectDateWidget)
    # date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
