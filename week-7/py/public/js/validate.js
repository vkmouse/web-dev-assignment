function handlePasswordValidation(inputElement) {
  if (inputElement.validity.patternMismatch) {
    inputElement.setCustomValidity('請輸入 4 ~ 100 個字元的英文字母、數字\n至少包含 1 英文字母')
  } else {
    inputElement.setCustomValidity('')
  }
}

function handleUsernameValidation(inputElement) {
  if (inputElement.validity.patternMismatch) {
    inputElement.setCustomValidity('請輸入 4 ~ 30 個字元的英文字母、數字、半形句號')
  } else {
    inputElement.setCustomValidity('')
  }
}
