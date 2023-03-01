function checkCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
      return parts.pop().split(";").shift();
    }
    return null;
  }

function Checked(x){
    for(var i = 1; i <= 5;i++){
        var id = 'FiltrationRadio' + (6-i) + x;
        if(document.getElementById(id).checked == true){
            return id;
        }
    }
}

function loadCookiesForCheckboxes(userId){
    const CheckDate = document.getElementById("CheckDate");
    const CheckInterval = document.getElementById("CheckInterval");
    const CheckLanguages = document.getElementById("CheckLanguages");
    const CheckStars = document.getElementById("CheckStars");

    let date1 = checkCookie("CheckDate");
    let interval1 = checkCookie("CheckInterval");
    let language1 = checkCookie("CheckLanguages");
    let stars1 = checkCookie("CheckStars");

    if (date1 === undefined) {
        CheckDate.checked = false;
        document.cookie = `CheckDate=false;`;
    } 
    else {
        CheckDate.checked = (date1 === "true");
    }

    if (interval1 === undefined) {
        CheckInterval.checked = false;
        document.cookie = `CheckInterval=false;`;
    } 
    else {
        CheckInterval.checked = (interval1 === "true");
    }

    if (language1 === undefined) {
        CheckLanguages.checked = false;
        document.cookie = `CheckLanguages=false;`;
    } 
    else {
        CheckLanguages.checked = (language1 === "true");
    }

    if (stars1 === undefined) {
        CheckStars.checked = false;
        document.cookie = `CheckStars=false;`;
    } 
    else {
        CheckStars.checked = (stars1 === "true");
    }
    
    
}

// DODĚLAT PRO VÝBĚR JAZYKA !!!!!!!!!
function loadCookies(userId){
    const FiltrationDate1 = document.getElementById("FiltrationDate1");
    const FiltrationDate2 = document.getElementById("FiltrationDate2");

    const FiltrationInterval1 = document.getElementById("FiltrationInterval1");
    const FiltrationInterval2 = document.getElementById("FiltrationInterval2");

    const FiltrationLanguages1 = document.getElementById("FiltrationLanguages1");
    
    let options = FiltrationLanguages1.options;


    let date1 = checkCookie("FiltrationDate1");
    let date2 = checkCookie("FiltrationDate2");

    let interval1 = checkCookie("FiltrationInterval1");
    let interval2 = checkCookie("FiltrationInterval2");

    let languages1 = checkCookie("FiltrationLanguages1");

    let stars1 = checkCookie("FiltrationStarsA");
    let stars2 = checkCookie("FiltrationStarsB");

    // Začátek Datumu
    if (date1) {
        FiltrationDate1.value = date1;
    } 
    else {
        FiltrationDate1.value = "2022-01-01";
        document.cookie = `FiltrationDate1=2022-01-01;`;
    }

    if (date2) {
        FiltrationDate2.value = date2;
    } 
    else {
        FiltrationDate2.value = "2023-01-01";
        document.cookie = `FiltrationDate2=2023-01-01;`;
    }
    // Konec Datumu

    // Začátek Intervalu
    if (interval1) {
        FiltrationInterval1.value = interval1;
    } 
    else {
        FiltrationInterval1.value = 1;
        document.cookie = `FiltrationInterval1=1;`;
    }

    if (interval2) {
        FiltrationInterval2.value = interval2;
    } 
    else {
        FiltrationInterval2.value = 1440;
        document.cookie = `FiltrationInterval2=1440;`;
    }
    // Konec Intervalu

    // Začátek Jazyka
    if (languages1) {
        for (let i = 0, len = options.length; i < len; i++) {
            if (options[i].value === languages1) {
                options[i].selected = true;
                break;
            }
        }
    } 
    else {
        options[0].selected = true;
        document.cookie = `FiltrationLanguages1=${options[0].value};`;
    }
    // Konec Jazyka


    // Začátek Hodnocení - Není to úplně cookies
    if (stars1 === null){
        document.getElementById("FiltrationRadio6a").checked = true;
        document.cookie = `FiltrationStarsA=6;`;
    }
    else{
        document.getElementById(`FiltrationRadio${checkCookie("FiltrationStarsA")}a`).checked = true;
    }

    if (stars2 === null){
        document.getElementById("FiltrationRadio1b").checked = true;
        document.cookie = `FiltrationStarsB=1;`;
    }
    else{
        document.getElementById(`FiltrationRadio${checkCookie("FiltrationStarsB")}b`).checked = true;
    }
    // Konec Hodnocení
}

function changeCookies(elementID, userId){
    let original_value = document.getElementById(`${elementID}`).value;
    document.cookie = `${elementID}=${original_value};`;
}

function changeCookiesForCheckBoxes(elementID, userId){
    let original_value = document.getElementById(`${elementID}`).checked;
    document.cookie = `${elementID}=${original_value};`;
}

function changeCookiesForCheckBoxesA(elementID, userId){
    document.getElementById(`FiltrationRadio${elementID}a`).checked = true;
    document.cookie = `FiltrationStarsA=${elementID};`;
}

function changeCookiesForCheckBoxesB(elementID, userId){
    document.getElementById(`FiltrationRadio${elementID}b`).checked = true;
    document.cookie = `FiltrationStarsB=${elementID};`;
}

function changeCookiesForSelect(userId){
    let FiltrationLanguages1 = document.getElementById("FiltrationLanguages1");
    let options = FiltrationLanguages1.options;
    let selected_value;
    for (let i = 0, len = options.length; i < len; i++) {
        if (options[i].selected) {
            selected_value = options[i].value;
        }
    }
    document.cookie = `FiltrationLanguages1=${selected_value};`;
}

function deleteAllCookies() {
    const cookies = document.cookie.split(";");

    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i];
        const eqPos = cookie.indexOf("=");
        const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
}