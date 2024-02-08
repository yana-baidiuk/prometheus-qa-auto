import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''
