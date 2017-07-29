from django.shortcuts import render
from .forms import MyForm

def form_test(request):
    form = MyForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })
