class Quiz {

    constructor(connection) {
        this.connection = connection;
        connection.registerQuiz(this);

        this.prompt = document.querySelector('#prompt')
        this.buttons = document.querySelectorAll('.answerButton');
        this.indexCorrect = 0;

        console.log(this.buttons);
        this.registerEvents();
    }

    registerEvents() {
        for (let button of this.buttons) {
            button.onclick = this.handleClick;
        }
    }

    handleClick = event => {
        this.connection.requestQuestion();
    }

    updateQuiz(question) {
        this.prompt.innerHTML = question.prompt
        this.buttons[0].innerHTML = question.answers[0];
        this.buttons[1].innerHTML = question.answers[1];
        this.buttons[2].innerHTML = question.answers[2];
        this.buttons[3].innerHTML = question.answers[3];
        this.indexCorrect = question.indexCorrect;
    }
}