let projectsUrl = 'http://127.0.0.1:8000/api/projects/'

//send the token in the header
let getProjects = () => {
    fetch(projectsUrl)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            buildProjects(data)
        })
}

let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('project--wrapper')
    // console.log('projectsWrapper:',projectsWrapper)
    for (let i = 0; i < projects.length; i++) {
        let project = projects[i]
        let projectCard = `
            <div class="project--card">
                <img src="http://localhost:8000/${project.featured_image}" />
                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
                        <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
                    </div>
                </div>
                <i>${project.vote_ratio}% Positive Feedback</i>
                <p>${project.description.substring(0,150)}</p>
            </div>
        `
        projectsWrapper.innerHTML += projectCard

    }

    //Add event listeners
    addVoteEvents()
}

let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option')
    // console.log('VOTE BUTTONS:',voteBtns)
    for(let i=0; voteBtns.length > i; i++) {
        voteBtns[i].addEventListener('click', (e)=>{
            // console.log('Vote was Clicked',i)
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            // console.log(vote +"   "+project)
            let token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5OTE1Mjc2LCJpYXQiOjE3MDk4Mjg4NzYsImp0aSI6ImEyMmY4OGE0NWFkOTQ0NjVhMWM3OTlhNDI4ODFkN2I2IiwidXNlcl9pZCI6MTV9.GZhXyTvStD1aaY6sU5kieQJRZ3bO56kxexgIS2Cvh-k'
            fetch(`http://localhost:8000/api/projects/${project}/vote/`, {
                method:'POST', 
                    headers:{ 'Content-Type':'application/json',
                              Authorization: `Bearer ${token}`
                    },
                    body:JSON.stringify({'value':vote})
                }
            )
            .then(response => response.json())
            .then(
                data => console.log('SUCCESS')
            )
        })
    }
}

getProjects()