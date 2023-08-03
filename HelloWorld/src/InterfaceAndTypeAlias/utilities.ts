import { SpecialDate, UserContactInfo, UserInfo } from "./types"
function printContactInfo(info: UserContactInfo) {
    console.log(info)
    console.log(info.email)
}
const painter = {
    name: "Robert Ross",
    email: "bross@pbs.org",
    favoriteColor: "Titanium White",
}

printContactInfo(painter) // totally fine

const newYear: SpecialDate = {
    ...new Date(),
    getReason: () => "last day of the year"
}
console.log(newYear.getReason())

function printUserInfo(info: UserInfo) {
    console.log(info.name)
}
