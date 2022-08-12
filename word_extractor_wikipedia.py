import urllib.request as urllib2
import json
from datetime import datetime, timedelta

def main():

    TOP_API_URL = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/top-per-country/{lang}/all-access/{year}/{month}/{day}'

    def get_traffic(year, month, day):

        url = TOP_API_URL.format(lang='DE',
                                 year=year,
                                 month=month,
                                 day=day)
        
        resp = urllib2.urlopen(url)
        resp_bytes = resp.read()
    
        data = json.loads(resp_bytes)
        articles = data['items'][0]['articles']
        return articles

    
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    words = [ articles['article'] for articles in get_traffic(yesterday.year, '{:02d}'.format(yesterday.month), '{:02d}'.format(yesterday.day))]
    with open('hangman_words.txt', 'w') as f:
         f.write('\n'.join(words))
    print_info(words)


def print_info(words):
    print('Words in list:', len(words))
    longest_word = max(words, key=lambda word: len(word))
    print('Longest word:', longest_word, len(longest_word))
    shortest_word = min(words, key=lambda word: len(word))
    print('Shortest word:', shortest_word, len(shortest_word))


if __name__ == '__main__':
    main()
