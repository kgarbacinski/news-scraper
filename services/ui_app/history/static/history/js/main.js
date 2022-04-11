document.addEventListener("DOMContentLoaded", function () {
    const csrfToken = generateCookie('csrftoken');
    const contentDiv = document.getElementById('content');

    async function fetcher(url) {
        let response = await fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrfToken,
                'Authorization': `Bearer ${readAPITokenFromLocalStorage()}`
            }
        })
        let result = await response.json();

        return result
    }

    async function getHistory() {
        const url = `${window.location.protocol}//${window.location.hostname}:8005/records`;
        let data = await fetcher(url);

        console.log('data loaded!')
        return data;
    }


    function renderHistory(data) {
        for (i = 0; i < data.length; i++) {
            let record = data[i];
            let content= record['content'];
            let timestamp = record['timestamp'];
            let backend_task_id = record['task_id'];
            let keyword = record['keyword'];

            contentDiv.innerHTML += `
                <li class='content_row'>
                    <span class='color'>${timestamp}</span> |
                    keyword: <span class='color'>${keyword}</span>: |
                    content: <span class='color'>${content}</span>:  |
                    task: <span class='color'>${backend_task_id}</span>
                </li>
            `
        }
    }

    async function main() {
        let data = await getHistory();
        renderHistory(data);
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
    }

    function readAPITokenFromLocalStorage() {
        token = window.localStorage.getItem('auth_token');

        return token
    }

    main();
});
