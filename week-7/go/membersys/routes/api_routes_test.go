package routes

import (
	"encoding/json"
	"net/http/httptest"
	"net/url"
	"testing"

	"github.com/gin-gonic/gin"
	"github.com/stretchr/testify/assert"
)

func assertJSON(t *testing.T, w *httptest.ResponseRecorder, expected interface{}) {
	actual := expected
	json.Unmarshal(w.Body.Bytes(), &actual)
	assert.Equal(t, expected, actual)
}

func TestMemberQuerySuccess(t *testing.T) {
	router := setupRouter()
	data := url.Values{"username": {"test"}}
	w, _ := get(router, "/api/member", data, true)

	expected := map[string]interface{}{
		"data": map[string]interface{}{
			"id":       1.0,
			"name":     "test",
			"username": "test",
		},
	}
	assertJSON(t, w, expected)
	assertStatusOK(t, w)
}

func TestMemberQueryWithoutLogin(t *testing.T) {
	router := setupRouter()
	data := url.Values{"username": {"test"}}
	w, _ := get(router, "/api/member", data, false)

	expected := map[string]interface{}{
		"data": nil,
	}
	assertJSON(t, w, expected)
	assertStatusOK(t, w)
}

func TestMemberQueryFailed(t *testing.T) {
	router := setupRouter()
	data := url.Values{"username": {"123"}}
	w, _ := get(router, "/api/member", data, true)

	expected := map[string]interface{}{
		"data": nil,
	}
	assertJSON(t, w, expected)
	assertStatusOK(t, w)
}

func TestModifyMemberNameSuccess(t *testing.T) {
	router := setupRouter()
	data := gin.H{"name": "test123"}
	w, _ := patch(router, "/api/member", data, true)

	expected := map[string]interface{}{
		"ok": true,
	}
	assertJSON(t, w, expected)
	assertStatusOK(t, w)
}
