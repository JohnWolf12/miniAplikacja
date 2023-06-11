from django import forms
from django.core.exceptions import ValidationError

from aplikacjaogloszeniowa.models import Kategoria, Ogloszenie


def check_positive_number(value):
    if value < 0:
        raise ValidationError('Cena musi być liczbą dodatnią')


class AnnouncementForm(forms.ModelForm):
    nazwa = forms.CharField(label='Nazwa', max_length=100, widget=forms.TextInput(
        attrs={
            'autocomplete': 'off',
            'class': 'form-control bg-light',
        }
    ))
    cena = forms.DecimalField(validators=[check_positive_number], label='Cena', max_digits=9, decimal_places=2,
                              widget=forms.NumberInput(
                                  attrs={
                                      'autocomplete': 'off',
                                      'class': 'form-control bg-light'
                                  }
                              ))
    kategoria = forms.ModelChoiceField(label='Kategoria', queryset=Kategoria.objects.all(),
                                       empty_label='Wybierz kategorię', widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        ))
    opis = forms.CharField(label='Opis', max_length=1000, required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control bg-light'
        }
    ))

    class Meta:
        model = Ogloszenie
        fields = ['nazwa', 'cena', 'kategoria', 'opis']
