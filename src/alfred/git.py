import os

from alfred import constants
import git
from git import RemoteProgress
from progress.bar import Bar


class CloneProgress(RemoteProgress):
    def create_bar(self, max_count):
        self.bar = Bar('Cloning', max=max_count)

    def update(self, op_code, cur_count, max_count=None, message=''):
        if not hasattr(self, "bar"):
            self.create_bar(max_count)
        self.bar.max = max_count
        self.bar.goto(cur_count)


def parse_url(git_url):
    GIT_URL_SPLIT = git_url.split(constants.GITHUB_DOMAIN_NAME)
    CLEAN_URL = GIT_URL_SPLIT[1][1:]
    USER, REPO = CLEAN_URL.split("/")
    USER = USER.lower()
    REPO = REPO.replace(".git", "")
    return USER, REPO


def create_user_dir(user):
    user_path = os.path.join(constants.GITHUB_BASE, user)
    if not os.path.exists(user_path):
        os.makedirs(user_path)
        print("Created user dir: {dir}".format(dir=user_path))
    return user_path


def clone_git_repo(user, repo, GIT_URL, branch="master"):
    repo_path = os.path.join(constants.GITHUB_BASE, user, repo)
    if os.path.exists(repo_path):
        print("Repo already exists: {repo}".format(repo=repo_path))
        os.chdir(repo_path)
        return False

    print("Cloning into path: {dir}".format(dir=repo_path))
    git.Repo.clone_from(GIT_URL, repo_path,
        branch=branch, progress=CloneProgress())
    print()
    os.chdir(repo_path)
