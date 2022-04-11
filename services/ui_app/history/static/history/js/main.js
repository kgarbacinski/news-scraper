/**
 * @fileoverview
 * Script to fetch & render content from history-app.
 */

document.addEventListener("DOMContentLoaded", function () {
    const csrfToken = generateCookie('csrftoken');
    const contentDiv = document.getElementById('content');

    /**
     * @function
     * @param {str} url
     * Makes GET request to specified URL and returns json content
     * Uses customized 'Authorization' header to get through auth validation
     */
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


    /**
     * @function
     * Calls history-app endpoint and returns available records
     * @returns {json} data
     */
    async function getHistory() {
        const url = `${window.location.protocol}//${window.location.hostname}:8005/records`;
        let data = await fetcher(url);

        console.log('data loaded!')
        return data;
    }

    /**
     * @function
     * @param {json} data
     * Takes json object with records and renders it to Django view.
     */
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

    /**
     * @function
     * Calls the data and runs rendering
     */
    async function main() {
        let data = await getHistory();
        renderHistory(data);
    }

    /**
     * @function
     * @param {str} name
     * @returns str
     * Supportive function to generate cookie to avoid CSRF errors.
     */
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

    /**
     * @function
     * reads generated auth_token from tokenization-app set by Django view here:
     * https://github.com/dyeroshenko/news-scraper/blob/535bcc027309aca4a539d39f96668ba0776e9615/services/ui_app/ui/templates/ui/main.html#L6
     */
    function readAPITokenFromLocalStorage() {
        token = window.localStorage.getItem('auth_token');
        return token
    }

    main();
});
