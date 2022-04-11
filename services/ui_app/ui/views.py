from django.shortcuts import render
from .auth_token_fetcher import get_auth_token


def main_view(request) -> None:
    """
    Renders main template and sets generated auth token to allow JS request data from scraper-app & history-app
    """
    return render(
        request,
        "ui/main.html",
        {"title": "News Scraper", "API_TOKEN": get_auth_token()},
    )
