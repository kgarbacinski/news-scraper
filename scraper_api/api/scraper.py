import asyncio
import aiohttp
import nest_asyncio
from typing import List, Coroutine
from random import choice as random
from bs4 import BeautifulSoup as bs


from .config import TimeConfig, TheGuardianConfig, BBCConfig, NewYorkTimesConfig
from .user_agents import UserAgent


class Scraper:
    def __init__(self, url: str, name: str):
        self.url = url
        self.name = name
        
    def execute(self):
        raise NotImplementedError

class TimeScraper(Scraper):
    def __init__(self):
        super().__init__(TimeConfig.URL, TimeConfig.NAME)
    
    def execute(self, content: str, keyword: str):
        soup = bs(content, 'html.parser')
        content = soup.findAll('h3')
        
        try:
            titles = set()
            for title in content:
                if keyword.lower() in title.text.lower():
                    titles.add((title.text.strip(), 'https://time.com/' + title.find_parent('a')['href']))

            return [list(title) for title in titles]

        except TypeError: 
            return [] 


class BBCScraper(Scraper):
    def __init__(self):
        super().__init__(BBCConfig.URL, BBCConfig.NAME)

    def execute(self, content: str, keyword: str):
        soup = bs(content, 'html.parser')
        content = soup.findAll('h3')

        try:
            titles = set()
            for title in content:
                if keyword.lower() in title.text.lower():
                    titles.add((title.text.strip(), 'https://www.bbc.com' + title.find_parent('a')['href']))

            return [list(title) for title in titles]
        
        except TypeError: 
            return [] 


class TheGuardianScraper(Scraper):
    def __init__(self):
        super().__init__(TheGuardianConfig.URL, TheGuardianConfig.NAME)
  
    def execute(self, content: str, keyword: str):
        soup = bs(content, 'html.parser')
        content = soup.findAll('a')

        try:
            titles = set()
            for title in content:
                if keyword.lower() in title.text.lower():
                    titles.add((title.text.strip(), title['href']))

            return [list(title) for title in titles]
        
        except TypeError: 
            return [] 


class NewYorkTimesScraper(Scraper):
    def __init__(self):
        super().__init__(NewYorkTimesConfig.URL, NewYorkTimesConfig.NAME)
  
    def execute(self, content: str, keyword: str):
        soup = bs(content, 'html.parser')
        content = soup.findAll('a')

        try:
            titles = set()
            for title in content:
                if keyword.lower() in title.text.lower():
                    titles.add((title.text.strip(), title['href']))

            return [list(title) for title in titles]

        except TypeError: 
            return [] 


class HttpRequestSender:
    async def get(self, session: aiohttp.ClientSession, data) -> Coroutine:
        async with session.get(data[0]) as response:
            text = await response.text()
            return text, data[1]


class Fetcher:
    def __init__(self) -> None:
        self.user_agent = UserAgent()
        self.headers = {'User-Agent': random(self.user_agent.user_agents)}
        
    async def fetch(self, data, inner):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = [inner(session, pair) for pair in data]            
            responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        return responses
        

class Executor:
    def __init__(self, *scrapers):
        self.scrapers: List[Scraper] = list(scrapers) 
        self.fetcher = Fetcher()
        self.http_request_sender = HttpRequestSender()
    
    def execute(self, keyword: str): 
        data = [(scraper.url, scraper.name) for scraper in self.scrapers]
        
        nest_asyncio.apply()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
        data_resp = loop.run_until_complete(self.fetcher.fetch(data, self.http_request_sender.get))

        articles = {data[1]: self.scrapers[index].execute(data[0], keyword) 
                    for index, data in enumerate(data_resp)}

        sorted_articles = {pair[0]: pair[1] 
                    for pair in sorted(articles.items(), key=lambda x:len(x[1]), reverse=True)}

        return sorted_articles

class ContentGetter:
    @staticmethod
    def get(keyword):
        executor = Executor(
            TimeScraper(), 
            BBCScraper(), 
            TheGuardianScraper(), 
            NewYorkTimesScraper()
        )

        data = {keyword: executor.execute(keyword)}

        return data