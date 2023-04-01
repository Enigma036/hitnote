function checkCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
      return parts.pop().split(";").shift();
    }
    return null;
}


function sortLoad(userId){
    const dateTH = document.getElementById("dateTH");
    const languageTH = document.getElementById("languageTH");
    const intervalTH = document.getElementById("intervalTH");
    const starsTH = document.getElementById("starsTH");

    let date_value = checkCookie("dateTH");
    let language_value = checkCookie("languageTH");
    let interval_value = checkCookie("intervalTH");
    let stars_value = checkCookie("starsTH");

    if (date_value) {
        dateTH.innerHTML = `<input type="hidden" name="dateTH" value="${date_value}"> <span>${date_value}</span>`;
    } 
    else {
        dateTH.innerHTML = `<input type="hidden" name="dateTH" value="&#8597;"> <span>&#8597;</span>`;
        document.cookie = `dateTH=&#8597;;`;
    }

    if (date_value) {
        languageTH.innerHTML = `<input type="hidden" name="languageTH" value="${language_value}"> <span>${language_value}</span>`;
    } 
    else {
        languageTH.innerHTML = `<input type="hidden" name="languageTH" value="&#8597;"> <span>&#8597;</span>`;
        document.cookie = `languageTH=&#8597;;`;
    }

    if (interval_value) {
        intervalTH.innerHTML = `<input type="hidden" name="intervalTH" value="${interval_value}"> <span>${interval_value}</span>`;
    } 
    else {
        intervalTH.innerHTML = `<input type="hidden" name="intervalTH" value="&#8597;"> <span>&#8597;</span>`;
        document.cookie = `intervalTH=&#8597;;`;
    }

    if (stars_value) {
        starsTH.innerHTML = `<input type="hidden" name="starsTH" value="${stars_value}"> <span>${stars_value}</span>`;
    } 
    else {
        starsTH.innerHTML = `<input type="hidden" name="starsTH" value="&#8597;"> <span>&#8597;</span>`;
        document.cookie = `starsTH=&#8597;;`;
    }

}



function sortOnChange(id,userId){
    const element = document.getElementById(id);
    let value = checkCookie(id);

    if(value=="&#8597;" || value=="&#8597"){
        value = "&#8595;"
        element.innerHTML = `<input type="hidden" name="${id}" value="${value}"> <span>${value}</span>`;
        document.cookie = `${id}=${value};`;
    }
    else if(value=="&#8595;" || value=="&#8595"){
        value = "&#8593;"
        element.innerHTML = `<input type="hidden" name="${id}" value="${value}"> <span>${value}</span>`;
        document.cookie = `${id}=${value};`;
    }
    else{
        value = "&#8597;"
        element.innerHTML = `<input type="hidden" name="${id}" value="${value}"> <span>${value}</span>`;
        document.cookie = `${id}=${value};`;
    }
}


function getOrder(userId){
    let dateOrder = checkCookie("dateOrder");
    let languagesOrder = checkCookie("languagesOrder");
    let intervalOrder = checkCookie("intervalOrder");
    let starsOrder = checkCookie("starsOrder");

    if(dateOrder && languagesOrder && intervalOrder && starsOrder){
        document.getElementById("IdOrderDate").innerHTML = `<input type="hidden" name="dateOrder" value="${dateOrder}">`
        document.getElementById("IdOrderLanguage").innerHTML = `<input type="hidden" name="languagesOrder" value="${languagesOrder}">`
        document.getElementById("IdOrderInterval").innerHTML = `<input type="hidden" name="intervalOrder" value="${intervalOrder}">`
        document.getElementById("IdOrderStars").innerHTML = `<input type="hidden" name="starsOrder" value="${starsOrder}">`
    }
    else{
        document.cookie = `dateOrder=1;`;
        document.cookie = `languagesOrder=2;`;
        document.cookie = `intervalOrder=3;`;
        document.cookie = `starsOrder=4;`;
    }
}

function changeOrder(id, userId){
    let orderArray = [];
    let dateOrder = checkCookie("dateOrder");
    let languagesOrder = checkCookie("languagesOrder");
    let intervalOrder = checkCookie("intervalOrder");
    let starsOrder = checkCookie("starsOrder");

    orderArray.push(parseInt(dateOrder), parseInt(languagesOrder), parseInt(intervalOrder), parseInt(starsOrder))

    let original_value = parseInt(checkCookie(id));
    let index = 0;
    
    if(id == "dateOrder"){
        index = 0;
    }
    else if(id == "languagesOrder"){
        index = 1;
    }
    else if(id == "intervalOrder"){
        index = 2;
    }
    else if(id == "starsOrder"){
        index = 3;
    }   

    if((original_value) == 2){
        for(let i=0; i < orderArray.length; i++){
            if(orderArray[i] == 1){
                orderArray[i] = 2;
            }
        }
        orderArray[index] = 1;
    }

    else if((original_value) == 3){
        for(let i=0; i < orderArray.length; i++){
            if(orderArray[i] == 1){
                orderArray[i] = 2;
            }
            else if(orderArray[i] == 2){
                orderArray[i] = 3;
            }
        }
        orderArray[index] = 1;
    }

    else if((original_value) == 4){
        for(let i=0; i < orderArray.length; i++){
            if(orderArray[i] == 1){
                orderArray[i] = 2;
            }
            else if(orderArray[i] == 2){
                orderArray[i] = 3;
            }
            else if(orderArray[i] == 3){
                orderArray[i] = 4;
            }
        }
        orderArray[index] = 1;
    }
    
    document.cookie = `dateOrder=${orderArray[0]};`;
    document.cookie = `languagesOrder=${orderArray[1]};`;
    document.cookie = `intervalOrder=${orderArray[2]};`;
    document.cookie = `starsOrder=${orderArray[3]};`;

    document.getElementById("IdOrderDate").innerHTML = `<input type="hidden" name="dateOrder" value="${orderArray[0]}">`
    document.getElementById("IdOrderLanguage").innerHTML = `<input type="hidden" name="languagesOrder" value="${orderArray[1]}">`
    document.getElementById("IdOrderInterval").innerHTML = `<input type="hidden" name="intervalOrder" value="${orderArray[2]}">`
    document.getElementById("IdOrderStars").innerHTML = `<input type="hidden" name="starsOrder" value="${orderArray[3]}">`

}