function handleQueryMemberName() {
    const inputElement = document.getElementById('query_member_name_input')
    const outputElement = document.getElementById('query_member_name_output')
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

function handleUpdateName() {
    const inputElement = document.getElementById('update_name_input')
    const outputElement = document.getElementById('update_name_output')
    const newName = inputElement.value
    fetch('/api/member', { 
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'name': newName }),
    })
    .then(response => response.json())
    .then(body => {
        if (body.ok) {
            outputElement.textContent = '更新成功'
        }
    })
}
