const url = 'ws://localhost'
const port = 8123;
const websocket = new WebSocket(`${url}:${port}`);

const buttonQuestions = document.querySelector('#ButtonQuestions');
const buttonScores = document.querySelector('#ButtonScores');
const inputScores = document.querySelector('#InputScores');
const divResponse = document.querySelector('#DivResponse');

websocket.onmessage = function(event) {
    divResponse.innerHTML = event.data;
}

buttonQuestions.onclick = function(event) {
    websocket.send('<<Question>>Question');
}

buttonScores.onclick = function(event) {
    value = inputScores.value;
    websocket.send(`<<Score>>${value}`);
}
