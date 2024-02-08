import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('yana-baidiuk')
    assert user['login'] == 'yana-baidiuk'


@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user('yanabaidiuk')
    assert user['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    user = github_api.search_repo('become-qa-auto')
    assert user['total_count'] >= 54


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    user = github_api.search_repo('become-qa-auto-not-exist')
    assert user['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    user = github_api.search_repo('y')
    assert user['total_count'] > 0
