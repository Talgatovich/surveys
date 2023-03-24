from http import HTTPStatus

import pytest

OK = HTTPStatus.OK
NOT_FOUND = HTTPStatus.NOT_FOUND
FOUND = HTTPStatus.FOUND


class TestUrls:
    @pytest.mark.django_db(transaction=True)
    def test_auth_urls(self, client):
        """У неавторизованного пользователя есть доступ
        к страницам регистрации/входа и к главной странице.
        """
        urls = ["/auth/login/", "/auth/logout/", "/auth/signup/", ""]
        for url in urls:
            try:
                response = client.get(url)
            except Exception as e:
                assert (
                    False
                ), f"""Страница `{url}` работает неправильно. Ошибка: `{e}`"""
            assert (
                response.status_code != NOT_FOUND
            ), f"Страница `{url}` не найдена, проверьте этот адрес в *urls.py*"
            assert (
                response.status_code == OK
            ), f"Ошибка {response.status_code} при открытии `{url}`. Проверьте ее view-функцию"

    @pytest.mark.django_db(transaction=True)
    def test_unauthorized_client_redirect(self, client):
        """У неавторизованного пользователя нет доступа к страницам"""
        urls = ["/auth/profile/", "/auth/summary_table/"]
        for url in urls:
            try:
                response = client.get(url)
            except Exception as e:
                assert (
                    False
                ), f"""Страница `{url}` работает неправильно. Ошибка: `{e}`"""
            assert (
                response.status_code != NOT_FOUND
            ), f"Страница `{url}` не найдена, проверьте этот адрес в *urls.py*"

            assert (
                response.status_code == FOUND
            ), f"Ошибка {response.status_code} при открытии `{url}`. Проверьте ее view-функцию"

    @pytest.mark.django_db(transaction=True)
    def test_authorized_client(self, user_client):
        """У авторизованного пользователя есть доступ к страницам"""
        urls = [
            "",
            "/auth/summary_table/",
        ]
        for url in urls:
            try:
                response = user_client.get(url)
            except Exception as e:
                assert (
                    False
                ), f"""Страница `{url}` работает неправильно. Ошибка: `{e}`"""
            assert (
                response.status_code != NOT_FOUND
            ), f"Страница `{url}` не найдена, проверьте этот адрес в *urls.py*"

            assert (
                response.status_code == OK
            ), f"Ошибка {response.status_code} при открытии `{url}`. Проверьте ее view-функцию"
