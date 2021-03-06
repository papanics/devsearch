
let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if (token) {
    loginBtn.remove()
} else{
    logoutBtn.remove()
}


logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = 'file:///C:/Users/ntuban/Desktop/Prog_Courses/Dev_search/frontend/login.html'
})

let projectsUrl = 'http://127.0.0.1:8000/api/projects/'

let getProjects = () => { //make a request of the projects list

    fetch(projectsUrl) 
    .then(response => response.json() ) // this is a promise, it will wait to finish fetch or rendering or making a call before getting response. and then convert it to a json data
    .then(data => {
        console.log(data)
        buildProjects(data)
    })
}


//listing the projects
let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('projects--wrapper')
    projectsWrapper.innerHTML = '' //clear the projects
    for (let i = 0; projects.length > i; i++) {
        let project = projects[i]

        let projectCard =  `
                <div class="project--card">
                    <img src="http://127.0.0.1:8000${project.feature_image}" />
                    
                    <div>
                        <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong> 
                        <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
                        </div>
                        <i>${project.vote_ratio}% Positive feedback </i>
                        <p>${project.description.substring(0, 150)}</p>
                    </div>

                </div>
        `
        projectsWrapper.innerHTML += projectCard
    }

    //Add an event listener for click the vote
    addVoteEvent()
} 

let addVoteEvent = () => {
    let voteBtns = document.getElementsByClassName('vote--option')
    console.log('VOTE BUTTONS:', voteBtns)

    for (let i =0;  voteBtns.length > i; i++){
        voteBtns[i].addEventListener('click', (e) => {
            
            let token = localStorage.getItem('token')
            console.log('TOKEN:', token)

            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            

            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
                method:'POST', 
                headers:{
                    'Content-Type':'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({'value': vote}) 
            })
            .then(response => response.json())
            .then(data => {
                console.log('success:', data)
                getProjects()
            })
        })
    }
}

getProjects() //triggering this function.


//NOTES: CORS error --> meaning Cross-Origin Resource Sharing error.
// --> meaning we're trying to make this request, but it's not working.