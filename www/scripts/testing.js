const url = 'ws://localhost'
const port = 8123;
const websocket = new WebSocket(`${url}:${port}`);

const buttonConnect = document.querySelector('#ButtonConnect');
const buttonQuestions = document.querySelector('#ButtonQuestions');
const buttonScores = document.querySelector('#ButtonScores');
const inputPlayerName = document.querySelector('#InputPlayerName');
const inputScores = document.querySelector('#InputScores');
const divResponse = document.querySelector('#DivResponse');

websocket.onopen = event => {
    let message = new Message('Init', 'Pascal')
    let json_of_message = JSON.stringify(message);
    websocket.send(json_of_message);
}

websocket.onmessage = event => {
    divResponse.innerHTML = event.data;
}

buttonConnect.onclick = event => {
    value = inputScores.value;
    websocket.send(`<<Init>>${value}`);
}

buttonQuestions.onclick = event => {
    websocket.send('<<Question>>Question');
}

buttonScores.onclick = event =>{
    value = inputScores.value;
    websocket.send(`<<Score>>${value}`);
}
