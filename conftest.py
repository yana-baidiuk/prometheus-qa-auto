import pytest
import sqlite3 as sql
from modules.api.clients.github import GitHub


class User():
    def __init__(self):
        self.name = None
        self.second_name = None

    def create_user(self, name, second_name, repo_name):
        self.name = name
        self.second_name = second_name
        self.repo_name = repo_name


@pytest.fixture
def user():
    user = User()
    user.create_user('Yana', 'Baidiuk')
    yield user
    user.remove_user()


@pytest.fixture
def github_api():
    user = GitHub()
    yield user
