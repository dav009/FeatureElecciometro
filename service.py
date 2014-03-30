# -*- coding: utf-8 -*- 

import json

from news_sources import RssFeeder, CaracolRadioRssSource, TiempoRssSource
from flask import Flask, request, Response
from EventSearcher import EventSearcher

from twitter_tools.bot_classifier import BotClassifier

app = Flask(__name__)
event_searcher = EventSearcher()
classifier = BotClassifier()

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
    try:
        date = request.args['date']
        words = json.loads(request.args['words'])
        number_of_candidates = json.loads(request.args['max'])

        list_of_events = event_searcher.get_event(words, date, number_of_candidates)
        return Response(json.dumps(list_of_events))
    except Exception as e:
        print e

@app.route("/bot_classifier")
def classify_bot():
    try:
        user = request.args['user']
        print user

        classification_result = classifier.classify(user)

        print classification_result

        result = {"bot":classification_result[0][1], "human":classification_result[0][0]}

        return Response(json.dumps(result))
    except Exception as e:
        print e


if __name__ == '__main__':
    init_server()
    app.run(host='0.0.0.0', port=5000)