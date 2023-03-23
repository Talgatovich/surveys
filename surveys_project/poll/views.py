from django.shortcuts import render

from .models import PassedPolls, Poll


def index(request):
    if request.user.is_anonymous:
        return render(request, "poll/welcome.html")
    user = request.user
    tests = Poll.objects.exclude(passed_poll__user=user)
    if request.method == "POST":
        balance = 0
        wrong = 0
        correct = 0
        total = 0
        for val in tests:
            total += 1
            if val.correct_answer == request.POST.get(val.question):
                PassedPolls.objects.create(poll=val, user=user)
                balance += 30
                correct += 1
            else:
                wrong += 1

        user.balance += balance
        user.passed_tests += total
        user.save()
        context = {
            "balance": balance,
            "correct": correct,
            "wrong": wrong,
            "total": total,
        }
        return render(request, "poll/results.html", context=context)
    else:
        context = {"tests": tests}
        return render(request, "poll/index.html", context=context)
