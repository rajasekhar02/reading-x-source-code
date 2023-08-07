export interface TwoNumberCalculation {
    calculator: (x: number, y: number) => number
}

// Call Signatures
export interface TwoNumberCalculationFunction {
    (x:number, y:number): number
}

export type TwoNumberCalc = (x: number, y: number) => number

// Constructor Signatures
export interface DateConstructor {
    new(value: number): Date
}

// Function Overloading
type FormSubmitHandler = (data: FormData) => void
type MessageHandler = (evt: MessageEvent) => void

export function handleMainEvent(elem: HTMLFormElement, handler: FormSubmitHandler): void
export function handleMainEvent(elem: HTMLIFrameElement, handler: MessageHandler): void

// There should be a declaration followed after the overloading function definition
// All the overloaded functions should be exported
export function handleMainEvent(elem: HTMLFormElement | HTMLIFrameElement, handler: FormSubmitHandler | MessageHandler) { }