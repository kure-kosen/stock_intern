from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from .models import User


class UserCreate(CreateView):
    model = User
    template_name = 'accounts/form.html'
    fields = ("user_id", "user_name", "password" )  # リストもしくはタプル

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
