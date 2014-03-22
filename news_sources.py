import dateutil.parser
import feedparser

class BaseRssSource:

    def __init__(self, url):
        self.url = url

    def get_publication_date(self):
        pass

    def get_content(self, article):
        pass

    def get_url(self, article):
        pass

class TiempoRssSource(BaseRssSource):

    def __init__(self, url):
        super(TiempoRssSource, self).__init__(url)

    def get_publication_date(self, article):

class CaracolRadioRssSource(BaseRssSource):
    
    def __init__(self, url):
        super(CaracolRadioRssSource, self).__init__(url)


class RssFeeder:

    def __init__(self, rss_url):
        self.url = rss_url 
        self.seconds_in_a_day = 166400

    def get_content(self, date_str):
        self.feed = feedparser.parse(self.url)
        return self.filter_by_date(date_str)

    '''
    Filtering the RSS feed using a pivot date
    '''
    def filter_by_date(self, date_str):
        reference_date = dateutil.parser.parse(date_str)

        list_of_items = list()

        for item in self.feed["items"]:
            item_date = dateutil.parser.parse(item["published"])
            item_date = item_date.replace(tzinfo=None)
            total_seconds = abs((reference_date-item_date).total_seconds())
            # filtering articles one day recent
            if total_seconds < self.seconds_in_a_day:
                list_of_items.append(item)
        return list_of_items