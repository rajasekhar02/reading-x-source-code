// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<Concat<[], []>, []>>,
  Expect<Equal<Concat<[], [1]>, [1]>>,
  Expect<Equal<Concat<[1, 2], [3, 4]>, [1, 2, 3, 4]>>,
  Expect<Equal<Concat<['1', 2, '3'], [false, boolean, '4']>, ['1', 2, '3', false, boolean, '4']>>,
]


// ============= Your Code Here =============
/**
 * Learn about spread operator can be used on the types also
 */
type Concat<T, U> = T extends any[] ? U extends any[] ? [...T, ...U] : T : U extends any[] ? U : never
