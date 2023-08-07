interface Person {
  name: string;
  age: number;
  city: string;
}

type PersonKeys = keyof Person;

function printPersonProperty(person: Person, property: PersonKeys) {
  console.log(`Person's ${property}: ${person[property]}`);
}

const person: Person = {
  name: "Alice",
  age: 30,
  city: "New York",
};

printPersonProperty(person, "name"); // Output: Person's name: Alice
printPersonProperty(person, "age");  // Output: Person's age: 30
printPersonProperty(person, "city"); // Output: Person's city: New York
printPersonProperty(person, "address") // TypeError: Because there is not key with 'address' in Person type



// typeof
// as class is both type and value
class Fruit {
  constructor(
    public readonly name: string,
    public readonly mass: number,
    public readonly color: string
  ) {}
 
  static createBanana() {
    return new Fruit("banana", 108, "yellow")
  }
}

// MyFruit, the class (constructor) is of type typeof Fruit,
const MyFruit = Fruit

const banana: Fruit = MyFruit.createBanana()
const apple: Fruit = new MyFruit("apple", 20, "red")