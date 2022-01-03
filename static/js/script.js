function hideAll(){
    let publications = document.getElementsByClassName('publications');
    for (publication of publications){
        publication.classList.toggle('hide');
    }   
}

function showSelected(value){
    let selectedPublications = document.querySelectorAll('[data-type="'+value+'"]')
    for (publication of selectedPublications){
        publication.classList.toggle('hide'); 
    }
}

function jobFilter(value){
    hideAll()
    showSelected(value)
}