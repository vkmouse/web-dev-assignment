from urllib import request
from bs4 import BeautifulSoup

def getPage(url):
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    headers = {'User-Agent': userAgent}
    req = request.Request(url, headers=headers)
    with request.urlopen(req) as response:
        return response.read().decode('utf-8')

def getPreviousPageUrl(page):
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.find_all('a')
    link = list(filter(lambda link: link.string == '‹ 上頁', links))[0]
    return 'https://www.ptt.cc' + link.get('href')

def getTitles(page):
    soup = BeautifulSoup(page, 'html.parser')
    titleDivs = soup.find_all('div', class_='title')
    titles = map(lambda element: element.find('a'), titleDivs)
    titles = filter(lambda element: element != None, titles)
    titles = map(lambda element: element.string, titles)
    return list(titles)

def validatePrefix(title):
    substr = title[0:4]
    if substr == '[好雷]':
        return 0
    elif substr == '[普雷]':
        return 1
    elif substr == '[負雷]':
        return 2
    else:
        return -1
