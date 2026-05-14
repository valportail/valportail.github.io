let messages = document.getElementById("list-messages");
let form = document.getElementById("chat-form");

function update() {
    let lastMessage;
    let lastModif;

    $.getJSON("../htbin/chatget.py", function(data) {
        var items = [];

        // Les messages sont enregistrés dans le fichier dans l'ordre chronologique
        // (du + ancien au + récent).
        lastMessage = data[data.length-1].date + " " + data[data.length-1].time;

        if (lastMessage != lastModif) { // S'il y a eu une modification
            for (var m of data) {
                items.push('<div class="message">');
                items.push('<p class="message-header">' + m.user + ', le ' + m.date + ' à ' + m.time + '</p>');
                items.push('<p>' + m.msg + '</p>');
                items.push('</div>');
            }
    
            messages.innerHTML = items.join('\n');

            lastModif = lastMessage;
        }
    });
}

// window.addEventListener("load", update());

window.addEventListener("load", function() {
    update();
    this.setInterval(update, 3000);
});

form.addEventListener("submit", function(event) {
    let content = document.getElementById("msg");
    let chat_prompt = document.getElementById("prompt");

    event.preventDefault();

    $.post("../htbin/chatsend.py", {msg: content.value}, function(answer) {

        if (answer.num == -1 || answer.num == 1) {
            chat_prompt.innerHTML = answer.msg;
        } else if (answer.num == 0) {
            chat_prompt.innerHTML = "Votre message a bien été envoyé !";
            update();
        }
    });
});