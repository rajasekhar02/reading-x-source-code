export class Car {
    public readonly ID: number
    public make: string
    public model: string
    #year: number
    protected vinNumber = generateVinNumber()
    private doorLockCode = generateDoorLockCode()
    constructor(make: string, model: string, year: number) {
        this.make = make
        this.model = model
        this.#year = year
    }

    protected unlockAllDoors() {
        unlockCar(this, this.doorLockCode)
    }
}


export function generateVinNumber(): number

export function generateVinNumber(): number {
    return 0
}

export function generateDoorLockCode(): string
export function generateDoorLockCode(): string {
    return "adsf"
}

export function unlockCar(car: Car, doorLockCode: string): void
export function unlockCar(car: Car, doorLockCode: string): void {
    console.log("Unlocked")
}