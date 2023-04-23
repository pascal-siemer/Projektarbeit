class Game {

    constructor() {
        
        this.title = document.querySelector('#gameTitle');

        this.prompt = document.querySelector('#prompt');

        this.buttonA = document.querySelector('#buttonA');

        this.buttonB = document.querySelector('#buttonB');

        this.buttonC = document.querySelector('#buttonC');

        this.buttonD = document.querySelector('#buttonD');

        this.buttons = [this.buttonA, 
                        this.buttonB,
                        this.buttonC, 
                        this.buttonD];

        this.scores = document.querySelector('#scores');
    
    }

}