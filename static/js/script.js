// Add hide class to all publications
function addHideClass(){
    let allPublications = document.getElementsByClassName('publications');
    for (let publication of allPublications){
        publication.classList.add('hide');
    }
}

// Remove hide class from all publication
function removeHideClass(){
    let allPublications = document.getElementsByClassName('publications');
    for (let publication of allPublications){
        if(publication.classList.contains('hide')){
            publication.classList.remove('hide');
        }
    }
}

// Remove hide class only for those who match the filter
function showFilteredPublications(value){
    let filteredPublications = document.querySelectorAll('[data-type="'+value+'"]');
    for (let publication of filteredPublications){
        publication.classList.remove('hide');
    }
}

// Remove checked from all inputs
function clearInputs(){
    let allInputs = document.querySelectorAll('input[name="job_types"]');
    for (let input of allInputs){
        input.checked=false;
    }
}

// Add checked back to the chosen input
function checkInput(value){
    let input = document.querySelector('input[value="'+value+'"]');
    input.checked=true;
}

// Add opacity class to not selected inputs labels
function addOpacityClass(){
    let allInputs = document.querySelectorAll('input[name="job_types"');
    for (let input of allInputs){
        if(input.checked == false){
            input.previousElementSibling.classList.add('opacity');
        }
    }
}

// Remove opacity class from all input labels
function removeOpacityClass(){
    let allLabels = document.getElementsByTagName('label');
    for(let label of allLabels){
        if(label.classList.contains('opacity')){
            label.classList.remove('opacity');
        }
    }
}

// Main filter function
function jobFilter(value){
    let firstTimeClicked = document.querySelector('input[value="'+value+'"]').checked;
    
    if(firstTimeClicked){
        clearInputs();
        checkInput(value);
        addHideClass();
        removeOpacityClass();
        addOpacityClass();
        showFilteredPublications(value);
    }else{
        removeHideClass();
        removeOpacityClass();
    }
}