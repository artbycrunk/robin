import click
from alfred import git, constants

@click.group()
def cli():
    pass


@cli.group()
def git():
    pass


@git.command()
@click.argument('url')
def clone(url):
    if constants.GITHUB_DOMAIN_NAME in url:
        USER, REPO = git.parse_url(url)
        click.echo(f"Github:\n  User: {USER}\n  Repo: {REPO}")
        user_dir = git.create_user_dir(USER)
        git.clone_git_repo(USER, REPO, url)


if __name__ == '__main__':
    cli()