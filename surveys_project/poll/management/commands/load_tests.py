import json
import os

from django.core.management.base import BaseCommand

from poll.models import Poll
from surveys_project.settings import BASE_DIR


class Command(BaseCommand):
    help = "Выгружаем тесты из json в базу."

    def add_arguments(self, parser):
        parser.add_argument("file_name", default="polls.json", nargs="?", type=str)

    def handle(self, *args, **options):
        f = open(
            os.path.join(os.path.join(BASE_DIR, "poll/data"), options["file_name"]),
            "r",
            encoding="utf-8",
            errors="ignore",
        )
        tests = f.read()
        f.close()
        data = json.loads(tests)
        items = []
        if Poll.objects.count() == 0:
            for item in data:
                poll = Poll(
                    question=item["question"],
                    answer_1=item["answer_1"],
                    answer_2=item["answer_2"],
                    answer_3=item["answer_3"],
                    answer_4=item["answer_4"],
                    correct_answer=item["correct_answer"],
                )
                items.append(poll)
            Poll.objects.bulk_create(items)
            print("Данные успешно загружены!")
        else:
            print("Данные уже были загружены ранее!")
