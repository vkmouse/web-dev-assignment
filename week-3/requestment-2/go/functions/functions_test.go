package functions

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func page() string {
	p := ""
	p += "<a class=\"btn wide\" href=\"/bbs/movie/index9501.html\">‹ 上頁</a>\n"
	p += "<div class=\"title\">\n"
	p += "  <a href=\"/bbs/movie/M.1664272810.A.ED2.html\">[負雷] Ｎ号棟鬧鬼 BLDG. N</a>\n"
	p += "</div>\n"
	p += "<div class=\"title\">\n"
	p += "  <a href=\"/bbs/movie/M.1664272810.A.ED2.html\">[好雷]復仇之淵 槍戰很爽</a>\n"
	p += "</div>\n"
	p += "<div class=\"title\">\n"
	p += "  <a href=\"/bbs/movie/M.1664272810.A.ED2.html\">[普雷] 行動代號：狼狩獵（首映）</a>\n"
	p += "</div>\n"
	return p
}

func TestGetResult(t *testing.T) {
	url := "https://www.ptt.cc/bbs/movie/index.html"
	page := GetPage(url)
	assert.NotEqual(t, "", page)
}

func TestGetPreviousPageUrl(t *testing.T) {
	expected := "https://www.ptt.cc/bbs/movie/index9501.html"
	actual := GetPreviousPageUrl(page())
	assert.Equal(t, expected, actual)
}

func TestGetTitles(t *testing.T) {
	expected := []string{
		"[負雷] Ｎ号棟鬧鬼 BLDG. N",
		"[好雷]復仇之淵 槍戰很爽",
		"[普雷] 行動代號：狼狩獵（首映）",
	}
	actual := GetTitles(page())
	assert.Equal(t, expected, actual)
}

func TestValidatePrefix(t *testing.T) {
	assert.Equal(t, ValidatePrefix("[好雷]復仇之淵 槍戰很爽"), 0)
	assert.Equal(t, ValidatePrefix("[普雷] 行動代號：狼狩獵（首映）"), 1)
	assert.Equal(t, ValidatePrefix("[負雷] Ｎ号棟鬧鬼 BLDG. N)"), 2)
	assert.Equal(t, ValidatePrefix("[情報] 2022 第59屆金馬獎 入圍名單&入圍統計"), -1)
}
