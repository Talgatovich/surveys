from http import HTTPStatus

import pytest

from poll.models import Poll
from users.models import User

OK = HTTPStatus.OK
NOT_FOUND = HTTPStatus.NOT_FOUND
FOUND = HTTPStatus.FOUND


class TestContext:
    @pytest.mark.django_db(transaction=True)
    def test_unpassed_tests_context(self, question, user_client):
        """Выводятся все непройденные тесты"""
        url = ""
        cnt = Poll.objects.count()
        try:
            response = user_client.get(url)
        except Exception as e:
            assert False, f"""Страница `{url}` работает неправильно. Ошибка: `{e}`"""

        assert (
            len(response.context.get("tests")) == cnt
        ), "Убедитесь, что выводятся все тесты на странице"

    @pytest.mark.django_db(transaction=True)
    def test_passed_test_context(self, another_user, another_user_client, passed_poll):
        """Пройденные тесты не выводятся"""
        url = ""
        cnt = Poll.objects.exclude(passed_poll__user=another_user).count()
        try:
            response = another_user_client.get(url)
        except Exception as e:
            assert False, f"""Страница `{url}` работает неправильно. Ошибка: `{e}`"""

        assert (
            len(response.context.get("tests")) == cnt
        ), "Убедитесь, что выводятся все тесты на странице"

    @pytest.mark.django_db(transaction=True)
    def test_summary_table(self, another_user, another_user_client):
        """В таблице участников выводятся все пользователи"""
        url = "/auth/summary_table/"
        cnt = User.objects.count()
        try:
            response = another_user_client.get(url)
        except Exception as e:
            assert False, f"""Страница `{url}` работает неправильно. Ошибка: `{e}`"""

        assert (
            len(response.context.get("users_list")) == cnt
        ), "Убедитесь, что выводятся все пользователи на странице"
