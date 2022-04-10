import os
from decouple import config

from django.shortcuts import render

def main_view(request):
    return render(request, 'ui/main.html', {
        'title': 'News Scraper',
        'API_TOKEN': config('API_AUTH_TOKEN', os.environ['API_AUTH_TOKEN'])
        })
