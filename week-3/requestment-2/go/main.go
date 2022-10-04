package main

import (
	. "Project/functions"
	"fmt"
	"os"
)

func main() {
	numPages := 10
	url := "https://www.ptt.cc/bbs/movie/index.html"

	categories := [][]string{{}, {}, {}}

	for i := 0; i < numPages; i++ {
		page := GetPage(url)
		url = GetPreviousPageUrl(page)
		titles := GetTitles(page)
		for _, title := range titles {
			index := ValidatePrefix(title)
			if index >= 0 {
				categories[index] = append(categories[index], title)
			}
		}
	}

	content := ""
	for _, category := range categories {
		for _, title := range category {
			content += title + "\n"
		}
	}

	fout, err := os.Create("movie.txt")
	if err != nil {
		fmt.Println("movie.txt", err)
		return
	}
	defer fout.Close()
	fout.WriteString(content)
}
