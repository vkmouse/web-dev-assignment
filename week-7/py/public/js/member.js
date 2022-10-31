function handleQueryMemberName() {
    const inputElement = document.getElementById('query_member_name_input') // value
    const outputElement = document.getElementById('query_member_name_output') // textContent
    const username = inputElement.value
    fetch(`/api/member?username=${username}`)
    .then(response => response.json())
    .then(body => {
        let output = ''
        if (body.data !== null) {
            output = `${body.data.name} (${body.data.username})`
        }
        outputElement.textContent = output
    })
}