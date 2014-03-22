import math
import operator

class Clustering:

    def __init__(self, article_vectors, flag_vector):
        self.vectors = article_vectors
        self.flag_vector = flag_vector


    def vector_magnitude(self, v):
        magnitude = 0.0
        for dimension, value in v.items():
            magnitude = magnitude + (value**2)

        return math.sqrt(magnitude)

    def score_candidate_articles(self):
        cosine_sims = list()
        for vector in self.vectors:
            current_cosine_sim = self.cosine_sim(vector, self.flag_vector)
            cosine_sims.append(current_cosine_sim)

        return cosine_sims

    def get_articles(self):
        cosine_scores = self.score_candidate_articles()
        max_index, max_value = max(enumerate(cosine_scores), key=operator.itemgetter(1))
        return max_index, max_value

    def cosine_sim(self, v1, v2):

        cosine_sim = 0.0
        all_dimensions = set(v1.keys() + v2.keys())

        numerator = 0.0

        for dimension in all_dimensions:
            if dimension in v1 and dimension in v2:
                numerator = numerator + (v1[dimension] * v2[dimension])

        v1_magnitude = self.vector_magnitude(v1)
        v2_magnitude = self.vector_magnitude(v2)

        denominator = v1_magnitude*v2_magnitude

        try:
            cosine_sim = numerator / denominator
        except Exception:
            pass

        return cosine_sim
            




