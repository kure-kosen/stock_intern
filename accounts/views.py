from django.shortcuts import render
from .forms import MyForm

def form_test(request):
    if request.method == "POST":
        form = MyForm(data=request.POST)
        if form.is_valid():
            print(form.data.get('text'))
    else:
        form = MyForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })
