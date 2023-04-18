const serverAddress = 'localhost';
const serverPort = 8123;
const socket = new WebSocket(`ws://${serverAddress}:${serverPort}`);
const game = new Game();

function requestQuestions() {
    let message = new Message('Question');
    let json = JSON.stringify(message);
    socket.send(json);
}

function requestNextQuestions() {
    let message = new Message('NextQuestion');
    let json = JSON.stringify(message);
    socket.send(json);
}

function updateQuestions(question) {
    game.prompt.innerHTML = question.prompt;
    game.buttonA.innerHTML = question.answers[0];
    game.buttonB.innerHTML = question.answers[1];
    game.buttonC.innerHTML = question.answers[2];
    game.buttonD.innerHTML = question.answers[3];
    game.indexCorrect = question.indexCorrect;
    
}

buttonEvent = (event, button, buttonIndex) => {
    button.style.background = game.indexCorrect === buttonIndex
        ? '#00FF00' 
        : '#FF0000';
}



// Event Listener

socket.onopen = event => {
    let message = new Message('Init', 'Pascal');
    let json = JSON.stringify(message);
    socket.send(json);
}

socket.onmessage = event => {
    let message = JSON.parse(event.data);
    let handler = message.handler;
    let value = JSON.parse(message.value);

    switch (handler) {
        case 'Question': 
            updateQuestions(value); 
            break;
        case 'NextQuestion': 
            updateQuestions(value); 
            break;
        case 'Init': 
            game.prompt.innerHTML = value; 
            requestQuestions(); 
            break;
        default: console.log(value);
    }
}

game.buttonA.onclick = event => buttonEvent(event, game.buttonA, 0);
game.buttonB.onclick = event => buttonEvent(event, game.buttonB, 1);
game.buttonC.onclick = event => buttonEvent(event, game.buttonC, 2);
game.buttonD.onclick = event => buttonEvent(event, game.buttonD, 3);
