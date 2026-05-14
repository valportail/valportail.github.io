let form = document.getElementById('signup-form')

let lastname = document.getElementById('lastname');
let firstname = document.getElementById('firstname');
let birthdate = document.getElementById('birthdate');
let username = document.getElementById('username');
let password = document.getElementById('userpwd');
let email = document.getElementById('useremail');

let submit = document.getElementById('signup-submit')

function testName(name) {
    return name.value.length > 0;
}

function testBirthDate(birthdate) {
    var birthdateRegExp = /^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$/
    var date = Date.parse(birthdate.value.split('/').reverse().join('-'));

    return birthdate.value.length === 0 || (birthdateRegExp.test(birthdate.value) && (date != NaN && date <= Date.now()));
}

function testUserName(username) {
    return username.value.length >= 6;
}

function testEmail(email) {
    var emailRegExp = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    return emailRegExp.test(email.value);
}

function testPassword(password) {
    var passwordRegExp = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$/;
    return passwordRegExp.test(password.value);
}

function testForm(form) {
    return testName(lastname) && testName(firstname) && testBirthDate(birthdate)
           && testUserName(username) && testEmail(email) && testPassword(password);
}

// Vérification du nom de famille et du prénom

lastname.addEventListener("keyup", function() {
    lastname.className = testName(lastname) ? "form-texte" : "form-texte-invalid"
});

firstname.addEventListener("keyup", function() {
    firstname.className = testName(firstname) ? "form-texte" : "form-texte-invalid"
});

// Vérification de la date de naissance

birthdate.addEventListener("keyup", function() {
    birthdate.className = testBirthDate(birthdate) ? "form-texte" : "form-texte-invalid";
});

// Vérification du nom d'utilisateur

username.addEventListener("keyup", function() {
    username.className = testUserName(username) ? "form-texte" : "form-texte-invalid";
});

// Vérification du mot de passe

password.addEventListener("keyup", function() {
    password.className = testPassword(password) ? "form-texte" : "form-texte-invalid";
});

// Vérification de l'adresse e-mail

email.addEventListener("keyup", function () {
    email.className = testEmail(email) ? "form-texte" : "form-texte-invalid";
});

// Vérification finale à l'envoi du formulaire

window.addEventListener("load", function() {
    if (!testForm(form)) {
        submit.disabled = 'disabled';
    } else {
        submit.disabled = false;
    }
});

form.addEventListener("keyup", function() {
    if (!testForm(form)) {
        submit.disabled = 'disabled';
    } else {
        submit.disabled = false;
    }
});