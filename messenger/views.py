from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = "messenger/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = "messenger:login"


class RegisterView(CreateView):
    template_name = "messenger/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("messenger:login"))
