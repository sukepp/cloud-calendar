from django.forms import ModelForm, TextInput
from datetime import date, time, datetime
from .models import Record


class RecordForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Record
        fields = ['date', 'time_start', 'time_end', 'title', 'description']
        widgets = {
            'date': TextInput(attrs={
                'id': 'datepicker1',
                'value': date.today().strftime('%Y-%m-%d')
            }),
        }


class UserForm(ModelForm):
    class Meta:
        model = Record
        fields = ['user']
