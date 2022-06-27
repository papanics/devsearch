let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault() // avoid the page to refresh when hitting the submit.
    
    let formData = {
        'username':form.username.value,
        'password':form.password.value
    }

    fetch('http://127.0.0.1:8000/api/users/token/', {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:JSON.stringify(formData)
    })
    .then(response => response.json()) // promise
    .then(data => {                     // another promise
        console.log('DATA:', data.access)
        if(data.access){
            localStorage.setItem('token', data.access) // save token to the local storage
            window.location = 'file:///C:/Users/ntuban/Desktop/Prog_Courses/Dev_search/frontend/projects-list.html' // redirect to this page if authentication is valid.
        } else{
            alert('Username or password did not work')
        }
    })
})