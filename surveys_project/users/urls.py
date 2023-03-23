from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logged_out.html"),
        name="logout",
    ),
    path("login/", LoginView.as_view(template_name="users/log_in.html"), name="login"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("profile/", views.profile, name="profile"),
    path("summary_table/", views.summary_table, name="summary_table"),
    path(
        r"buy_back_color/int:<price>/<back_color>/",
        views.buy_color,
        name="buy_back_color",
    ),
    path(
        r"buy_username_color/int:<price>/<username_color>/",
        views.buy_color,
        name="buy_username_color",
    ),
]
