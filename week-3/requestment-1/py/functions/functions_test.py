from functions import *
import unittest

class TestFunctions(unittest.TestCase):
    def testGetData(self):
        results = getResults()
        self.assertEqual(58, len(results))

    def testParseRegionFromAddress(self):
        address = '臺北市  北投區中山路、光明路沿線'
        region = parseRegionFromAddress(address)
        self.assertEqual('北投區', region)

    def testParseFileToFiles(self):
        file = ''
        file += 'https://www.travel.taipei/pic/11000848.jpg'
        file += 'https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3'
        files = parseFileToFiles(file)
        self.assertEqual(2, len(files))
        self.assertEqual('https://www.travel.taipei/pic/11000848.jpg', files[0])
        self.assertEqual('https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3', files[1])
    
    def testCheckPostDateAfterSpecificYear(self):
        self.assertTrue(checkPostDateAfterSpecificYear('2016/07/07', 2015))
        self.assertTrue(checkPostDateAfterSpecificYear('2016/07/07', 2016))
        self.assertFalse(checkPostDateAfterSpecificYear('2016/07/07', 2017))

    def testCheckRegionInAcceptableRegions(self):
        self.assertTrue(checkRegionInAcceptableRegions('文山區', ['文山區', '內湖區']))
        self.assertFalse(checkRegionInAcceptableRegions('文山區', ['信義區', '內湖區']))

    def testCheckImgUrl(self):
        self.assertTrue(checkImgUrl('https://www.travel.taipei/pic/11000848.bmp'))
        self.assertTrue(checkImgUrl('https://www.travel.taipei/pic/11000848.jpg'))
        self.assertTrue(checkImgUrl('https://www.travel.taipei/pic/11000848.png'))
        self.assertTrue(checkImgUrl('https://www.travel.taipei/pic/11000848.BMP'))
        self.assertTrue(checkImgUrl('https://www.travel.taipei/pic/11000848.JPG'))
        self.assertTrue(checkImgUrl('https://www.travel.taipei/pic/11000848.PNG'))
        self.assertFalse(checkImgUrl('https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3'))

    def testConvertResultToRow(self):
        result = {}
        result['info'] = '...'
        result['stitle'] = '新北投溫泉區'
        result['xpostDate'] = '2016/07/07'
        result['longitude'] = '121.508447'
        result['REF_WP'] = '10'
        result['avBegin'] = '2010/02/14'
        result['langinfo'] = '10'
        result['MRT'] = '新北投'
        result['SERIAL_NO'] = '2011051800000061'
        result['RowNumber'] = '1'
        result['CAT1'] = '景點'
        result['CAT2'] = '養生溫泉'
        result['MEMO_TIME'] = '各業者不同，依據現場公告'
        result['POI'] = 'Y'
        result['file'] = ''
        result['file'] += 'https://www.travel.taipei/pic/11000848.jpg'
        result['file'] += 'https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3'
        result['idpt'] = '臺北旅遊網'
        result['latitude'] = '25.137077'
        result['xbody'] = '...'
        result['_id'] = 1
        result['avEnd'] = '2016/07/07'
        result['address'] = '臺北市  北投區中山路、光明路沿線'

        expected = ['新北投溫泉區', '北投區', '121.508447', '25.137077', 'https://www.travel.taipei/pic/11000848.jpg']
        actual = convertResultToRow(result)
        self.assertEqual(expected, actual)