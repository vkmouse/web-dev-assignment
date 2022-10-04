import { 
  getPage,
  getPreviousPageUrl, 
  getTitles,
  validatePrefix
} from './functions/functions'
import * as fs from 'node:fs/promises';

const numPages = 10
let url = 'https://www.ptt.cc/bbs/movie/index.html'

async function parsePage(numPages: number, url: string, categories: string[][], index: number) {
  if (numPages <= index) {
    let content = ''
    for (const category of categories) {
      for (const title of category) {
        content += `${title}\n`
      }
    }
    fs.writeFile('movie.txt', content)
    return
  }
  getPage(url).then(page => {
    url = getPreviousPageUrl(page)
    const titles = getTitles(page)
    for (const title of titles) {
      const i = validatePrefix(title)
      if (i >= 0) {
        categories[i].push(title)
      }
    }
  }).then(() => parsePage(numPages, url, categories, index + 1))
}

const categories: string[][] = [[], [], []]
parsePage(numPages, url, categories, 0)