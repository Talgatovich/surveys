from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CreationForm
from .models import User


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("quiz:index")
    template_name = "users/signup.html"


def profile(request):
    return render(request, "users/profile.html")
