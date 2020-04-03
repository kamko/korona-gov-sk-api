import jsonpath_ng
import requests

from kgs.config import StaticConfiguration as StaticConf


class KGSClient:

    def __init__(self,
                 url=StaticConf.KORONA_GOV_SK_API_URL,
                 user_agent=StaticConf.USER_AGENT):
        self._target_url = url
        self._user_agent = user_agent

    def do_get(self, url):
        return requests.get(
            url=url,
            headers={'user-agent': self._user_agent},
            timeout=10
        )

    def load_stats(self):
        res = self.do_get(self._target_url)

        json = res.json()

        positive_path_expr = jsonpath_ng.parse('$.tiles.k5.data.d[*].v')
        negative_path_expr = jsonpath_ng.parse('$.tiles.k6.data.d[*].v')
        recovered_path_expr = jsonpath_ng.parse('$.tiles.k7.data.d[*].v')
        dead_path_expr = jsonpath_ng.parse('$.tiles.k8.data.d[*].v')

        positive = list(positive_path_expr.find(json))[-1].value
        negative = list(negative_path_expr.find(json))[-1].value
        recovered = list(recovered_path_expr.find(json))[-1].value
        dead = list(dead_path_expr.find(json))[-1].value

        return {
            'tested': positive + negative,
            'negative': negative,
            'positive': positive,
            'recovered': recovered,
            'dead': dead
        }
