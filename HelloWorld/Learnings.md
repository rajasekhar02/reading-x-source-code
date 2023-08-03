A good way to think of TS files:

* .ts files contain both type information and code that runs
* .js files contain only code that runs
* .d.ts files contain only type information


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