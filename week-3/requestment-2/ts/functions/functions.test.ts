import { 
  getPage,
  getPreviousPageUrl, 
  getTitles,
  validatePrefix
} from './functions'

const page = ` 
  <a class="btn wide" href="/bbs/movie/index9501.html">‹ 上頁</a>
  <div class="title">
    <a href="/bbs/movie/M.1664272810.A.ED2.html">[負雷] Ｎ号棟鬧鬼 BLDG. N</a>
  </div>
  <div class="title">
    <a href="/bbs/movie/M.1664272810.A.ED2.html">[好雷]復仇之淵 槍戰很爽</a>
  </div>
  <div class="title">
    <a href="/bbs/movie/M.1664272810.A.ED2.html">[普雷] 行動代號：狼狩獵（首映）</a>
  </div>
`

test('get page from movie bbs', async () => {
  const url = 'https://www.ptt.cc/bbs/movie/index.html'
  return getPage(url).then(page => {
    expect(page !== '').toBeTruthy()
  })
})

test('get previous page url', () => {
  const expected = 'https://www.ptt.cc/bbs/movie/index9501.html'
  const actual = getPreviousPageUrl(page)
  expect(actual).toBe(expected);
})

test('get titles  ', () => {
  const expected = [
    '[負雷] Ｎ号棟鬧鬼 BLDG. N',
    '[好雷]復仇之淵 槍戰很爽',
    '[普雷] 行動代號：狼狩獵（首映）'
  ]
  const actual = getTitles(page)
  expect(actual).toStrictEqual(expected);
})

test('validate prefix', () => {
  expect(validatePrefix('[好雷]復仇之淵 槍戰很爽')).toBe(0)
  expect(validatePrefix('[普雷] 行動代號：狼狩獵（首映）')).toBe(1)
  expect(validatePrefix('[負雷] Ｎ号棟鬧鬼 BLDG. N)')).toBe(2)
  expect(validatePrefix('[情報] 2022 第59屆金馬獎 入圍名單&入圍統計')).toBe(-1)
})
