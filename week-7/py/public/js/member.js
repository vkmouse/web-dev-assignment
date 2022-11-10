function handleQueryMemberName() {
    const username = document.getElementById('query_member_name_input').value
    fetch(`api/member?username=${username}`)
    .then(response => response.json())
    .then(body => displayMemberName(body))
}

async function displayMemberName(body) {
    let output = ''
    if (body.data !== null) {
        output = `${body.data.name} (${body.data.username})`
    }
    document.getElementById('query_member_name_output').textContent = output
}

function handleUpdateName() {
    const newName = document.getElementById('update_name_input').value
    fetch('api/member', { 
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'name': newName }),
    })
    .then(response => response.json())
    .then(body => updateName(body, newName))
}

async function updateName(body, newName) {
    if (body.ok) {
        document.getElementById('name').textContent = newName
        document.getElementById('update_name_output').textContent = '更新成功'
    }
}
