import json

import requests
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import xmltodict
import os
import re
import random
from bernard_bot.naver_api.naver import naver_api


@listen_to("!뉴스 (.*)", re.IGNORECASE)
def search_news(msg, q):
    connector = naver_api()
    news_list = connector.news_api(q)

    for i in news_list:
        short_url = connector.short_url_api(i['originallink'])
        attachments = [
            {
                'title': i['title'],
                'title_link': short_url,
                'text': i['description']
            }]
        msg.send_webapi('', json.dumps(attachments))


@listen_to("!지식인 (.*)", re.IGNORECASE)
def search_news(msg, q):
    connector = naver_api()
    jisik_list = connector.jisikin_api(q)

    for i in jisik_list:
        short_url = connector.short_url_api(i['link'])
        attachments = [
            {
                'title': i['title'],
                'title_link': short_url,
                'text': i['description']
            }]
        msg.send_webapi('', json.dumps(attachments))


@listen_to("!단축 (.*)", re.IGNORECASE)
def shorten_url(msg, q):
    connector = naver_api()
    shorten = connector.short_url_api(q)
    msg.reply(shorten)
