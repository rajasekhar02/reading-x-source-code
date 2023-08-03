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
## Type Aliases
Type aliases help to address this, by allowing us to:

* define a more meaningful name for this type
* declare the particulars of the type in a single place
* import and export this type from modules, the same as if it were an exported value

### Inheritance in type aliases
You can create type aliases that combine existing types with new behavior by using Intersection (`&`) types.
## Interfaces
* An interface is a way of defining an object type. An “object type” can be thought of as, “an instance of a class could conceivably look like this”.
For example, `string | number` is not an object type, because it makes use of the union type operator.
* Like type aliases, interfaces can be imported/exported between modules just like values, and they serve to provide a “name” for a specific type.
### Inheritance in interfaces
`extends` is used in following cases:
* a subclass extends from a base class.
* a “sub-interface” extends from a base interface

`implements` in TypeScript adds a second heritage clause that can be used to state that a given class should produce instances that confirm to a given interface.

* While TypeScript (and JavaScript) does not support true multiple inheritance (extending from more than one base class), this implements keyword gives us the ability to validate, at compile time, that instances of a class conform to one or more “contracts” (types).

* While it’s possible to use implements with a type alias, if the type ever breaks the “object type” rules there’s some potential for problems…
```ts
type CanBark =
  | number
  | {
      bark(): string
    }
 
class Dog implements CanBark {
// ERROR: A class can only implement an object type or intersection of object types with statically known members.
  bark() {
    return "woof"
  }
  eat(food) {
    consumeFood(food)
  }
}
```
For this reason, it is best to use interfaces for types that are used with the implements heritage clause.

* TypeScript interfaces are “open”, meaning that unlike in type aliases, you can have multiple declarations in the same scope:
```ts
interface AnimalLike {
  isAlive(): boolean
}
function feed(animal: AnimalLike) {
  animal.eat

  animal.isAlive
}
 
// SECOND DECLARATION OF THE SAME NAME
interface AnimalLike {
  eat(food): void
}
```
These declarations are merged together to create a result identical to what you would see if both the isAlive and eat methods were on a single interface declaration.

### Choosing which to use
In many situations, either a type alias or an interface would be perfectly fine, however…

* If you need to define something other than an object type (e.g., use of the | union type operator), you must use a type alias
* If you need to define a type to use with the implements heritage term, it’s best to use an interface
* If you need to allow consumers of your types to augment them, you must use an interface.

### Recursion
Recursive types, are self-referential, and are often used to describe infinitely nestable types. For example, consider infinitely nestable arrays of numbers

```ts
type NestedNumbers = number | NestedNumbers[]
 
const val: NestedNumbers = [3, 4, [5, 6, [7], 59], 221]
 
if (typeof val !== "number") {
  val.push(41)
  // Below Line ERROR: Argument of type 'string' is not assignable to parameter of type 'NestedNumbers'.
  val.push("this will not work")
}
```

## Functions

`void` is a special type, that’s specifically used to describe function return values. It has the following meaning:

```The return value of a void function is intended to be ignored```

### Constructor Signatures
Construct signatures are similar to call signatures, except they describe what should happen with the new keyword.
```ts
interface DateConstructor {
  new (value: number): Date
}
 
let MyDateConstructor: DateConstructor = Date
const d = new MyDateConstructor()
```

### Function overloads
* There should be a declaration followed after the overloading function definition
* All the overloaded functions should be exported

### Function type best practices
* Explicitly define return types

## Classes
* JS Classes private fields are followed #. `#fields`
* `readonly`: While not strictly an access modifier keyword (because it has nothing to do with visibility), TypeScript provides a readonly keyword that can be used with class fields.
* Note the following order of what ends up in the class constructor:

  * super()
  * param property initialization
  * other class field initialization
  * anything else that was in your constructor after super()
  * Also note that, while it is possible in JS to put stuff before super(), the use of class field initializers or param properties disallows this:
```js
class Base {}
 
class Car extends Base {
  foo = console.log("class field initializer")
  constructor(public make: string) {
    console.log("before super")
    super()
    console.log("custom constructor stuff")
  }
}
 
const c = new Car("honda")
```

## Top and Bottom Types

### Top Types
`any`: You can think of values with an any type as “playing by the usual JavaScript rules”.
`unknown`: unknown is different from any in a very important way, i.e: Values with an unknown type cannot be used without first applying a type guard
```ts
// ERROR: Accessing `myUnknown.it.is.possible.to.access.any.deep.property` Object is of type 'unknown'.
let myUnknown: unknown = 14
         
// Correct Way: Using Type guard
// This code runs for { myUnknown| anything }
if (typeof myUnknown === "string") {
  // This code runs for { myUnknown| all strings }
  console.log(myUnknown, "is a string")
                 
let myUnknown: string
} else if (typeof myUnknown === "number") {
  // This code runs for { myUnknown| all numbers }
  console.log(myUnknown, "is a number")
                 
let myUnknown: number
} else {
  // this would run for "the leftovers"
  //       { myUnknown| anything except string or numbers }
}
```
**Practical use of top types:**
*  if you ever convert a project from JavaScript to TypeScript, it’s very convenient to be able to incrementally add increasingly strong types.
* `unknown` is great for values received at runtime (e.g., your data layer). By obligating consumers of these values to perform some light validation before using them, errors are caught earlier, and can often be surfaced with more context.

### Bottom Type
[`never`](https://www.typescript-training.com/course/fundamentals-v3/11-top-and-bottom-types/#exhaustive-conditionals): approach works nicely with a switch statement, when the UnreachableError is thrown from the default case clause.

## Type Guards
### Built-in typeguards
Refer to `typeguards.ts`

### [User-defined type guards](https://www.typescript-training.com/course/fundamentals-v3/12-type-guards/#writing-high-quality-guards)
**value is Foo**: The first kind of user-defined type guard we will review is an is type guard. It is perfectly suited for our example above because it’s meant to work in cooperation with a control flow statement of some sort, to indicate that different branches of the “flow” will be taken based on an evaluation of valueToTest’s type. Pay very close attention to isCarLike’s return type
```ts
interface CarLike {
  make: string
  model: string
  year: number
}
 
let maybeCar: unknown
 
// the guard
function isCarLike(
  valueToTest: any
): valueToTest is CarLike {
  return (
    valueToTest &&
    typeof valueToTest === "object" &&
    "make" in valueToTest &&
    typeof valueToTest["make"] === "string" &&
    "model" in valueToTest &&
    typeof valueToTest["model"] === "string" &&
    "year" in valueToTest &&
    typeof valueToTest["year"] === "number"
  )
}
 
// using the guard
if (isCarLike(maybeCar)) {
  maybeCar
  // Typehint: let maybeCar: CarLike
}
```

**asserts value is Foo**: There is another approach we could take that eliminates the need for a conditional. Pay very close attention to assertsIsCarLike’s return type:

```ts
interface CarLike {
  make: string
  model: string
  year: number
}
 
let maybeCar: unknown
 
// the guard
function assertsIsCarLike(
  valueToTest: any
): asserts valueToTest is CarLike {
  if (
    !(
      valueToTest &&
      typeof valueToTest === "object" &&
      "make" in valueToTest &&
      typeof valueToTest["make"] === "string" &&
      "model" in valueToTest &&
      typeof valueToTest["model"] === "string" &&
      "year" in valueToTest &&
      typeof valueToTest["year"] === "number"
    )
  )
    throw new Error(
      `Value does not appear to be a CarLike${valueToTest}`
    )
}
 
// using the guard
maybeCar
   
let maybeCar: unknown
assertsIsCarLike(maybeCar)
maybeCar
// Typehint: let maybeCar: CarLike
```