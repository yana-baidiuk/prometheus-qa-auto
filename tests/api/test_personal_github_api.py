import pytest


@pytest.mark.github
def test_get_list_commits(github_api):
    commits = github_api.search_commits('yana-baidiuk', 'prometheus-qa-auto')
    commits_number = len(commits)
    first_commit_message = commits[0]['commit']['message']
    committer_email = commits[0]['commit']['committer']['email']
    assert first_commit_message == 'First github api tests have been performed'
    assert commits_number == 4
    assert committer_email == 'jane.baidiuk@gmail.com'


@pytest.mark.github
def test_get_last_year_commit_activity(github_api):
    commit_activity = github_api.get_last_year_commit_activity(
        'yana-baidiuk', 'prometheus-qa-auto')
    commit_activity_length = len(commit_activity)
    print('total:', commit_activity_length)
    total_commits = 0
    for i in range(commit_activity_length):
        new_commits = commit_activity[i]['total']
        total_commits += new_commits
    assert total_commits != 0


@pytest.mark.github
def test_check_emoji(github_api):
    emoji = github_api.check_emoji()
    assert 'cactus' in emoji
