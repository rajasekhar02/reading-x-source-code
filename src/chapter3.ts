import fs from "fs-extra"
import { glob } from "glob"


function callbacksWithZeroTimeouts() {
    [1000, 1500, 500].forEach((t) => {
        console.log(`about to setTimeout for ${t}`)
        setTimeout(() => console.log(`inside timer handler for ${t}`), 0)
    })
}

function usingSetImmediate() {
    [1000, 1500, 500].forEach((t) => {
        console.log(`about to setTimeout for ${t}`)
        setImmediate(() => console.log(`inside timer handler for ${t}`))
    })
}

// usingSetImmediate()

type SuccessCallback = <T>(input: T) => any

class Oath {
    private status: 'RESOLVED' | 'REJECTED' | "PENDING"
    private successCallback: SuccessCallback[]
    private errorCallback: (error: any) => void
    constructor(action: (resolve: (input: any) => void, reject: (err: any) => void) => void) {
        this.successCallback = []
        // this.status = "PENDING"
        this.errorCallback = () => { }
        action(this.onResolve.bind(this), this.onReject.bind(this))
    }

    then(callback: SuccessCallback): Oath {
        // The reason for successCallback is a array because `then` 
        // is a synchornous function so all the callbacks need to be 
        // append to the promise instance
        this.successCallback.push(callback)
        return this
    }

    catch(errorCallback: (error: Error) => void): Oath {
        this.errorCallback = errorCallback
        return this
    }

    onResolve(input: any) {
        let callBackInput = input
        try {
            this.successCallback.forEach(action => {
                callBackInput = action(callBackInput)
            })
        } catch (error) {
            this.successCallback = []
            this.onReject(error)
        }
    }

    onReject(error: any) {
        this.errorCallback(error)
    }
}

// let newPromise2 =
function promiseWOCallingResolve() {
    new Oath((resolve, reject) => {
        console.log('top of a single then clause')
    }).then((value) => {
        console.log(`then with "${value}"`)
        return 'first then value'
    })
}


function resolvingPromise() {
    new Oath((resolve, reject) => {
        console.log('top of action callback with double then and a catch')
        setTimeout(() => {
            console.log('about to call resolve callback')
            resolve('initial result')
            console.log('after resolve callback')
        }, 0)
        console.log('end of action callback')
    }).then((value) => {
        console.log(`first then with "${value}"`)
        return 'first value'
    }).then((value) => {
        console.log(`second then with "${value}"`)
        return 'second value'
    })
}



function rejection() {
    new Oath((resolve, reject) => {
        console.log('top of action callback with deliberate error')
        setTimeout(() => {
            console.log('about to reject on purpose')
            reject('error on purpose')
        }, 0)
    }).then((value) => {
        console.log(`should not be here with "${value}"`)
    }).catch((err) => {
        console.log(`in error handler with "${err}"`)
    })
}


// Difference between process.nextTick and setImmediate

function nextTickVsSetImmediate() {
    console.log("1")

    setImmediate(() => {
        console.log("Output From setImmediate")
    })
    setTimeout(() => {
        console.log("output from timeout")
    })
    process.nextTick(() => {
        console.log("output from process.nextTick")
    })
    return "nextTickVsSetImmediate"
}


function head() {
    let [linesToDisplay, ...filesNames] = process.argv.slice(2, process.argv.length)
    const linesToDisplayInt: number = Number.parseInt(linesToDisplay);
    if (isNaN(linesToDisplayInt)) {
        console.log(`Invalid arguments: `, linesToDisplay)
        return
    }
    filesNames.forEach(async (fileName) => {
        if (!fs.existsSync(fileName)) return
        const status = await fs.stat(fileName)
        if (!status.isFile()) return
        try {
            const content = await fs.readFileSync(fileName, { encoding: 'utf-8' })
            const contentByLines = content.split("\n")
            const fileLength = contentByLines.length
            const sliceEnd = Math.max(0, Math.min(linesToDisplayInt, fileLength))
            console.log(contentByLines.slice(0, sliceEnd).join("\n"))
        } catch (err) {
            console.error("Failed to process: ", fileName)
        }
    })
}

function tail() {
    let [linesToDisplay, ...filesNames] = process.argv.slice(2, process.argv.length)
    const linesToDisplayInt: number = Number.parseInt(linesToDisplay);
    if (isNaN(linesToDisplayInt)) {
        console.log(`Invalid arguments: `, linesToDisplay)
        return
    }
    filesNames.forEach(async (fileName) => {
        if (!fs.existsSync(fileName)) return
        const status = await fs.stat(fileName)
        if (!status.isFile()) return
        try {
            const content = await fs.readFileSync(fileName, { encoding: 'utf-8' })
            const contentByLines = content.split("\n")
            const fileLength = contentByLines.length
            const sliceStart = Math.max(0, Math.min(fileLength - linesToDisplayInt, fileLength))
            console.log(contentByLines.slice(sliceStart, fileLength).join("\n"))
        } catch (err) {
            console.error("Failed to process: ", fileName)
        }
    })
}

const statsPair = async (fileName: string) => {
    const stats = await fs.statSync(fileName)
    return { fileName, stats }
}




// function lh() {
//     const main = async (srcDir) => {
//         const files = await glob(`${srcDir}/**/*.*`)
//         const pairs = await 
//     }
// }

import fsa from 'fs-extra-promise'
import yaml from 'js-yaml'

const test = async () => {
    const raw = await fsa.readFileAsync('config.yml', 'utf-8')
    console.log('inside test, raw text', raw)
    const cooked = yaml.load(raw)
    console.log('inside test, cooked configuration', cooked)
    return cooked
}

const result = test()
console.log('outside test, result is', result.constructor.name)
result.then(something => console.log('outside test we have', something))