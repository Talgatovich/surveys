from django.contrib import admin
from .models import Poll, PassedPolls


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"question"
	)


@admin.register(PassedPolls)
class PassedPollsAdmin(admin.ModelAdmin):
	list_display = (
		"user",
		"poll",
	)