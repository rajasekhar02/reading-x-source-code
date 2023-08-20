import axios from 'axios'

const BASE_URL = 'https://jsonplaceholder.typicode.com'

type Geo = {
    lat: number,
    lng: number
}

type Address = {
    street: string,
    suite: string,
    city: string,
    zipcode: string,
    geo: Geo
}

type Company = {
    name: string,
    catchPhrase: string,
    bs: string
}

type User = {
    id: number,
    name: string,
    username: string,
    email: string,
    address: Address,
    phone: string,
    website: string,
    company: Company
}

export const fetchUsers = async () => {
  return (await axios.get<User>(`${BASE_URL}/users`)).data
}

export const createUser = async (user: User) => {
  return (await axios.post<User>(`${BASE_URL}/users`, user)).data
}