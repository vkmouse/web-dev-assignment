package functions

import (
	"io/ioutil"
	"log"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

func GetPage(url string) string {
	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	return string(body)
}

func GetPreviousPageUrl(page string) string {
	doc, err := goquery.NewDocumentFromReader(strings.NewReader(page))
	if err != nil {
		log.Fatal(err)
	}

	url := ""

	filterFunc := func(i int, s *goquery.Selection) bool {
		first := s.First()
		return first.Text() == "‹ 上頁"
	}

	eachFunc := func(i int, s *goquery.Selection) {
		first := s.First()
		val, _ := first.Attr("href")
		url = "https://www.ptt.cc" + val
	}

	doc.Find("a").FilterFunction(filterFunc).Each(eachFunc)

	return url
}

func GetTitles(page string) []string {
	doc, err := goquery.NewDocumentFromReader(strings.NewReader(page))
	if err != nil {
		log.Fatal(err)
	}

	var titles []string
	eachFunc := func(i int, s *goquery.Selection) {
		titles = append(titles, s.Text())
	}

	doc.Find("div").Filter(".title").Find("a").Each(eachFunc)

	return titles
}

func ValidatePrefix(title string) int {
	substr := title[0:8]
	if substr == "[好雷]" {
		return 0
	} else if substr == "[普雷]" {
		return 1
	} else if substr == "[負雷]" {
		return 2
	} else {
		return -1
	}
}
