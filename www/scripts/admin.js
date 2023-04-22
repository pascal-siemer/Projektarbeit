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

let registerPlayer = () => Send('Init', 'admin');
let sendStartRound = () => Send('Round_Start', '{}');
let sendStopRound  = () => Send('Round_End', '{}');

socket.onmessage = event => divDisplayMessage.innerHTML = event.data; 
buttonRoundStart.onclick = () => sendStartRound();
buttonRoundStop.onclick = () => sendStopRound();