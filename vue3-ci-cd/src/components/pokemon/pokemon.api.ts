import axios from 'axios'

const axiosClient = axios.create({
    baseURL: 'https://pokeapi.co/api/v2'
})

type Pokemon = {
    name: string
    url: string
}

type PokemonAPIPayload = {
    count: number;
    next?: string;
    previous?: string;
    results: Pokemon[]
}

export async function getPokemons(): Promise<Pokemon[]> {
    let cacheValue = localStorage.getItem("fivePokemons")
    if (cacheValue == undefined) {
        let payload = await axiosClient.get<PokemonAPIPayload>("/pokemon?limit=5&offset=0")
        let result: PokemonAPIPayload = payload.data
        localStorage.setItem("fivePokemons", JSON.stringify(result.results))
        return result.results
    } else {
        return JSON.parse(cacheValue)
    }
}

export default {
    getPokemons
}