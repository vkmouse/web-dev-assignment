package functions

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGetResult(t *testing.T) {
	results := GetResults()
	assert.Equal(t, len(results), 58)
}

func TestParseRegionFromAddress(t *testing.T) {
	address := "臺北市  北投區中山路、光明路沿線"
	region := ParseRegionFromAddress(address)
	fmt.Print(region)
	assert.Equal(t, region, "北投區")
}

func TestParseFileToFiles(t *testing.T) {
	var file string
	file += "https://www.travel.taipei/pic/11000848.jpg"
	file += "https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3"
	files := ParseFileToFiles(file)
	assert.Equal(t, len(files), 2)
	assert.Equal(t, files[0], "https://www.travel.taipei/pic/11000848.jpg")
	assert.Equal(t, files[1], "https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3")
}

func TestCheckPostDateAfterSpecificYear(t *testing.T) {
	assert.True(t, CheckPostDateAfterSpecificYear("2016/07/07", 2015))
	assert.True(t, CheckPostDateAfterSpecificYear("2016/07/07", 2016))
	assert.False(t, CheckPostDateAfterSpecificYear("2016/07/07", 2017))
}

func TestCheckRegionInAcceptableRegions(t *testing.T) {
	assert.True(t, CheckRegionInAcceptableRegions("文山區", []string{"文山區", "內湖區"}))
	assert.False(t, CheckRegionInAcceptableRegions("文山區", []string{"信義區", "內湖區"}))
}

func TestCheckImgUrl(t *testing.T) {
	assert.True(t, CheckImgUrl("https://www.travel.taipei/pic/11000848.bmp"))
	assert.True(t, CheckImgUrl("https://www.travel.taipei/pic/11000848.jpg"))
	assert.True(t, CheckImgUrl("https://www.travel.taipei/pic/11000848.png"))
	assert.True(t, CheckImgUrl("https://www.travel.taipei/pic/11000848.BMP"))
	assert.True(t, CheckImgUrl("https://www.travel.taipei/pic/11000848.JPG"))
	assert.True(t, CheckImgUrl("https://www.travel.taipei/pic/11000848.PNG"))
	assert.False(t, CheckImgUrl("https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3"))
}

func TestConvertResultToRow(t *testing.T) {
	result := Result{
		Info:      "...",
		Stitle:    "新北投溫泉區",
		XpostDate: "2016/07/07",
		Longitude: "121.508447",
		REF_WP:    "10",
		AvBegin:   "2010/02/14",
		Langinfo:  "10",
		MRT:       "新北投",
		SERIAL_NO: "2011051800000061",
		RowNumber: "1",
		CAT1:      "景點",
		CAT2:      "養生溫泉",
		MEMO_TIME: "各業者不同，依據現場公告",
		POI:       "Y",
		File:      "",
		Idpt:      "臺北旅遊網",
		Latitude:  "25.137077",
		Xbody:     "...",
		Id:        1,
		AvEnd:     "2016/07/07",
		Address:   "臺北市  北投區中山路、光明路沿線",
	}
	result.File += "https://www.travel.taipei/pic/11000848.jpg"
	result.File += "https://www.travel.taipei/streams/sceneadmin/video/100C1.mp3"

	expected := []string{"新北投溫泉區", "北投區", "121.508447", "25.137077", "https://www.travel.taipei/pic/11000848.jpg"}
	actual := ConvertResultToRow(result)
	assert.Equal(t, expected, actual)
}
