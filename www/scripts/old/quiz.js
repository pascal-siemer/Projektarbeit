class Quiz {

    constructor(connection) {
        this.connection = connection;
        connection.registerQuiz(this);

        this.prompt = document.querySelector('#text')
        this.buttons = document.querySelectorAll('.answerButton');
        this.registerEvents();
    }

    registerEvents() {
        for (let button of this.buttons) {
            button.onclick = this.handleClick;
        }
    }

    handleClick(event) {
        this.connection.requestQuestion();
    }

    updateQuiz(question) {
        this.prompt = question.prompt
        this.buttons[0].innerHTML = question.answers[0];
        this.buttons[1].innerHTML = question.answers[1];
        this.buttons[2].innerHTML = question.answers[2];
        this.buttons[3].innerHTML = question.answers[3];
        this.indexCorrect = question.index_correct;
    }
}