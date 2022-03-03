from django.shortcuts import render, redirect
from .models import Palindromo
from .forms import PalindromoForm

# Create your views here.

def show_palindromos(request):
    palindromos = Palindromo.objects.all()
    return render(request, 'palindromos.html', {'palindromos': palindromos})

def create_palindromos(request):
    form = PalindromoForm(request.POST or None)
    if form.is_valid():
        palindromo_string = str(form.cleaned_data['palindromo'])
        if palindromo_string == palindromo_string[::-1] and Palindromo.objects.filter(palindromo=palindromo_string).count() == 0:
            form.save()
            return redirect('show_palindromos')
        else:
            return render(request, 'palindromo-error.html', {'palindromo': palindromo_string})
    return render(request, 'palindromos-form.html')

def delete_palindromos(request, id):
    palindromo = Palindromo.objects.get(id=id)
    palindromo.delete()
    return redirect('show_palindromos')


