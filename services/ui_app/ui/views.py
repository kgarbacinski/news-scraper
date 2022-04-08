from django.shortcuts import render

def main_view(request):
    return render(request, 'ui/main.html', {'title': 'News Scraper'})
