window.addEventListener("load", function () {
    let login_prompt = document.getElementById('prompt');

    function login() {
        var XHR = new XMLHttpRequest();
    
        // Liez l'objet FormData et l'élément form
        var FD = new FormData(form);
    
        XHR.onreadystatechange = function () {
            if (XHR.readyState === XMLHttpRequest.DONE) {
                if (XHR.status === 200) {
                    login_prompt.innerHTML = XHR.responseText;
                } else {
                    login_prompt.innerHTML = 'Il y a eu un problème avec la requête.';
                }
            }
        };    
        XHR.open("POST", "../htbin/login.py");
        XHR.send(FD);
    }
    
    let form = document.getElementById('login-form');
    
    form.addEventListener("submit", function (event) {
        event.preventDefault();
    
        login();
    });
});