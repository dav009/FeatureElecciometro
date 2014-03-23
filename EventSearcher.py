
from VectorUtils import Vector

from Cluster import Clustering

class EventSearcher:

    def __init__(self):
        self.feeders = list()


    def add_feedsource(self, feed_source):
        self.feeders.append(feed_source)

    def get_event(self, word_vector, date_str, number_of_candidates):

        articles = list()
        vectors = list()

        # get the articles from each feeder
        for feeder in self.feeders:
            articles = articles + feeder.get_content(date_str)

        # transform the content from each feeder into vector
        for article in articles:
            vector = Vector(article['content']).get_vector()
            vectors.append(vector)

        # convert the flag input into a vector
        word_vector_text = ' '.join(word_vector)
        flag_vector = Vector(word_vector_text).get_vector()
        for key,value in flag_vector.items():
            flag_vector[key] =  flag_vector[key] + 2

        # find the most similar article for the input flag_vector
        clustering = Clustering(vectors, flag_vector)
        sorted_scores = clustering.get_articles()


        list_of_url_score_tuples = list()
        for index, score in sorted_scores:
            list_of_url_score_tuples.append({"score":score, "url":articles[index]['url']})

        list_of_url_score_tuples = list_of_url_score_tuples[:number_of_candidates]

        return list_of_url_score_tuples