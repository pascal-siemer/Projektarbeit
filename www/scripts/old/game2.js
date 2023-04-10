var answer;
var selectedButton;
var socket = new WebSocket('ws://localhost:8123');

document.getElementById('buttonA').onclick = () => buttonEvent(document.getElementById('buttonA'));
document.getElementById('buttonB').onclick = () => buttonEvent(document.getElementById('buttonB'));
document.getElementById('buttonC').onclick = () => buttonEvent(document.getElementById('buttonC'));
document.getElementById('buttonD').onclick = () => buttonEvent(document.getElementById('buttonD'));

function resetButtonColors() {
    var buttons = Array.from(document.getElementsByClassName('answerButton'));

    buttons.forEach(element => {
        element.style.backgroundColor = getComputedStyle(document.documentElement).getPropertyValue('--accentColor');
    });
}

function buttonEvent(button) {
    console.log(button.id);

    switch(button.id) {
        case 'buttonA':
            answer = 'A';
            break;
        case 'buttonB':
            answer = 'B';
            break;
        case 'buttonC':
            answer = 'C';
            break;
        case 'buttonD':
            answer = 'D';
            break;
        default:
            console.log("Answer invalid!");
            return;
    }

    selectedButton = button.id;

    resetButtonColors();
    requestAnswer();
}

function requestAnswer() {
        console.log(`requesting answer`);
        socket.send(`request:answer`);
}


socket.onopen = function() {
    socket.send("Javascript talking..");
};

socket.onmessage = function(event) {

    var receivedMessage = event.data;
    alert("Message received:  " + receivedMessage);

    if(selectedButton === null) {
        return;
    }

    if(!(receivedMessage === answer)) {
        selectedButton.style.backgroundColor = "Red";
        return;
    }

    selectedButton.style.backgroundColor = "Green";




};

socket.onclose = function() {
    alert("Websocket connection closed.");
};

socket.onerror = function() {
    alert("Websocket ERROR");
};