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

    if news_list:
        for i in news_list:
            short_url = connector.short_url_api(i['originallink'])
            attachments = [
                {
                    'title': i['title'],
                    'title_link': short_url,
                    'text': i['description']
                }]
            msg.send_webapi('', json.dumps(attachments))
    else:
        msg.reply("검색어 "+"`"+q+"` 로 " + "검색된 결과가 없습니다.")


@listen_to("!지식인 (.*)", re.IGNORECASE)
def search_news(msg, q):
    connector = naver_api()
    jisik_list = connector.jisikin_api(q)

    if jisik_list:
        for i in jisik_list:
            short_url = connector.short_url_api(i['link'])
            attachments = [
                {
                    'title': i['title'],
                    'title_link': short_url,
                    'text': i['description']
                }]
            msg.send_webapi('', json.dumps(attachments))
    else:
        msg.reply("검색어 "+"`"+q+"` 로 " + "검색된 결과가 없습니다.")


@listen_to("!단축 (.*)", re.IGNORECASE)
def shorten_url(msg, q):
    connector = naver_api()
    shorten = connector.short_url_api(q)
    msg.reply(shorten)


@respond_to("헬프", re.IGNORECASE)
@respond_to("도움말", re.IGNORECASE)
def help_display(msg):
    help_text = []
    help_text.append("""
버나드 뉴스 봇의 도움말에 오신것을 환영합니다.
이 봇은 다음의 기능을 수행할 수 있습니다.
`지식인` 검색
`뉴스` 검색
url `단축`
""")

    help_text.append("""
각각의 기능은 다음의 명령어를 사용해서 이용할 수 있습니다.

`!뉴스 검색어`
`!지식인 검색어`
`!단축 URL`

각각 `검색어`와 `URL`을 원하는 검색어와 URL로 바꾸어 사용하면 됩니다.
예를 들어, `카카오페이지`를 검색하고 싶을 경우,
`!뉴스 카카오페이지`
라고 채팅방에 치면 됩니다.
""")

    help_text.append("""
뉴스와 지식인의 검색결과는 `"`로 감싸서 검색을 하게 되며, 날짜순으로 정렬되어 최상위 5개를 가져오게 됩니다.
""")

    for text in help_text:
        msg.send(text)
