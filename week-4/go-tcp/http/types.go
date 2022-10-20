package http

type Context struct {
	Method       string
	RequestedURL string
	Body         string
	QueryString  string
	Cookie       string
}
