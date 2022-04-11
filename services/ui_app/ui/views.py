from django.shortcuts import render
from .auth_token_fetcher import get_auth_token

def main_view(request):
    return render(request, 'ui/main.html', {
        'title': 'News Scraper',
        'API_TOKEN': get_auth_token()
        })
