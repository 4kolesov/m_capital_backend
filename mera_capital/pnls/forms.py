from django import forms


class DateForm(forms.Form):
    start_date = forms.DateTimeField(
        initial='введите дату и время', widget=forms.DateTimeInput)
    finish_date = forms.DateTimeField(
        initial='введите дату и время', widget=forms.DateTimeInput)
