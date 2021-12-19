from newsapi import NewsApiClient as NAC
import apikey  # sorry cannot share that
from datetime import date


class NewsFeed():
    '''
    Repersenting multiple news titles and urls 
    as part of a single string.
    '''

    apikey = apikey.key
    newsapi = NAC(api_key=apikey)

    def __init__(self, intrest, from_date, to_date, language) -> None:
        self._intrest = intrest
        self._from_date = from_date
        self._to_date = to_date
        self._lang = language

    def get(self):
        '''
        To get the news article for specific intrest of people
        '''
        all_articles = self.newsapi.get_everything(
            qintitle=self._intrest,
            from_param=self._from_date,
            to=self._to_date,
            language=self._lang,
            sort_by='relevancy')

        articles = all_articles['articles']
        single_string = ''

        for article in articles:
            article_title = articles['title']
            article_url = article['url']
            single_string += article_title + '\n' + article_url + '\n\n'

        return single_string

    def get10(self):
        '''
        Not to get full bucket load of news stuff
        '''
        all_articles = self.newsapi.get_everything(
            qintitle=self._intrest,
            from_param=self._from_date,
            to=self._to_date,
            language=self._lang,
            sort_by='relevancy')

        articles = all_articles['articles']
        single_string = ''

        for i, article in enumerate(articles):
            if i >= 10:
                break
            article_title = article['title']
            article_url = article['url']
            single_string += article_title + '\n' + article_url + '\n\n'

        return single_string


if __name__ == '__main__':
    # Only to test out code
    today = date.today()
    news_feed = NewsFeed(
        intrest='bitcoin',
        from_date=f'{today.year}-{today.month}-{int(today.day) - 1}',
        to_date=str(today),
        language='en')

with open('test.txt', mode='w') as file:
    file.write(news_feed.get10())
