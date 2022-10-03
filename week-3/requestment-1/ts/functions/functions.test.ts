import { 
  getResults, 
  parseRegionFromAddress, 
  parseFileToFiles, 
  checkPostDateAfterSpecificYear,
  checkRegionInAcceptableRegions,
  checkImgUrl,
  convertResultToRow 
} from './functions'
import { Result } from './types'

test('lenght of results is 58', async () => {
  return getResults().then(results => {
    expect(results.length).toBe(58)
  })
})

test('parse region from address', () => {
  const address = '臺北市  北投區中山路、光明路沿線'
  const region = parseRegionFromAddress(address)
  expect(region).toBe('北投區');
})

test('parse file to files', () => {
  let file = ''
  file += 'https://www.travel.taipei/pic/11000848.jpg'
  file += 'https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3'
  const files = parseFileToFiles(file)
  expect(files.length).toBe(2)
  expect(files[0]).toBe('https://www.travel.taipei/pic/11000848.jpg')
  expect(files[1]).toBe('https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3')
})

test('check post date after specific year', () => {
  expect(checkPostDateAfterSpecificYear('2016/07/07', 2015)).toBeTruthy()
  expect(checkPostDateAfterSpecificYear('2016/07/07', 2016)).toBeTruthy()
  expect(checkPostDateAfterSpecificYear('2016/07/07', 2017)).toBeFalsy()
})

test('check region in acceptable regions', () => {
  expect(checkRegionInAcceptableRegions('文山區', ['文山區', '內湖區'])).toBeTruthy()
  expect(checkRegionInAcceptableRegions('文山區', ['信義區', '內湖區'])).toBeFalsy()
})

test('check img url', () => {
  expect(checkImgUrl('https://www.travel.taipei/pic/11000848.bmp')).toBeTruthy()
  expect(checkImgUrl('https://www.travel.taipei/pic/11000848.jpg')).toBeTruthy()
  expect(checkImgUrl('https://www.travel.taipei/pic/11000848.png')).toBeTruthy()
  expect(checkImgUrl('https://www.travel.taipei/pic/11000848.BMP')).toBeTruthy()
  expect(checkImgUrl('https://www.travel.taipei/pic/11000848.JPG')).toBeTruthy()
  expect(checkImgUrl('https://www.travel.taipei/pic/11000848.PNG')).toBeTruthy()
  expect(checkImgUrl('https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3')).toBeFalsy()
})

test('convert result to row', () => {
  const result: Result = {
    info: '...',
    stitle: '新北投溫泉區',
    xpostDate: '2016/07/07',
    longitude: '121.508447',
    REF_WP: '10',
    avBegin: '2010/02/14',
    langinfo: '10',
    MRT: '新北投',
    SERIAL_NO: '2011051800000061',
    RowNumber: '1',
    CAT1: '景點',
    CAT2: '養生溫泉',
    MEMO_TIME: '各業者不同，依據現場公告',
    POI: 'Y',
    file: '',
    idpt: '臺北旅遊網',
    latitude: '25.137077',
    xbody: '...',
    _id: 1,
    avEnd: '2016/07/07',
    address: '臺北市  北投區中山路、光明路沿線',
  }
  result.file += 'https://www.travel.taipei/pic/11000848.jpg'
  result.file += 'https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3'

  const expected = ['新北投溫泉區', '北投區', '121.508447', '25.137077', 'https://www.travel.taipei/pic/11000848.jpg']
  const actual = convertResultToRow(result)
  expect(actual).toStrictEqual(expected)
})