document.addEventListener("DOMContentLoaded", function () {

    const csrfToken = generateCookie('csrftoken');
    const contentDiv = document.getElementById('scraped_content');
    const form = document.getElementById('form');
    const input = document.getElementById('keyword')


    async function insertTask(keyword) {
        const endpoint = `${window.location.protocol}//${window.location.hostname}:8004/new_task/${keyword}`;
        let response = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrfToken
            }
        });
        let data = await response.json();

        console.log('task added!');
        return data['task_id'];
    }

    async function fetchData(url) {
        let response = await fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrfToken
            }
        })
        let result = await response.json()
        return result
    }

    function getContent(task_id) {
        setTimeout(async function () {
            let url = `${window.location.protocol}//${window.location.hostname}:8004/tasks/${task_id}`
            let response = await fetchData(url);
            let task_status = response.task_status;
            let content = response.content;

            if (task_status == 'SUCCESS') {
                console.log('Content is ready!');
                console.log(content);
                renderContent(content);
                return
            } else {
                console.log('Checking for content...');
            }
            getContent(task_id);
        }, 100)
    }

    function renderContent(data) {
        let content = data.articles;
        let query = data.keyword;
        
        for (key in content) {
            let articles_array = content[key]

            for (i = 0; i < articles_array.length; i++) {
                let title = articles_array[i][0];
                let link = articles_array[i][1];

                contentDiv.innerHTML += `
                <div class='source_data'>
                    <span class='source_header'>${key.toUpperCase()} | ${articles_array.length}</span>
                    <ul>
                        <li><span class='article_title'>${title}</span>: <a href='${link}' target='_blank'>more</a></li>
                    </ul>
                </div>
                `
            }
        }
    }

    function removeContent() {
        contentDiv.innerHTML = '';
    }

    function runQuery() {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            removeContent();

            const keyword = input.value;
            console.log(`input: ${keyword}`);

            startScraping(keyword);
        })
        
    }

    async function startScraping(keyword) {
        let task_id = await insertTask(keyword);
        getContent(task_id);
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


    runQuery();
});