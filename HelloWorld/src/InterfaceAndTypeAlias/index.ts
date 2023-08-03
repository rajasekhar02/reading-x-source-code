/**
 * Type aliases help to address this, by allowing us to:
 * define a more meaningful name for this type
 * declare the particulars of the type in a single place
 * import and export this type from modules, the same as if it were an exported value
 * 
 * If we look at the declaration syntax for a moment

    ```ts
    type UserContactInfo = {
        name: string
        email: string
    }
    ```

    1. This is a rare occasion where we see type information on the right hand side of the assignment operator (=)
    2. We’re using TitleCase to format the alias’ name. This is a common convention
    3. As we can see below, we can only declare an alias of a given name once within a given scope. This is kind of like how a let or const variable declaration works

 */

import { UserInfoOutcome } from "./with-alias"
/**
 * CLEANED UP version
 */
export function maybeGetUserInfo(): UserInfoOutcome {
    // implementation is the same in both examples
    if (Math.random() > 0.5) {
        return [
            "success",
            { name: "Mike North", email: "mike@example.com" },
        ]
    } else {
        return [
            "error",
            new Error("The coin landed on TAILS :("),
        ]
    }
}
// In