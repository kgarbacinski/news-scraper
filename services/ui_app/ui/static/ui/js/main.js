/**
 * @fileoverview
 * Script to interact with scraper-app and get scraped content.
 * Also reads the auth_token from Django rendered view and set it to localStorage to reuse by history-app
 */

document.addEventListener("DOMContentLoaded", function () {

    const csrfToken = generateCookie('csrftoken');
    const contentDiv = document.getElementById('scraped_content');
    const form = document.getElementById('form');
    const input = document.getElementById('keyword')

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
     * @param {str} keyword
     * Takes keyword and calls scraper-app to start scraping process
     * @returns {str} task_id
     */
    async function insertTask(keyword) {
        const endpoint = `${window.location.protocol}//${window.location.hostname}:8004/new_task/${keyword}`;
        let data = await fetcher(endpoint);

        console.log('task added!');
        return data['task_id']
    }

      /**
     * @function
     * @param {str} task_id
     * Takes task_id and checks task_status each 500ms.
     * If task is ready and data available starts content handling.
     * If not, renders waiting spinner.
     */
    function getContent(task_id) {
        addWaitingMessage();

        setTimeout(async function () {
            let url = `${window.location.protocol}//${window.location.hostname}:8004/tasks/${task_id}`
            let response = await fetcher(url);
            let task_status = response.task_status;
            let content = response.content;

            if (task_status == 'SUCCESS') {
                clearContent();
                console.log('Data is ready!');
                renderContent(content);
                return
            } else {
                console.log('Checking for data...');
            }
            getContent(task_id);
        }, 500)
    }

    /**
     * @function
     * @param {json} data
     * Takes json object with articles and renders it to Django view.
     */
    function renderContent(data) {
        let content = data.articles;
        let query = data.keyword;

        for (key in content) {
            contentDiv.innerHTML += `
            <div class='source'>
                <span class='source_header'>${key.toUpperCase()}: <span class='color'>${content[key].length}</span></span>
            </div>
            `

            for (i = 0; i < content[key].length; i++) {
                let title = content[key][i][0];
                let link = content[key][i][1];

                contentDiv.innerHTML += `
                <div class='content_row'>
                    <span class='article_title'>${title}</span> - <a class='article_link' href='${link} target='_blank'>more</a>
                </div>
                `
            }
        }
    }

    /**
     * @function
     * clear the content from template
     */
    function clearContent() {
        contentDiv.innerHTML = '';
    }

    /**
     * @function
     * renders waiting spinner
     */
    function addWaitingMessage() {
        contentDiv.innerHTML = "<div class='loader'>fetching....</div>";
    }

    /**
     * @function
     * on form submit checks if input is passed.
     * if yes calls startScraping function to send task_id to scraper-app backend.
     */
    function runQuery() {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            clearContent();

            if (input.value.length > 0) {
                const keyword = input.value;
                console.log(`input: ${keyword}`);
                startScraping(keyword);
            } else {
                input.placeholder = 'Add something!'
            }
        })

    }

    /**
     * @function
     * @param {str} keyword
     * Takes keyword generated added by user
     * Sends GET call to scraper-app/new_task/{keyword} to get task_id
     * Calls getContent
     */
    async function startScraping(keyword) {
        let task_id = await insertTask(keyword);
        return getContent(task_id);
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
    };

    /**
     * @function
     * reads generated auth_token from tokenization-app set by Django view here:
     * https://github.com/dyeroshenko/news-scraper/blob/535bcc027309aca4a539d39f96668ba0776e9615/services/ui_app/ui/templates/ui/main.html#L6
     */
    function readAPITokenFromLocalStorage() {
        token = window.localStorage.getItem('auth_token');
        return token
    }

    runQuery();
});
