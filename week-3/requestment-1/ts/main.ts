import { 
  getResults, 
  checkPostDateAfterSpecificYear,
  convertResultToRow,
  checkRegionInAcceptableRegions
} from './functions/functions'
import * as fs from 'node:fs/promises';

const filename = 'data.csv'
const minYear = 2015
const acceptableRegions = ['中正區', '萬華區', '中山區', '大同區', '大安區',
                           '松山區', '信義區', '士林區', '文山區', '北投區',
                           '內湖區', '南港區']

getResults().then(results => {
  const rows = results
    .filter(result => checkPostDateAfterSpecificYear(result['xpostDate'], minYear))
    .map(result => convertResultToRow(result))
    .filter(row => checkRegionInAcceptableRegions(row[1], acceptableRegions))
  
  let content = ''
  for (const row of rows) {
    for (const element of row.slice(0, -1))
      content += element + ','
    content += row.slice(-1) + '\n'
  }
  
  fs.writeFile(filename, content)
})
