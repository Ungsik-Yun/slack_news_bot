import os

import requests
import xmltodict
import json


class naver_api:
    def __init__(self):
        self.news_url = "https://openapi.naver.com/v1/search/news.xml?"
        self.short_url = "https://openapi.naver.com/v1/util/shorturl.xml"
        self.jisikin_url = "https://openapi.naver.com/v1/search/kin.xml?"

        self.headers = {
            'X-Naver-Client-Id': os.environ['naver_client_id'],
            'X-Naver-Client-Secret': os.environ['naver_client_secret']
        }

    def news_api(self, q, display_number=5):
        news_api = self.news_url + 'query="' + q + '"'
        news_api += "&display=" + str(display_number)
        r = requests.get(news_api, headers=self.headers)
        result = r.text
        parsed = xmltodict.parse(result)

        if 'item' not in parsed['rss']['channel']:
            return False

        return parsed['rss']['channel']['item']

    def jisikin_api(self,q,display_number=5):
        jisikin_api = self.jisikin_url + 'query="' + q + '"'
        jisikin_api += "&display=" + str(display_number)
        r = requests.get(jisikin_api, headers=self.headers)
        result = r.text
        parsed = xmltodict.parse(result)

        if 'item' not in parsed['rss']['channel']:
            return False

        return parsed['rss']['channel']['item']


    def short_url_api(self, ori_url):
        payload = {
            "url": ori_url
        }
        r = requests.post(self.short_url, headers=self.headers, data=payload)
        r = r.text
        r = xmltodict.parse(r)

        return r['result']['result']['url']
        # return r