import pytest

from poll.models import PassedPolls, Poll


@pytest.fixture()
def user(django_user_model):
    return django_user_model.objects.create_user(
        username="TestUser", password="1234567", balance=250
    )


@pytest.fixture()
def another_user(django_user_model):
    return django_user_model.objects.create_user(
        username="Stas", password="1234567", balance=250, email="1@mail.com"
    )


@pytest.fixture()
def user_client(user, client):
    client.force_login(user)
    return client


@pytest.fixture()
def another_user_client(another_user, client):
    client.force_login(another_user)
    return client


@pytest.fixture
def question():
    return Poll.objects.create(
        question="2 x 2 = ?",
        answer_1=4,
        answer_2=5,
        answer_3=46,
        answer_4="45",
        correct_answer=1,
    )


@pytest.fixture()
def passed_poll(another_user, question):
    c_user = another_user
    c_question = question
    return PassedPolls.objects.create(user=c_user, poll=c_question)
