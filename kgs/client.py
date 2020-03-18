import requests
from bs4 import BeautifulSoup

from kgs.config import StaticConfiguration as StaticConf


class KGSClient:

    def __init__(self,
                 url=StaticConf.KORONA_GOV_SK_URL,
                 user_agent=StaticConf.USER_AGENT):
        self._target_url = url
        self._user_agent = user_agent

    def do_get(self, url):
        return requests.get(
            url=url,
            headers={'user-agent': self._user_agent}
        )

    def load_stats(self):
        res = self.do_get(self._target_url)

        soup = BeautifulSoup(res.text, features='html.parser')
        values = [int(i.text) for i in soup.findAll('span', {'class': 'countValue'})]

        return {
            'tested': values[0],
            'negative': values[1],
            'positive': values[2]
        }
