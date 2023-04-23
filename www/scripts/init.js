const serverAddress = 'localhost';
const serverPort = 8123;
const socket = new WebSocket(`ws://${serverAddress}:${serverPort}`);
const game = new Game();

let indexSelectedAnswer = -1;

// Messaging

function jsonToMessage(json) {
    let object = JSON.parse(json);
    let handler = object.handler;
    let value = JSON.parse(object.value);
    return new Message(handler, value);
}

function getUsername() {
    return new URLSearchParams(window.location.search).get('username')
}

function send(handler, value='{}') {
    let message = new Message(handler, value);
    let json = JSON.stringify(message);
    socket.send(json);
}

const requestAnswer         = () => send('Answer', indexSelectedAnswer)
const requestQuestions      = () => send('Question');
const requestScore          = () => send('Score');
const sendRegistration      = () => send('Register', getUsername());
const sendSelection         = () => send('Selection', indexSelectedAnswer);

// Updating UI

function resetUI() {

    for (let button of game.buttons) {
        button.classList.remove('selected', 'correct', 'incorrect');
    }
}

function selectButton(button) {
    indexSelectedAnswer = -1
    let iteratedButton;
    for (let i = 0; i < game.buttons.length; i++) {
        iteratedButton = game.buttons[i];
        iteratedButton.classList.remove('selected', 'correct', 'incorrect');
        if (button === iteratedButton) {
            indexSelectedAnswer = i;
            button.classList.add('selected');
        }
    }
}

function updateQuestions(question) {
    game.prompt.innerHTML   = question.prompt;
    let length = Math.min(game.buttons.length, question.answers.length);
    for(let i = 0; i < length; i++) {
        game.buttons[i].innerHTML = question.answers[i];
    }
}

function updateScores(players) {
    game.scores.innerHTML = '';
    for (let player of players) {
        game.scores.innerHTML += `${player.name}: ${player.score}<br>`;
    }
}

function updateSelectionWithAnswer(isAnswerCorrect) {
    resetUI();
    if(indexSelectedAnswer < 0 || indexSelectedAnswer >= game.buttons.length) {
        return;
    }
    let selectedButton = game.buttons[indexSelectedAnswer];
    selectedButton.classList.add(isAnswerCorrect
        ? 'correct'
        : 'incorrect');
}

// Event Listener

socket.onopen = () => {
    sendRegistration(); 
}
socket.onmessage = event => routeMessage(jsonToMessage(event.data));

game.buttonA.onclick = event => selectButton(event.target);
game.buttonB.onclick = event => selectButton(event.target);
game.buttonC.onclick = event => selectButton(event.target);
game.buttonD.onclick = event => selectButton(event.target);

function routeMessage(message) {

    console.log(`${message.handler} <- ${message.value}`);

    switch (message.handler) {
        
        case 'Question': 
            updateQuestions(message.value);         
            break;

        case 'NextQuestion': 
            updateQuestions(message.value);
            break;

        case 'Scores': 
            updateScores(message.value);
            break;

        case 'Register': 
            updateScores(message.value);
            requestQuestions();                  
            break;

        case 'Round_Start':
            requestQuestions();
            resetUI();
            break;

        case 'Round_End':
            sendSelection();
            requestAnswer();
            setTimeout(requestScore, 500);
            break;

        case 'Score':
            updateScores(message.value);
            break;

        case 'Answer':
            updateSelectionWithAnswer(message.value);
            break;

        default: break;
    }
}
