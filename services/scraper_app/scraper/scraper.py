import asyncio
import aiohttp
import nest_asyncio
from typing import List, Coroutine, Dict
from random import choice as random
from bs4 import BeautifulSoup as bs


from .config import TimeConfig, TheGuardianConfig, BBCConfig, NewYorkTimesConfig
from .user_agents import UserAgent


class Scraper:
    """
    Main scraper interface
    """

    def __init__(self, url: str, name: str) -> None:
        self.url = url
        self.name = name

    def execute(self):
        raise NotImplementedError


class TimeScraper(Scraper):
    """
    Customized scrapers with BS4 configs. Each websource has a different HTML structure
    so we need to set a separate BS parsing
    """

    def __init__(self) -> None:
        super().__init__(TimeConfig.URL, TimeConfig.NAME)

    def execute(self, content: str, keyword: str) -> List:
        soup = bs(content, "html.parser")
        content = soup.findAll("h3")

        try:
            titles = set()
            for title in content:
                if keyword.lower() in title.text.lower():
                    titles.add(
                        (
                            title.text.strip(),
                            "https://time.com/" + title.find_parent("a")["href"],
                        )
                    )

            return [list(title) for title in titles]

        except TypeError:
            return []


class BBCScraper(Scraper):
    """
    Customized scrapers with BS4 configs. Each websource has a different HTML structure
    so we need to set a separate BS parsing
    """

    def __init__(self) -> None:
        super().__init__(BBCConfig.URL, BBCConfig.NAME)

    def execute(self, content: str, keyword: str) -> List:
        soup = bs(content, "html.parser")
        content = soup.findAll("h3")

        try:
            titles = set()
            for title in content:
                if keyword.lower() in title.text.lower():
                    titles.add(
                        (
                            title.text.strip(),
                            "https://www.bbc.com" + title.find_parent("a")["href"],
                        )
                    )

            return [list(title) for title in titles]

        except TypeError:
            return []


class TheGuardianScraper(Scraper):
    """
    Customized scrapers with BS4 configs. Each websource has a different HTML structure
    so we need to set a separate BS parsing
    """

    def __init__(self) -> None:
        super().__init__(TheGuardianConfig.URL, TheGuardianConfig.NAME)

    def execute(self, content: str, keyword: str) -> List:
        soup = bs(content, "html.parser")
        content = soup.findAll("a")

        try:
            titles = set()
            for title in content:
                if keyword.lower() in title.text.lower():
                    titles.add((title.text.strip(), title["href"]))

            return [list(title) for title in titles]

        except TypeError:
            return []


class NewYorkTimesScraper(Scraper):
    """
    Customized scrapers with BS4 configs. Each websource has a different HTML structure
    so we need to set a separate BS parsing
    """

    def __init__(self) -> None:
        super().__init__(NewYorkTimesConfig.URL, NewYorkTimesConfig.NAME)

    def execute(self, content: str, keyword: str) -> List:
        soup = bs(content, "html.parser")
        content = soup.findAll("a")

        try:
            titles = set()
            for title in content:
                if keyword.lower() in title.text.lower():
                    titles.add((title.text.strip(), title["href"]))

            return [list(title) for title in titles]

        except TypeError:
            return []


class HttpRequestSender:
    """
    HTTP interface to run GET requests asynchronous.
    Takes a list of scraper configs.
    Returns a asyncio coroutine.
    """

    async def get(self, session: aiohttp.ClientSession, data) -> Coroutine:
        async with session.get(data[0]) as response:
            text = await response.text()
            return text, data[1]


class Fetcher:
    """
    Wrapping interface to scrap the content from *Scraper instance.
    Returns a list of responses to be consumed by each scraper.
    Requests are modified with random UA strings to generate 'legit' traffic to the source.
    """

    def __init__(self) -> None:
        self.user_agent = UserAgent()
        self.headers = {"User-Agent": random(self.user_agent.user_agents)}

    async def fetch(self, data, inner) -> List:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = [inner(session, pair) for pair in data]
            responses = await asyncio.gather(*tasks, return_exceptions=True)

        return responses


class Executor:
    """
    Generates new asyncio loop with coroutines.
    Fetches content from webpage with Fetcher().
    Content being filtered by each scraper using a keyword with execute() and sorted by # of articles.
    """

    def __init__(self, *scrapers) -> None:
        self.scrapers: List[Scraper] = list(scrapers)
        self.fetcher = Fetcher()
        self.http_request_sender = HttpRequestSender()

    def execute(self, keyword: str) -> Dict:
        data = [(scraper.url, scraper.name) for scraper in self.scrapers]

        nest_asyncio.apply()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        data_resp = loop.run_until_complete(
            self.fetcher.fetch(data, self.http_request_sender.get)
        )

        articles = {
            data[1]: self.scrapers[index].execute(data[0], keyword)
            for index, data in enumerate(data_resp)
        }

        sorted_articles = {
            pair[0]: pair[1]
            for pair in sorted(articles.items(), key=lambda x: len(x[1]), reverse=True)
        }

        return sorted_articles


class ContentGetter:
    """
    Passes a list of scrappers to Executor.
    Retrieves filtered content from each scraper and returns dict.
    """

    @staticmethod
    def get(keyword) -> Dict:
        executor = Executor(
            TimeScraper(), BBCScraper(), TheGuardianScraper(), NewYorkTimesScraper()
        )

        data = {"keyword": keyword, "articles": executor.execute(keyword)}

        return data
