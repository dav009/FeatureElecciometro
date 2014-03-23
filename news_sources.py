import dateutil.parser
import feedparser

class BaseRssSource(object):

    def __init__(self, url):
        self.feed_url = url

    def get_publication_date(self, article):
        pass

    def get_content(self, article):
        pass

    def get_url(self, article):
        pass

    def get_title(self, article):
        pass

class TiempoRssSource(BaseRssSource):

    def __init__(self, url):
        super(TiempoRssSource, self).__init__(url)

    def get_publication_date(self, article):
        return article['published']

    def get_content(self, article):
        return article['content'][0]['value']

    def get_url(self, article):
        return article['link']

    def get_title(self, article):
        return article['title']


class CaracolRadioRssSource(BaseRssSource):
    
    def __init__(self, url):
        super(CaracolRadioRssSource, self).__init__(url=url)

    def get_publication_date(self, article):
        return article['published']

    def get_content(self, article):
        return article['summary']

    def get_url(self, article):
        return article['link']

    def get_title(self, article):
        return article['title']


class RssFeeder:

    def __init__(self, rss_source):
        self.source = rss_source
        self.seconds_in_a_day = 166400

    def get_content(self, date_str):
        self.feed = feedparser.parse(self.source.feed_url)
        return self.filter_by_date(date_str)

    '''
    Filtering the RSS feed using a pivot date
    '''
    def filter_by_date(self, date_str):
        reference_date = dateutil.parser.parse(date_str)

        list_of_items = list()

        for item in self.feed["items"]:
            item_date = dateutil.parser.parse(self.source.get_publication_date(item))
            item_date = item_date.replace(tzinfo=None)
            total_seconds = abs((reference_date-item_date).total_seconds())
            # filtering articles one day recent
            if total_seconds < self.seconds_in_a_day:
                new_item = dict()
                new_item['url'] = self.source.get_url(item)
                new_item['content'] = self.source.get_content(item)
                new_item['published'] = self.source.get_publication_date(item)
                new_item['title'] = self.source.get_title(item)

                list_of_items.append(new_item)
        return list_of_items