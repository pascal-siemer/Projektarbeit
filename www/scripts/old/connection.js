class Connection {

    //endpoints = ['SEND', 'GET'];

    constructor(url, port) {
        this.websocket = new WebSocket(`ws://${url}:${port}`);
        this.registerEvents();
    }

    registerEvents() {
        throwErrorIf(!this.websocket, 'no Websocket found!');
        this.websocket.onopen = this.handleOnOpen;
        this.websocket.onmessage = this.handleOnMessage;
        this.websocket.onclose = this.handleOnClose;
        this.websocket.onerror = this.handleOnError;
    }

    registerQuiz(quiz) {
        this.quiz = quiz;
    }


    requestQuestion() {
        return this.websocket.send("<<Question>>");
    }


    getEndpoint(message) {
        for (let endpoint of this.endpoints) {
            if(message.includes(endpoint)) {
                return endpoint;
            }
        }
    }

    // event handler

    handleOnOpen = event => {
        let connectedSocket = event.target;
        let message = "<<Question>>";
        connectedSocket.send(message);
        console.log(message);
    }
    
    handleOnMessage = event => {
        logObject(event, 'message incoming');
        let question = JSON.parse(event.data)
        this.quiz?.updateQuiz(question);
    }

    handleOnClose = event => {
        logObject(event, 'connection closed');
    }

    handleOnError = event => {
        logObject(event, 'ERROR');
    }

}