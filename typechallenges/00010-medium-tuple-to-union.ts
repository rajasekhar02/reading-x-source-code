// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<TupleToUnion<[123, '456', true]>, 123 | '456' | true>>,
  Expect<Equal<TupleToUnion<[123]>, 123>>,
]


// ============= Your Code Here =============
// My Solution: type TupleToUnion<T extends readonly any[]> = keyof { [P in T[number]]: T[P] }
type TupleToUnion<T extends readonly any[]> = T extends Array<infer IT> ? IT : never

