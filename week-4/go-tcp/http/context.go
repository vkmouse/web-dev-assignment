package http

import (
	"strings"
)

func ParseRequest(req string) Context {
	lines := strings.Split(req, "\n")
	tokens := strings.Split(lines[0], " ")
	body := ""

	urlTokens := strings.Split(tokens[1], "?")
	requestedURL := urlTokens[0]
	queryString := ""
	if len(urlTokens) > 1 {
		if urlTokens[1] == "message=%E8%AB%8B%E8%BC%B8%E5%85%A5%E5%B8%B3%E8%99%9F%E3%80%81%E5%AF%86%E7%A2%BC" {
			queryString = "message=請輸入帳號、密碼"
		}
	}

	cookie := ""
	for _, line := range lines {
		if strings.Contains(line, "Cookie") {
			cookie = strings.Replace(line, "Cookie: ", "", -1)
			cookie = strings.Replace(line, "\r", "", -1)
		}
	}

	isBody := false
	for _, line := range lines {
		if isBody {
			body += line + "\n"
		}
		if line == "\r" {
			isBody = true
		}
	}

	return Context{
		Method:       tokens[0],
		RequestedURL: requestedURL,
		Body:         body,
		QueryString:  queryString,
		Cookie:       cookie,
	}
}
