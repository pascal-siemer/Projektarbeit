const serverAddress = 'localhost';
const serverPort = 8123;
const socket = new WebSocket(`ws://${serverAddress}:${serverPort}`);
const buttonRoundStart = document.querySelector('#ButtonRoundStart');
const buttonRoundStop = document.querySelector('#ButtonRoundStop');
const divDisplayMessage = document.querySelector('#DivDisplayMessage');

function Send(handler, value) {
    let message = new Message(handler, value);
    let json = JSON.stringify(message);
    socket.send(json);
}

const sendRegistration      = () => Send('Register', 'admin');
const sendStartRound        = () => Send('Round_Start', '{}');
const sendStopRound         = () => Send('Round_End', '{}');
const requestNextQuestions  = () => Send('NextQuestion', '{}');

socket.onopen = () => sendRegistration();
socket.onmessage = event => divDisplayMessage.innerHTML = JSON.stringify(event.data); 
buttonRoundStart.onclick = () => {sendStartRound(); requestNextQuestions();}
buttonRoundStop.onclick = () => sendStopRound();