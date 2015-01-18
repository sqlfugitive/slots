from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms import layout


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    animal = forms.CharField(max_length=100)
    
    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(layout.Submit('submit', 'Submit'))
