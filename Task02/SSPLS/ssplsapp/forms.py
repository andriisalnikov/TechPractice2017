from django import forms
# Модель формы обратной связи
class ContactForm(forms.Form):
    CHOICES=[('stone','stone'),
         ('scissors','scissors'),
         ('paper','paper'),
         ('lizard','lizard'),
         ('spock','spock')]
    bet = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())