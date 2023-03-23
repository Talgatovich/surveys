from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CreationForm
from .models import User


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("users:login")
    template_name = "users/signup.html"


@login_required
def profile(request):
    return render(request, "users/profile.html")


def buy_color(request, price, back_color=None, username_color=None):
    user = User.objects.get(id=request.user.id)
    if user.balance < int(price):
        return render(request, "users/error.html")
    if back_color:
        user.back_color = back_color
    elif username_color:
        user.username_color = username_color
    user.balance -= int(price)
    user.save()
    return redirect("users:profile")


def summary_table(request):
    queryset = User.objects.all().order_by("-passed_tests")
    return render(request, "users/summary_table.html", context={"users_list": queryset})
