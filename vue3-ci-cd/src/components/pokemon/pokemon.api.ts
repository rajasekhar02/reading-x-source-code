import axios from 'axios'

const axiosClient = axios.create({
    baseURL: 'https://pokeapi.co/api/v2'
})

type Pokemon = {
    id: number
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
    let listPokemons: Pokemon[] = []
    if (cacheValue == undefined) {
        let payload = await axiosClient.get<PokemonAPIPayload>("/pokemon?limit=5&offset=0")
        let result: PokemonAPIPayload = payload.data
        listPokemons = result.results.map(x => {
            let matches = x.url.split("pokemon");
            if (matches.length < 2) {
                return {
                    name: x.name,
                    url: "https://picsum.photos/200"
                }
            }
            let pokemonId = (matches[1]).substring(1, matches[1]?.length - 1)
            // pokemonId = pokemonId.substring(1, matches.length - 1)
            // console.log(pokemonId)
            return {
                id: pokemonId,
                name: x.name,
                url: `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/${pokemonId}.svg`
            }
        })
        localStorage.setItem("fivePokemons", JSON.stringify(listPokemons))

    } else {
        listPokemons = JSON.parse(cacheValue)
    }
    return listPokemons
}

export default {
    getPokemons
}