class Game {

    constructor() {
        this.title = document.querySelector('#gameTitle');
        this.prompt = document.querySelector('#prompt');
        this.buttonA = document.querySelector('#buttonA');
        this.buttonB = document.querySelector('#buttonB');
        this.buttonC = document.querySelector('#buttonC');
        this.buttonD = document.querySelector('#buttonD');
        this.scores = document.querySelector('#scores');
        this.indexCorrect = -1; //entfernen, juckt den client nicht.
    }

}