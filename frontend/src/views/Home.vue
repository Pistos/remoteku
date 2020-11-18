<template>
<div>
  <h3>Roku:</h3>
  <div>
    <div v-for="(host, index) in rokuHosts" :key="host">
      <input type="radio" :id="`roku-${index}`" :value="host" v-model="rokuHost" />
      <label for="`roku-${index}`">{{host}}</label>
    </div>
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
    async select () {
      const res = await axios.get('/api/select')
      console.log(res)
    },
  },
  name: 'Home',
}
</script>
