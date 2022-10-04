from functions import *
import unittest

class TestFunctions(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestFunctions, self).__init__(*args, **kwargs)
        self.page = '''
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
        '''

    def testGetPage(self):
        url = 'https://www.ptt.cc/bbs/movie/index.html'
        page = getPage(url)
        self.assertNotEqual('', page)

    def testGetPreviousPageUrl(self):
        expected = 'https://www.ptt.cc/bbs/movie/index9501.html'
        actual = getPreviousPageUrl(self.page)
        self.assertEqual(expected, actual)

    def testGetTitles(self):
        expected = [
            '[負雷] Ｎ号棟鬧鬼 BLDG. N',
            '[好雷]復仇之淵 槍戰很爽',
            '[普雷] 行動代號：狼狩獵（首映）'
        ]
        actual  = getTitles(self.page)
        self.assertEqual(expected, actual)

    def testValidatePrefix(self):
        self.assertEqual(validatePrefix('[好雷]復仇之淵 槍戰很爽'), 0)
        self.assertEqual(validatePrefix('[普雷] 行動代號：狼狩獵（首映）'), 1)
        self.assertEqual(validatePrefix('[負雷] Ｎ号棟鬧鬼 BLDG. N'), 2)
        self.assertEqual(validatePrefix('[情報] 2022 第59屆金馬獎 入圍名單&入圍統計'), -1)