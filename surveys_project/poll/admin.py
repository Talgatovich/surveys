from django.contrib import admin
from .models import Poll, PassedPolls


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
	list_display = (
		"answer_1",
		"answer_2",
		"answer_3",
		"answer_4",
		"correct_answer",
	)


@admin.register(PassedPolls)
class PassedPollsAdmin(admin.ModelAdmin):
	list_display = (
		"user",
		"poll",
	)