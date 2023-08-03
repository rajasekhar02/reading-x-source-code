import { TwoNumberCalc, TwoNumberCalculation, handleMainEvent } from "./types"

function main() {
    const add: TwoNumberCalc = (a, b) => a + b
    const sub: TwoNumberCalculation = function (a, b) {
        return a - b
    }
    let MyDateConstructor: DateConstructor = Date
    const d = new MyDateConstructor()

    let hME = handleMainEvent
}


// https://www.typescript-training.com/course/fundamentals-v3/09-functions/#this-types
function WorkingWithThis() {
    function myClickHandler(this: HTMLButtonElement, event: Event) {
        this.disabled = true
    }
    myClickHandler
    // myClickHandler.
    const myButton = document.getElementsByTagName("button")[0]
    const boundHandler = myClickHandler.bind(myButton)
    boundHandler(new Event("click"))
    myClickHandler.call(myButton, new Event("click"))
}

WorkingWithThis()