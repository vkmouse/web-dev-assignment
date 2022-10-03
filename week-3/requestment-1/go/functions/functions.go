package functions

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
	"strings"
)

func GetResults() []Result {
	url := "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	var obj map[string]json.RawMessage
	var result map[string]json.RawMessage
	var results []Result
	json.Unmarshal(body, &obj)
	json.Unmarshal(obj["result"], &result)
	json.Unmarshal(result["results"], &results)

	return results
}

func ParseRegionFromAddress(address string) string {
	return address[11:20] // 英文字母為 1 byte，中文字為 3 byte
}

func ParseFileToFiles(file string) []string {
	results := strings.Split(file, "https")[1:]
	for i, result := range results {
		results[i] = "https" + result
	}
	return results
}

func CheckPostDateAfterSpecificYear(postDate string, year int) bool {
	i, _ := strconv.Atoi(postDate[0:4])
	return i >= year
}

func CheckRegionInAcceptableRegions(region string, acceptableRegions []string) bool {
	return includes(region, acceptableRegions)
}

func CheckImgUrl(url string) bool {
	strs := strings.Split(url, ".")
	ext := strs[len(strs)-1]
	ext = strings.ToLower(ext)
	return (ext == "bmp" ||
		ext == "jpg" ||
		ext == "png")
}

func ConvertResultToRow(result Result) []string {
	title := result.Stitle
	region := ParseRegionFromAddress(result.Address)
	longitude := result.Longitude
	latitude := result.Latitude
	files := ParseFileToFiles(result.File)
	var imgUrls []string
	for _, file := range files {
		isImgUrl := CheckImgUrl(file)
		if isImgUrl {
			imgUrls = append(imgUrls, file)
		}
	}
	return []string{title, region, longitude, latitude, imgUrls[0]}
}

func includes(element string, elements []string) bool {
	for _, current := range elements {
		if current == element {
			return true
		}
	}
	return false
}
