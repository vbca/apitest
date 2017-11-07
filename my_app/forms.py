from django import forms
from django.forms import ModelForm
from . import validators, models

GENERO_CHOICES = (
    ('m', 'Mujer'),
    ('h', 'Hombre')
)
DATE_CHOICES = ('1980', '1981', '1982')


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, widget=
                            forms.TextInput(attrs={'style':'color:green;'}))
    email = forms.EmailField(label='Mail', max_length=255)
    gender = forms.CharField(label='Genero', widget=forms.Select(
                                                choices=GENERO_CHOICES)
                                                )
    birthday = forms.DateField(label='Birthday', widget=forms.SelectDateWidget(
                                                years= DATE_CHOICES
                                                ))
    age = forms.IntegerField(label='Edad', required=False, help_text='+18', validators=[
                                                            validators.age_validation
                                                            ])

    send_mail = forms.BooleanField(label='Te mandamos email?')

class PersonModelForm(ModelForm):
    class Meta:
        model = models.Person
        fields = '__all__'

#formset
'''class DetailEventForm(forms.Form):
    event = forms.CharField(widget=forms.Select(
                                choices=tuple((x.id,x.name) for x in models.Event.objects.all()))
                            )'''

'''class PersonForm(forms.Form):
        name = forms.CharField(
                                        max_length=30,
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'Name',
                                        }))
        email = forms.CharField(
                                        max_length=30,
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'email',
                                        }))
        age = forms.IntegerField(
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'age',
                                        }))
        program = forms.CharField(
                                        widget=forms.Select(
                                            choices=tuple((x.id, x.name) for x in models.Program.objects.all())
                                        ))'''

from django.forms.formsets import BaseFormSet

class BaseFormSet(BaseFormSet):

    def clean(self):
        if any(self.errors):
            return

        events = []

        for form in self.forms:
            if form.cleaned_data:
                event = form.cleaned_data["event"]
                if event:
                    events.append(event)

class SearchForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={
                                            'placeholder': 'search',
                                        }))