let x = 10
const y = 10
// between 500 and 1000
const RANDOM_WAIT_TIME =
    Math.round(Math.random() * 500) + 500

let startTime = new Date()
let endTime: Date

setTimeout(() => {
    endTime = new Date()
}, RANDOM_WAIT_TIME)

function add(a: number, b: number) {
    return a + b
}
