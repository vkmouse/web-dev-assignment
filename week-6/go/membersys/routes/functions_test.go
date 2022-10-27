package routes

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCheckLogin(t *testing.T) {
	assert.True(t, CheckLogin("test", "test"))
	assert.False(t, CheckLogin("", ""))
	assert.False(t, CheckLogin("test", ""))
	assert.False(t, CheckLogin("", "test"))
	assert.False(t, CheckLogin("123", "456"))
}

func TestGetErrorMessage(t *testing.T) {
	assert.Equal(t, GetErrorMessage("", ""), "請輸入帳號、密碼")
	assert.Equal(t, GetErrorMessage("test", ""), "請輸入帳號、密碼")
	assert.Equal(t, GetErrorMessage("", "test"), "請輸入帳號、密碼")
	assert.Equal(t, GetErrorMessage("123", "456"), "帳號、或密碼輸入錯誤")
	assert.Equal(t, GetErrorMessage("test", "test"), "")
}
