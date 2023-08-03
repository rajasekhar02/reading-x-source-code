let value:
    | Date
    | null
    | undefined
    | "pineapple"
    | [number]
    | { dateRange: [Date, Date] }

// instanceof
if (value instanceof Date) {
    value
}
// typeof
else if (typeof value === "string") {
    value
}
// Specific value check
else if (value === null) {
    value
}
// Truthy/falsy check
else if (!value) {
    value
}
// Some built-in functions
else if (Array.isArray(value)) {
    value
}
// Property presence check
else if ("dateRange" in value) {
    value
} else {
    value
}