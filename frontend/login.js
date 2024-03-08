let form = document.getElementById('login--form')

form.addEventListener('submit', (e) =>{
    e.preventDefault()
    console.log('Form Submitted')

    let formdata = {
        'username':form.username.value,
        'password':form.password.value
    }

    // console.log(formdata)
    fetch('http://127.0.0.1:8000/api/users/token/', {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
        },
        body:JSON.stringify(formdata)
    })
    .then(response => response.json())
    .then(data => {
        // console.log(data)
        if(data.access){
            localStorage.setItem('token', data.access)
            window.location = 'project-list.html'
        }
        else{
            alert('Username or Password didnt Work')
        }
    })
})