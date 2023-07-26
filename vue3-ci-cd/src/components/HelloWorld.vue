<script async setup lang="ts">
import { ref,onMounted } from 'vue'
import type {Ref} from "vue"
import {getPokemons} from "./pokemon/pokemon.api.ts"
defineProps<{ msg: string }>()
type Pokemon = {
    name: string
    url: string
}
const count = ref(0)
const rectFivePokemons:Ref<Pokemon[]> = ref([])
onMounted(async ()=>{
  const fivePokemons = await getPokemons()
  rectFivePokemons.value = fivePokemons
})

</script>

<template>
  <ul v-if="rectFivePokemons.length > 0">
    <li v-for="pokemon in rectFivePokemons">
      <span>
        <img :src="pokemon.url">
      </span> 
      {{pokemon.name}}
    </li>
    <li></li>
  </ul>
  <ul v-else>No Pokemons</ul>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
