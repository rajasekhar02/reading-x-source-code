// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

const promiseAllTest1 = PromiseAll([1, 2, 3] as const)
const promiseAllTest2 = PromiseAll([1, 2, Promise.resolve(3)] as const)
const promiseAllTest3 = PromiseAll([1, 2, Promise.resolve(3)])
const promiseAllTest4 = PromiseAll<Array<number | Promise<number>>>([1, 2, 3])

type cases = [
  Expect<Equal<typeof promiseAllTest1, Promise<[1, 2, 3]>>>,
  Expect<Equal<typeof promiseAllTest2, Promise<[1, 2, number]>>>,
  Expect<Equal<typeof promiseAllTest3, Promise<[number, number, number]>>>,
  Expect<Equal<typeof promiseAllTest4, Promise<number[]>>>,
]


// ============= Your Code Here =============
type PromiseType<L> = L extends Promise<infer LType> ? LType : L
// type Return<Values extends any[]> = Values extends [infer L, ...infer REST] ? [PromiseType<L>, ...Return<REST>] : []
type Return<Values> = { [K in keyof Values]: PromiseType<Values[K]> }

// TIPS 1: Using unknown instead of any to prevent from lint errors
// TIPS 2: Thinking an Array as Object also helpful in resolving types
// TIPS 3: Using Recursion to loop over the types
// TIPS 4: Using infer to create type variables
declare function PromiseAll<Values extends readonly unknown[]>(values: readonly [...Values]): Promise<Return<Values>>
