from django.shortcuts import render

from .dummy_data import DUMMY_DATA

def main_view(request):
    return render(request, 'ui/main.html', {'title': 'News Scraper', 'articles': DUMMY_DATA})
