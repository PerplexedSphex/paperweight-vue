from django.contrib.auth.views import FormView
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from .models import EncampUser
from .forms import SignupForm


class SignupView(FormView):
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = EncampUser(email=form.cleaned_data['email'])
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return HttpResponseRedirect(reverse('login'))

    def get_form(self, form_class=None):
        return SignupForm()
