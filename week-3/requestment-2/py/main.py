from functions import *

numPages = 10
url = 'https://www.ptt.cc/bbs/movie/index.html'

categories = [[], [], []]
for i in range(numPages):
    page = getPage(url)
    url = getPreviousPageUrl(page)
    titles = getTitles(page)
    for title in titles:
        index = validatePrefix(title)
        if index >= 0:
            categories[index].append(title)

with open('movie.txt', 'w', encoding='utf-8') as f:
    for category in categories:
        for title in category:
            f.write(f'{title}\n')
