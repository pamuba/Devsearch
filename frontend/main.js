let loginBtn = document.getElementById('login--btn')
let logoutBtn = document.getElementById('logout--btn')

let token = localStorage.getItem('token')
if(token){
    loginBtn.remove()
}
else{
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e)=>{

    e.preventDefault()
    localStorage.removeItem('token');
    window.location = 'login.html'
})

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
    projectsWrapper.innerHTML = ''
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
            e.preventDefault()
            // console.log('Vote was Clicked',i)
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            // console.log(vote +"   "+project)
            // Step 1
            let token = localStorage.getItem('token')
            console.log('TOKEN:', token)
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
                data => console.log('SUCCESS:', data),
                getProjects()
            )
        })
    }
}

getProjects()