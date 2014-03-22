from nltk.stem.snowball import SnowballStemmer
from BeautifulSoup import BeautifulSoup
import nltk

class Tokenizer:

    def __init__(self):
        pass

    def clean_html(self, text):
        soup_text = BeautifulSoup(text, convertEntities=BeautifulSoup.HTML_ENTITIES)
        no_html = ''.join(soup_text.findAll(text=True))
        return no_html

    def tokenize(self, text):
        cleaned_text = self.clean_html(text)
        return nltk.word_tokenize(cleaned_text)

class Stemmer:

    def __init__(self):
        self.stemmer = SnowballStemmer("spanish")

    def stem(self, word):
        return self.stemmer.stem(word)

class Vector:

    def __init__(self, text):
        self.text = text
        self.vector = dict()

    def addToVector(self, token_type):
        if not token_type in self.vector:
            self.vector[token_type] = 0
        self.vector[token_type] = self.vector[token_type] + 1

    def transform_text(self):
        tokenizer = Tokenizer()
        stemmer = Stemmer()

        tokens = tokenizer.tokenize(self.text)
        for token in tokens:
            stemmed_word = stemmer.stem(token)
            self.addToVector(stemmed_word)


    def get_vector(self):
        self.transform_text()
        return self.vector

