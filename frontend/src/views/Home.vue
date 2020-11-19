<template>
<div>
  <div>
    <div v-if="discoveringRokus">
      Finding Roku devices...
    </div>
    <div v-else>
      <div v-if="noRokus">
        No Roku devices found.
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
  </div>
  <div v-if="rokuHost">
    <button @click="apiPress('info')">info</button>
    <button @click="apiPress('select')">select</button>
    <button @click="apiPress('up')">up</button>
    <button @click="apiPress('down')">down</button>
    <button @click="apiPress('left')">left</button>
    <button @click="apiPress('right')">right</button>
    <button @click="apiPress('back')">back</button>
    <button @click="apiPress('home')">home</button>
  </div>
</div>
</template>

<script>
const axios = require('axios')

export default {
  computed: {
    noRokus () {
      return this.rokuHosts.length == 0
    },
  },
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
    async apiPress (button) {
      await axios.get(`/api/press/${button}`)
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
