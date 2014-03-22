# -*- coding: utf-8 -*- 
from news_sources import RssFeeder
from VectorUtils import Vector
from Cluster import Clustering

feeders = list()

def init_server():

    url_feeds = [
                #"http://www.eltiempo.com/politica/rss.xml",
                "http://www.caracol.com.co/feed.aspx?id=196"
                ]

    for feed in url_feeds:
        feeder = RssFeeder(feed)
        feeders.append(feeder)

init_server()

def get_events(word_vector, date_str):

    articles = list()
    vectors = list()

    for feeder in feeders:
        print "in feeders"
        articles = articles + feeder.get_content(date_str)

    print articles[0]


    for article in articles:
        vector = Vector(article['content'][0]['value']).get_vector()
        vectors.append(vector)
        print vector

    word_vector_text = ' '.join(word_vector)
    flag_vector = Vector(word_vector_text).get_vector()
    for key,value in flag_vector.items():
        flag_vector[key] =  flag_vector[key] + 2

    clustering = Clustering(vectors, flag_vector)

    index, value = clustering.get_articles()

    print articles[index]
    print "Value:"
    print "\t",value
    print articles[index]['link']



    # cluster articles with word_vector


words ="Peñalosa, Peñalosa, Enrique, Enrique, registradura, registraduria, Peñalosa, CNE, candidato, verde".split(",")



get_events(words, "2014-03-21 23:00:00")