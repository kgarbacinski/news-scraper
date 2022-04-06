document.addEventListener("DOMContentLoaded", function () {

    const csrfToken = generateCookie('csrftoken');
    const contentDiv = document.getElementById('content');
    const keyword = 'war';


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
                contentDiv.textContent += content.keyword
                return
            } else {
                console.log('Checking for content...');
            }
            getContent(task_id);
        }, 100)
    }


    async function run(keyword) {
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


    run(keyword)
});