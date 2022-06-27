

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
    
    for (let i = 0; projects.length > i; i++) {
        let project = projects[i]

        let projectCard =  `
                <div class="project--card">
                    <img src="http://127.0.0.1:8000${project.feature_image}" />
                    
                    <div>
                        <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option">&#43;</strong>
                        <strong class="vote--option">&#8722;</strong>
                        </div>
                        <i>${project.vote_ratio}% Positive feedback </i>
                        <p>${project.description.substring(0, 150)}</p>
                    </div>

                </div>
        `
        projectsWrapper.innerHTML += projectCard
    }
} 

getProjects() //triggering this function.


//NOTES: CORS error --> meaning Cross-Origin Resource Sharing error.
// --> meaning we're trying to make this request, but it's not working.