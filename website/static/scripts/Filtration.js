function checkCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
      return parts.pop().split(";").shift();
    }
    return null;
}

function activeForm(id){
    document.getElementById(id).submit();
}

function loadActiveFormAfterLoad(id){
    let checkboxes = document.querySelectorAll('input[type="checkbox"]');
    let allChecked = false;
    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            allChecked = true;
            break;
        }
    }
    if(document.getElementsByName("dateTH")[0].value != "↕"){
        allChecked = true;
    }
    if(document.getElementsByName("languageTH")[0].value != "↕"){
        allChecked = true;
    }
    if(document.getElementsByName("intervalTH")[0].value != "↕"){
        allChecked = true;
    }
    if(document.getElementsByName("starsTH")[0].value != "↕"){
        allChecked = true;
    }
    if (allChecked == true) {
        document.getElementById(id).submit();
    }
}

function elementFiltrationChange(id){
    let checkbox = document.getElementById(id);
    if(checkbox.checked){
        document.getElementById("FormFiltration1").submit();
    }
}

