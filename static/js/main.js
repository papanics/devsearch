
        // get seact form and page links
        let searchForm = document.getElementById('searchForm')
        let pageLinks = document.getElementsByClassName('page-link')

        //ensure searchform exists
        if(searchForm){
            for(let i=0; pageLinks.length > i; i++) {
                pageLinks[i].addEventListener('click', function (e) {
                    e.preventDefault()
                    // get the data attribute
                    let page = this.dataset.page
                    //add hidden search input to form
                    searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

                    
                    //SUBMIT FORM
                    searchForm.submit()
                })
            }
        }

