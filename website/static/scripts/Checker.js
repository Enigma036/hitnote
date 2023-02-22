function checkCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
      return parts.pop().split(";").shift();
    }
    return null;
}

function Interval1(x, y)
{
    var interval1 = document.getElementById(x).value;
    var interval2 = document.getElementById(y).value;
    
    if(parseInt(interval1) > parseInt(interval2)){
        document.getElementById(x).value = interval2;
    }

    if(parseInt(interval1) > 1440){
        document.getElementById(x).value = interval2;
    }

    if(parseInt(interval1) < 0){
        document.getElementById(x).value = 0;
    }
}

function Interval2(x, y){
    var interval1 = document.getElementById(x).value;
    var interval2 = document.getElementById(y).value;
    if(parseInt(interval2) < parseInt(interval1)){
        document.getElementById(y).value = interval1;
    }

    if(parseInt(interval2) > 1440){
        document.getElementById(y).value = 1440;
    }

    if(parseInt(interval2) < 0){
        document.getElementById(y).value = interval1;
    }
}

function Rating1(){
    var rating1 = document.getElementById(CheckedRadio('a')).value;
    var rating2 = document.getElementById(CheckedRadio('b')).value;
    var id = 0;
    if(parseInt(rating1) > parseInt(rating2)){
        id = 'FiltrationRadio' + (6-rating2) + 'a';
        document.getElementById(id).checked = true;
    }
}

function Rating2(){
    var rating1 = document.getElementById(CheckedRadio('b')).value;
    var rating2 = document.getElementById(CheckedRadio('a')).value;
    
    var id = 0;

    if(parseInt(rating1) < parseInt(rating2)){
        id = 'FiltrationRadio' + (6-rating2) + 'b';
        document.getElementById(id).checked = true;
    }
}

function CheckedRadio(x){
    for(var i = 0; i <= 5;i++){
        var id = `FiltrationRadio${(6-i)}${x}`;
        if(document.getElementById(id).checked == true){
            return id;
        }
    }
}


function Datum(userId){

    let check_value = checkCookie("datechecker");

    if(check_value == null){
        var date = new Date();

        var day1 = date.getDate();
        var day2 = day1;
        var month = date.getMonth() + 1;
        var year1 = date.getFullYear();
        var year2 = year1-1;

        if (month < 10) month = "0" + month;
        if (day1 < 10) day1 = "0" + day1;
        if (day2 < 10) day2 = "0" + day2;

        var today = year1 + "-" + month + "-" + day1;
        var yesterday = year2 + "-" + month + "-" + day2;
        document.getElementById("FiltrationDate2").defaultValue = today;
        document.getElementById("FiltrationDate1").defaultValue = yesterday;
        document.cookie = `FiltrationDate2=${today};`;
        document.cookie = `FiltrationDate1=${yesterday};`;
        document.cookie = `datechecker=1;`;
    }
}

function Datum_add_message(){
    var date = new Date();
    var day1 = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();

    if (month < 10) month = "0" + month;
    if (day1 < 10) day1 = "0" + day1;

    var today = year + "-" + month + "-" + day1;
    document.getElementById("AddDate1").defaultValue = today;
}


function Date1(){
    var date1 = document.getElementById('FiltrationDate1').value;
    var date2 = document.getElementById('FiltrationDate2').value;
    if(date1 > date2){
        document.getElementById('FiltrationDate1').value = date2;
    }
}

function Date2(){
    var date1 = document.getElementById('FiltrationDate1').value;
    var date2 = document.getElementById('FiltrationDate2').value;
    if(date2 < date1){
        document.getElementById('FiltrationDate2').value = date1;
    }
}
