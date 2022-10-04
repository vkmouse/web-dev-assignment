import fetch, { Headers } from 'node-fetch'
import { parse } from 'node-html-parser'

export function getPage(url: string): Promise<string> {
  const headers = new Headers({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
  });
  const options = { 
    method: 'GET', 
    headers: headers
  }
  return fetch(url, options)
    .then(response => response.text())
}

export function getPreviousPageUrl(page: string): string {
  const root = parse(page);
  const links = root.getElementsByTagName('a')
  const link = links.filter(link => link.textContent === '‹ 上頁')[0]
  return 'https://www.ptt.cc' + link.getAttribute('href')
}

export function getTitles(page: string): string[] {
  const root = parse(page);
  const divs = root.getElementsByTagName('div')
  const titleDivs = divs.filter(div => div.classList.contains('title'))
  const titles = titleDivs
    .map(div => div.getElementsByTagName('a'))
    .filter(links => links.length !== 0)
    .map(links => links[0].textContent)
  return titles
}

export function validatePrefix(title: string): number {
    const substr = title.slice(0, 4)
    if (substr === '[好雷]') {
      return 0
    } else if (substr == '[普雷]') {
      return 1
    } else if (substr == '[負雷]') {
      return 2
    } else {
      return -1
    }
}
