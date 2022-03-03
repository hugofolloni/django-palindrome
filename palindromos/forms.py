from django import forms
from .models import Palindromo

class PalindromoForm(forms.ModelForm):
    palindromo = forms.CharField(label='Palindromo', max_length=255)
    class Meta:
        model = Palindromo
        fields = ['palindromo']