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

usingSetImmediate()

type SuccessCallback = (input: any) => void

class Oath {
    successCallback: SuccessCallback[]
    errorCallback: (error: Error) => void
    constructor(action: (resolve: (input: any) => void, reject: (err: Error) => void) => void) {

        action(this.onResolve.bind(this), this.onReject.bind(this))
    }

    then(callback: (input: any) => void): Oath {
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
            this.successCallback.forEach(callback => {
                callback(input)
            })
        } catch (error) {
            this.errorCallback(error)
        }
    }

    onReject(error: Error) {
        this.errorCallback(error)
    }
}

let newPromise = new Oath((res, rej) => {
    setTimeout(() => res(10), 500)
}).then((output) => {
    console.log(output)
})