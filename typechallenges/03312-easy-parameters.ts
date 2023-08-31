// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

const foo = (arg1: string, arg2: number): void => { }
const bar = (arg1: boolean, arg2: { a: 'A' }): void => { }
const baz = (): void => { }

type cases = [
  Expect<Equal<MyParameters<typeof foo>, [string, number]>>,
  Expect<Equal<MyParameters<typeof bar>, [boolean, { a: 'A' }]>>,
  Expect<Equal<MyParameters<typeof baz>, []>>,
]


// ============= Your Code Here =============
// Learning: all place infer in the place of the specifying type i.e (...args: <placeholder for type>) => <placeholder for type> => (...args: infer FP) => infer RT
type MyParameters<T extends (...args: any[]) => any> = T extends (...args: infer F) => any ? F : never
