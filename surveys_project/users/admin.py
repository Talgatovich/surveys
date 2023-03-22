from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"username",
		"password",
		"first_name",
		"last_name",
		"email",
		"balance",
		"passed_tests",
		"avatar",
		"username_color",
		"back_color",
	)
