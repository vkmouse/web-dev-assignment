package main

import (
	. "Project/functions"
	"fmt"
	"os"
)

func main() {
	filename := "data.csv"
	minYear := 2015
	acceptableRegions := []string{
		"中正區", "萬華區", "中山區", "大同區", "大安區",
		"松山區", "信義區", "士林區", "文山區", "北投區",
		"內湖區", "南港區"}
	results := GetResults()

	content := ""
	for _, result := range results {
		dateIsValid := CheckPostDateAfterSpecificYear(result.XpostDate, minYear)
		if dateIsValid {
			row := ConvertResultToRow(result)
			regionIsValid := CheckRegionInAcceptableRegions(row[1], acceptableRegions)
			lastIndex := len(row) - 1
			if regionIsValid {
				for _, element := range row[:lastIndex] {
					content += element + ","
				}
				content += row[lastIndex] + "\n"
			}
		}
	}

	fout, err := os.Create(filename)
	if err != nil {
		fmt.Println(filename, err)
		return
	}
	defer fout.Close()
	fout.WriteString(content)
}
