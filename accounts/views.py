from django.views.generic import CreateView
from .forms import CreateCustomUser
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = CreateCustomUser
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

