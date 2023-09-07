// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<Last<[2]>, 2>>,
  Expect<Equal<Last<[3, 2, 1]>, 1>>,
  Expect<Equal<Last<[() => 123, { a: string }]>, { a: string }>>,
]


// ============= Your Code Here =============
// My Solution: T extends [infer K, ...infer R] ? Last<R> extends never ? K : Last<R> : never
// Other Solution 1: [any, ...T][T["length"]]
// Other Solution 2: T extends [...infer _, infer L] ? L : never
type Last<T extends any[]> = T extends [infer K, ...infer R] ? Last<R> extends never ? K : Last<R> : never
