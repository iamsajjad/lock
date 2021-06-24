
// Change value
function checkTypes() {
  var currency = document.getElementById('currency');
  var currencyCheckbox = document.getElementById('currencyCheckbox');
  let currencyElements = document.querySelectorAll('.currentCurrency');
  var branch = document.getElementById('branch');
  var branchCheckbox = document.getElementById('branchCheckbox');

  // for currency
  if (currencyCheckbox.checked == false) {
    currency.value = 'IQD';
    for (let i = 0; i < currencyElements.length; i++) {
      currencyElements[i].innerHTML = currencies.IQD;
    }
  } else {
    currency.value = 'USD';
    for (let i = 0; i < currencyElements.length; i++) {
      currencyElements[i].innerHTML = currencies.USD;
    }
  }

  // for cluster Type
  if (branchCheckbox.checked == false) {
    branch.value = 'False';
  } else {
    branch.value = 'True';
  }
}

function checkMode() {
  var mode = document.getElementById('mode')
  var checkbox = document.getElementById('modeCheckbox')
  if (mode.checked == false) {
    checkbox.value = 'Dark';
  } else {
    checkbox.value = 'Light';
  }

  // submit from
  var form = document.getElementById("themeForm");
  form.submit();
}

function checkLanguage() {
  var language = document.getElementById('language')
  var checkbox = document.getElementById('languageCheckbox')
  if (language.checked == false) {
    checkbox.value = 'en';
  } else {
    checkbox.value = 'ar';
  }

  // submit from
  var form = document.getElementById("languageForm");
  form.submit();
}

function checkPrinterLanguage() {
  var language = document.getElementById('printerLanguage')
  var checkbox = document.getElementById('printerLanguageCheckbox')
  if (language.checked == false) {
    checkbox.value = 'en';
  } else {
    checkbox.value = 'ar';
  }

  // submit from
  var form = document.getElementById("printerLanguageForm");
  form.submit();
}
