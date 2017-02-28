from django import forms

class MeuFrom(forms.Form):
    email = forms.CharField(label='email', max_length=20)
    senha = forms.CharField(label='senha', max_length=20)
    quanti = forms.IntegerField(label='quanti')