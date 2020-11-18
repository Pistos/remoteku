<template>
<div>
  <h3>Roku:</h3>
  <div>
    <div v-for="(host, index) in rokuHosts" :key="host">
      <input type="radio" :id="`roku-${index}`" :value="host" v-model="rokuHost" />
      <label for="`roku-${index}`">{{host}}</label>
    </div>
  </div>
  <div>
    <button @click="apiInfo">info</button>
    <button @click="apiSelect">select</button>
    <button @click="apiUp">up</button>
    <button @click="apiDown">down</button>
    <button @click="apiLeft">left</button>
    <button @click="apiRight">right</button>
  </div>
</div>
</template>

<script>
const axios = require('axios')

export default {
  async created () {
    const res = await axios.get('/api/discover')
    this.rokuHosts = res.data
  },
  data: function () {
    return {
      rokuHost: null,
      rokuHosts: [],
    }
  },
  methods: {
    async apiDown () {
      await axios.get('/api/down')
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
