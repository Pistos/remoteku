<template>
<div>
  <div>
    <div v-if="discoveringRokus">
      Finding Roku devices...
    </div>
    <div v-else>
      <div v-if="! rokuHost">
        Choose a Roku device:
      </div>
      <div v-for="(host, index) in rokuHosts" :key="host">
        <input type="radio" :id="`roku-${index}`" :value="host" v-model="rokuHost" />
        <label for="`roku-${index}`">{{host}}</label>
      </div>
    </div>
  </div>
  <div v-if="rokuHost">
    <button @click="apiInfo">info</button>
    <button @click="apiSelect">select</button>
    <button @click="apiUp">up</button>
    <button @click="apiDown">down</button>
    <button @click="apiLeft">left</button>
    <button @click="apiRight">right</button>
    <button @click="apiBack">back</button>
    <button @click="apiHome">home</button>
  </div>
</div>
</template>

<script>
const axios = require('axios')

export default {
  async created () {
    this.discoveringRokus = true
    const res = await axios.get('/api/discover')
    this.rokuHosts = res.data
    this.discoveringRokus = false
  },
  data: function () {
    return {
      discoveringRokus: false,
      rokuHost: null,
      rokuHosts: [],
    }
  },
  methods: {
    async apiBack () {
      await axios.get('/api/back')
    },
    async apiDown () {
      await axios.get('/api/down')
    },
    async apiHome () {
      await axios.get('/api/home')
    },
    async apiInfo () {
      await axios.get('/api/info')
    },
    async apiLeft () {
      await axios.get('/api/left')
    },
    async apiRight () {
      await axios.get('/api/right')
    },
    async apiSelect () {
      await axios.get('/api/select')
    },
    async apiUp () {
      await axios.get('/api/up')
    },
  },
  name: 'Home',
  watch: {
    async rokuHost (newHost) {
      await axios.put(
        '/api/choose-roku',
        {host: newHost}
      )
    },
  },
}
</script>
