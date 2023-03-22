from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Poll, PassedPolls


def index(request):
    if request.user.is_anonymous:
        return render(request, "users/log_in.html")
    user = request.user
    questions = Poll.objects.exclude(Q(passedpolls__user=user))
    if request.method == "POST":
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            if q.answer == request.POST.get(q.question):
                PassedPolls.objects.create(poll=q, user=user)
                score += 10
                correct += 1
            else:
                wrong += 1

        user.scores += score
        user.passed_tests += total
        user.save()
        context = {
            "score": score,
            "correct": correct,
            "wrong": wrong,
            "total": total,
        }
        return render(request, "quiz/result.html", context)
    else:
        context = {"questions": questions}
        return render(request, "poll/index.html", context)
