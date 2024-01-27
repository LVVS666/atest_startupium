import requests


class Response():
    def __init__(self, url):
        self.base_url = url


    def get_request(self):
        return requests.get(url=f'{self.base_url}')


    def post_request(self, path=None, params=None, data=None, json=None, headers=None):
            url = f"{self.base_url}/{path}"
            return requests.post(url=url, params=params, data=data, json=json, headers=headers)


