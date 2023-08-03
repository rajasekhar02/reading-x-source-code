// Type Alias
export type UserContactInfo = {
    name: string
    email: string
}

// Type Inheritance
export type SpecialDate = Date & { getReason(): string }

// Interfaces
export interface UserInfo {
    name: string
    email: string
}

class LivingOrganism {
    isAlive() {
        return true
    }
    consumeFood(food: any) {
        console.log("Consumed")
    }
}
interface AnimalLike {
    eat(food: string): void
}
interface CanBark {
    bark(): string
}

class Dog
    extends LivingOrganism
    implements AnimalLike, CanBark {
    bark() {
        return "woof"
    }
    eat(food: string) {
        this.consumeFood(food)
    }
}