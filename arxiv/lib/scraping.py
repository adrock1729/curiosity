from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs


def search(keyword="consciousness"):
    url = 'http://export.arxiv.org/api/' \
        'query?search_query=all:{}&start=0&max_results=15'\
        '&sortBy=submittedDate&sortOrder=descending'.format(keyword)
    req = Request(url=url)
    with urlopen(req) as res:
        xml = res.read().decode('utf-8')

    soup = bs(xml, 'lxml')
    entries = soup.find_all('entry')
    return entries
