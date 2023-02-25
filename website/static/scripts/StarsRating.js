function setPreviousValues() {
  const radioButtons = document.querySelectorAll('input[type="radio"]');
  radioButtons.forEach(function(radio) {
    if (radio.checked) {
      radio.setAttribute('previousValue', true);
    } else {
      radio.setAttribute('previousValue', false);
    }
  });
}

function toggleRadioButton(radio) {
    const radioButtons = document.querySelectorAll('input[name="' + radio.name + '"]');
    if (radio.getAttribute('previousValue') === 'true') {
      radio.checked = false;
      radio.setAttribute('previousValue', false);
    } else {
      radioButtons.forEach(function(radio) {
        radio.setAttribute('previousValue', false);
      });
      radio.checked = true;
      radio.setAttribute('previousValue', true);
    }
  }

  function toggleRadioButtonRadioA(radio) {
    const radioButtons = document.querySelectorAll('input[name="' + radio.name + '"]');
    if (radio.getAttribute('previousValue') === 'true') {
          radio.checked = false;
          radio.setAttribute('previousValue', false);
          document.getElementById("FiltrationRadio6a").checked = true;
          changeCookiesForCheckBoxesA("6",1);
          elementFiltrationChange("CheckStars");
    } else {
      radioButtons.forEach(function(radio) {
        radio.setAttribute('previousValue', false);
      });
      if(radio.value <= document.getElementById(CheckedRadio('b')).value){
        radio.checked = true;
        radio.setAttribute('previousValue', true);
      }
      else{
        radio.checked = true;
        var id = CheckedRadio('b').slice(0, -1).concat('a');
        document.getElementById(id).setAttribute('previousValue', true);  
      }
    }
  }

  function toggleRadioButtonRadioB(radio) {
    const radioButtons = document.querySelectorAll('input[name="' + radio.name + '"]');
    if (radio.getAttribute('previousValue') === 'true') {
      if(document.getElementById(CheckedRadio('a')).value == 0){
        radio.checked = false;
        radio.setAttribute('previousValue', false);
        document.getElementById("FiltrationRadio6b").checked = true;
        changeCookiesForCheckBoxesB("6",1);
        elementFiltrationChange("CheckStars");
      }
    } else {
      radioButtons.forEach(function(radio) {
        radio.setAttribute('previousValue', false);
      });
      if(radio.value >= document.getElementById(CheckedRadio('a')).value){
        radio.checked = true;
        radio.setAttribute('previousValue', true);
      }
      else{
        radio.checked = true;
        var id = CheckedRadio('a').slice(0, -1).concat('b');
        document.getElementById(id).setAttribute('previousValue', true);  
      }
  }
}