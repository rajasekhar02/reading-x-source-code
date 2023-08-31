// ============= Test Cases =============
import type { Equal, Expect } from './test-utils'

type cases = [
  Expect<Equal<DeepReadonly<X1>, Expected1>>,
  Expect<Equal<DeepReadonly<X2>, Expected2>>,
]

type X1 = {
  a: () => 22
  b: string
  c: {
    d: boolean
    e: {
      g: {
        h: {
          i: true
          j: 'string'
        }
        k: 'hello'
      }
      l: [
        'hi',
        {
          m: ['hey']
        },
      ]
    }
  }
}

type X2 = { a: string } | { b: number }

type Expected1 = {
  readonly a: () => 22
  readonly b: string
  readonly c: {
    readonly d: boolean
    readonly e: {
      readonly g: {
        readonly h: {
          readonly i: true
          readonly j: 'string'
        }
        readonly k: 'hello'
      }
      readonly l: readonly [
        'hi',
        {
          readonly m: readonly ['hey']
        },
      ]
    }
  }
}

type Expected2 = { readonly a: string } | { readonly b: number }


// ============= Your Code Here =============
/* Learnings:
 My Solution(Wrong,not working): { readonly [K in keyof T]: T[K] extends { [L: string]: any } ? DeepReadonly<T[K]> : T[K] }
                           Diff:                           vvvvvv              vvvvv
              Solution(Working): { readonly [K in keyof T]: keyof T[K] extends never ? T[K] : DeepReadonly<T[K]> }
Correct Solution idea:
1. By checking keyof T[K] we can find the type having keys so if it doesnot have keys then it should T[K] otherwise DeepReadonly<T[K]>
*/
type DeepReadonly<T> = { readonly [K in keyof T]: keyof T[K] extends never ? T[K] : DeepReadonly<T[K]> }
