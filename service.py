# -*- coding: utf-8 -*- 

import json

from news_sources import RssFeeder, CaracolRadioRssSource, TiempoRssSource
from flask import Flask, request, Response
from EventSearcher import EventSearcher

app = Flask(__name__)
event_searcher = EventSearcher()

def init_server():

    url_feeds = [
                TiempoRssSource("http://www.eltiempo.com/politica/rss.xml"),
                CaracolRadioRssSource("http://www.caracol.com.co/feed.aspx?id=196")
                ]

    for feed in url_feeds:
        feeder = RssFeeder(feed)
        event_searcher.add_feedsource(feeder)


@app.route("/get_event")
def get_event():
    date = request.args['date']
    words = json.loads(request.args['words'])

    score, url = event_searcher.get_event(words, date)
    return Response(json.dumps({'score':score, 'url':url}))

if __name__ == '__main__':
    init_server()
    app.run(host='0.0.0.0', port=5000)