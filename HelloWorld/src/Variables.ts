// variable declarations
function main() {
    let x: number = 10
    const y: number = 10
    // between 500 and 1000
    const RANDOM_WAIT_TIME: number =
        Math.round(Math.random() * 500) + 500

    let startTime: Date = new Date()
    let endTime: Date

    setTimeout(() => {
        endTime = new Date()
    }, RANDOM_WAIT_TIME)

}

// function definition with types
function add(a: number, b: number): number {
    return a + b
}

// types
let car: {
    make: string
    model: string
    year: number
}

// Optional property with ? in the types
function printCar(car: {
    make: string
    model: string
    year: number
    chargeVoltage?: number
}) {
    let str = `${car.make} ${car.model} (${car.year})`
    // car.chargeVoltage

    if (typeof car.chargeVoltage !== "undefined")
        str += `// ${car.chargeVoltage}v`
    console.log(str)
}

// Index signatures
const phone: {
    [k: string]: {
        country: string
        area: string
        number: string
    }
} = {}

phone.fax

// Array Types
const fileExtensions: string[] = ["js", "ts"]
const cars: {
    make: string
    model: string
    year: number
    chargeVoltage?: number
}[] = [{
    make: "Toyota",
    model: "Corolla",
    year: 2002,
},
    ]

/*
 Tuples: Sometimes we may want to work with a multi-element, 
 ordered data structure, where position of each item has some
 special meaning or convention. This kind of structure is often 
 called a tuple.
 */
//                                    [Year, Make,     Model    ]
let myCar: [number, string, string] = [2002, "Toyota", "Corolla"]
// destructured assignment is convenient here!
const [year, make, model]: [number, string, string] = myCar

const numPair: [number, number, number] = [4, 5, 6]


// Union Types: Union types in TypeScript can be described using the | (pipe) operator.
function flipCoin(): "heads" | "tails" {
    if (Math.random() > 0.5) return "heads"
    return "tails"
}

function maybeGetUserInfo():
    | ["error", Error]
    | ["success", { name: string; email: string }] {
    if (flipCoin() === "heads") {
        return [
            "success",
            { name: "Mike North", email: "mike@example.com" },
        ]
    } else {
        return [
            "error",
            new Error("The coin landed on TAILS :("),
        ]
    }
}

function NarrowingWithTypeGuards() {
    // Narrowing with type guards
    const outcome = maybeGetUserInfo()
    const [first, second] = outcome

    if (second instanceof Error) {
        // In this branch of your code, second is an Error
        second
    } else {
        // In this branch of your code, second is the user info
        second
    }
}

// Intersection types in TypeScript can be described using the & (ampersand) operator.
function IntersectionTypes() {
    function makeWeek(): Date & { end: Date } {
        //⬅ return type
        let ONE_WEEK = 10
        const start = new Date()
        const end = new Date(start.valueOf() + ONE_WEEK)

        return { ...start, end } // kind of Object.assign
    }

    const thisWeek = makeWeek()
    thisWeek.toISOString()
}

function DiscriminatedUnions() {
    const outcome = maybeGetUserInfo()
    if (outcome[0] === "error") {
        // In this branch of your code, second is an Error
        outcome
    } else {
        // In this branch of your code, second is the user info
        outcome
    }
}

