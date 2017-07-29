from django.shortcuts import render

from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

from .forms import MyForm


class FormTest(FormView):
    form_class = MyForm
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('accounts:index')


# form_test = FormTest.as_view()


# def form_test(request):
#     if request.method == "POST":
#         form = MyForm(data=request.POST)
#         if form.is_valid():
#             print(form.data.get('text'))
#     else:
#         form = MyForm()
#     return render(request, 'accounts/form.html', {
#         'form': form,
#     })
