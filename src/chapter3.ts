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
function () {
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
