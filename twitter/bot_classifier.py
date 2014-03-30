import numpy as np
import utils
import math
from sklearn.linear_model import LogisticRegression
import json
from sklearn import svm

def entropy(labels):
    n_labels = len(labels)


    if n_labels <= 1:
        return 0.0

    counts = np.bincount(labels)
    probs = counts / float(n_labels)


    n_classes = np.count_nonzero(probs)

    if n_classes <= 1:
        return 0.0

    ent = 0.

    for i in probs:
        ent -= i * math.log(i,n_classes)

    return ent


class BotClassifier:


    def __init__(self):
        # other bots for test: "wutukovesare","wecavuxuzus","sixahabetuce","waroguqasex","qizorotolewi","qipujebyfir","gocakumebasu","panistillery","gocorubonur","solawodivyj","banaqihykaw"
        self.bot_list_of_users = ["xilixicosazo","temimyniwyra","qymodutyhaxo","qozozumexomy","PappalardoZinke","qizorotolewi","tyravyqabem","wavahovicij","vusexahybal"]
        self.non_bot_list_of_users = ["ELTIEMPO", "andresmao","nozuan", "dav009", "cubosensei","luchovelez","darknil", "Ministerio_TIC", "JuanManSantos", "petrogustavo"]
        self.twitter = utils.TwitterUtils()

        self.classifier = svm.SVC(probability=True)
        # uncomment this line to get training data file
        #self.export_training_vectors()
        self.train()

    def train(self):
        """
        trains the classifier by reading from a json file in the repo.
        """
        json_training_file = json_data=open("training_vectors.json").read()
        training_data = json.loads(json_training_file)

        self.classifier.fit(training_data['vectors'], training_data['labels'])

    def make_training_vectors(self):
        """
        given the list of bots and non-bots contructs their vectors and labels
        """
        labels = list()
        vectors = list()

        # positive samples
        for bot_user in self.bot_list_of_users:
            vectors.append(self.make_vector(bot_user))
            labels.append(1)

        # negative samples
        for real_user in self.non_bot_list_of_users:
            vectors.append(self.make_vector(real_user))
            labels.append(0)

        return vectors, labels


    def export_training_vectors(self):
        """
        uses the list of non-bots and bots users to construct a list of vectors
        and labels and xport them to a json file
        """
        vectors, labels = self.make_training_vectors()
        training_file = open('training_vectors.json', 'w')
        output_dict = {'vectors': vectors, "labels": labels}
        json.dump(output_dict, training_file)
        training_file.close()

    def classify(self, user):
        """
        @param user  string representing a twitter username
        @returns an array with the probabilities of each label 
        """
        vector = self.make_vector(user)
        return self.classifier.predict_proba([vector])

    def hash_tag_int_representation(self, list_of_str_hashtags):
        """
        @param list_of_str_hashtags: list of sets of hashtags
        @return list of ints where same sets are given a single integer identifier

        """
        map_of_hash_tags = dict()
        list_of_int_hash_tag = list()
        current_index = 0.0
        for hash_tag_set in list_of_str_hashtags:

            if len(hash_tag_set)==1 and utils.DEFAULT_NO_HASH_TEXT in hash_tag_set:
                # give a unique hashtag identifier to tweets with no hashtag
                list_of_int_hash_tag.append(current_index)
                current_index = current_index + 1.0
            else:
                # put the set in the hash and try to use an alreay given index
                if not hash_tag_set in map_of_hash_tags:
                    map_of_hash_tags[hash_tag_set] = current_index
                    current_index = current_index + 1.0
                list_of_int_hash_tag.append(map_of_hash_tags[hash_tag_set])

        return list_of_int_hash_tag

    def make_vector(self, user):
        """
        @param user: string representing a username in twitter
        @return vector with features of user's timeline
        """

        # get the hashtags of the user
        hash_tags = self.get_hashtags(user)

        int_hash_tag = self.hash_tag_int_representation(hash_tags)

        # calculate the entropy in the list of hash tags
        return [entropy(int_hash_tag)]


    def get_hashtags(self, user):
        """
        @param user string representing a username in twitter
        @return list of sets, each set contains the list of hashtags in a tweet
        """
        list_of_set_of_hash_tags = self.twitter.get_all_hash_tags_by_user(user)
        return list_of_set_of_hash_tags

classifier = BotClassifier()
classifier.classify("leonidasEsteban")