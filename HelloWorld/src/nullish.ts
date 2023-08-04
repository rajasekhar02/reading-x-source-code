type GroceryCart = {
  fruits?: { name: string; qty: number }[]
  vegetables?: { name: string; qty: number }[]
}
 
const cart: GroceryCart = {}
 
// non-null assertion operator
cart.fruits!.push({ name: "kumkuat", qty: 1 })

// definite assignment operator

class ThingWithAsyncSetup {
    setupPromise: Promise<any> // ignore the <any> for now
    // if `!:` operator is not used then results in
    // `ERROR: Property 'isSetup' has no initializer and is not definitely assigned in the constructor.`
    isSetup!: boolean
    constructor() {
        this.setupPromise = new Promise((resolve) => {
        this.isSetup = false
        return this.doSetup(resolve)
        }).then(() => {
        this.isSetup = true
        })
    }
 
  private async doSetup(resolve: (value: unknown) => void) {
    // some async stuff
  }
}