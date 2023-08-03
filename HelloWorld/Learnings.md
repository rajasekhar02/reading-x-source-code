A good way to think of TS files:

* .ts files contain both type information and code that runs
* .js files contain only code that runs
* .d.ts files contain only type information

## Categorizing Type Systems
### Static vs dynamic
* TypeScript’s type system is static.
* Dynamic type systems perform their “type equivalence” evaluation at runtime.
### Nominal vs structural
* Nominal type systems are all about NAMES.
    ```Java
    public class Car {
    String make;
    String model;
    int make;
    }
    public class CarChecker {
    // takes a `Car` argument, returns a `String`
    public static String printCar(Car car) {  }
    }
    Car myCar = new Car();
    // TYPE CHECKING
    // -------------
    // Is `myCar` type-equivalent to
    //     what `checkCar` wants as an argument?
    CarChecker.checkCar(myCar);
    ```
    In the code above, when considering the question of type equivalence on the last line, all that matters is whether myCar is an instance of the class named Car.

* Structural type systems are all about STRUCTURE or SHAPE. Let’s look at a TypeScript example:
```ts
class Car {
  make: string
  model: string
  year: number
  isElectric: boolean
}
 
class Truck {
  make: string
  model: string
  year: number
  towingCapacity: number
}
 
const vehicle = {
  make: "Honda",
  model: "Accord",
  year: 2017,
}
 
function printCar(car: {
  make: string
  model: string
  year: number
}) {
  console.log(`${car.make} ${car.model} (${car.year})`)
}
 
printCar(new Car()) // Fine
printCar(new Truck()) // Fine
printCar(vehicle) // Fine
```
The function printCar doesn’t care about which constructor its argument came from, it only cares about whether it has:

A make property that’s of type string
A model property that’s of type string
A year property that’s of type number
If the argument passed to it meets these requirements, printCar is happy.


## Compiler options
### [target](https://www.typescriptlang.org/tsconfig#target)
Modern browsers support all ES6 features, so ES6 is a good choice. You might choose to set a lower target if your code is deployed to older environments, or a higher target if your code is guaranteed to run in newer environments.

---
### [module](https://www.typescriptlang.org/tsconfig#module)

Sets the module system for the program. See the [Modules](https://www.typescriptlang.org/docs/handbook/modules.html) reference page for more information. You very likely want "CommonJS" for node projects.

---

### declaration
Generate .d.ts files for every TypeScript or JavaScript file inside your project. These .d.ts files are type definition files which describe the external API of your module. With .d.ts files, tools like TypeScript can provide intellisense and accurate types for un-typed code.

---