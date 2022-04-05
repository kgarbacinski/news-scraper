document.addEventListener("DOMContentLoaded", function() {
    console.log('dupa')
    insertTask()
})


const csrfToken = generateCookie('csrftoken')

async function insertTask() {
    let keyword = 'war'
    let endpoint = `http://scraper-app:8000/new_task/${keyword}`
    response = await fetch(endpoint, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfToken
        }
    })

    let data = await response.json()
    console.log(data)
}


function generateCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            };
        };
    };
    return cookieValue;
};
