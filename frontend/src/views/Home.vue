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
    <div>
      <img src="/roku-remote.png" alt="Roku remote" usemap="#rokumap"/>
      <map name="rokumap">
        <area shape="rect" coords="124,34,175,86" title="Power" @click="apiPress('power')"/>
        <area shape="rect" coords="40,138,139,187" title="Back" @click="apiPress('back')"/>
        <area shape="rect" coords="161,138,260,187" title="Home" @click="apiPress('home')"/>
        <area shape="rect" coords="112,286,186,356" title="OK" @click="apiPress('select')"/>
        <area shape="rect" coords="49,286,111,356" title="Left" @click="apiPress('left')"/>
        <area shape="rect" coords="187,286,254,356" title="Right" @click="apiPress('right')"/>
        <area shape="rect" coords="112,219,186,285" title="Up" @click="apiPress('up')"/>
        <area shape="rect" coords="112,357,186,425" title="Down" @click="apiPress('down')"/>
        <area shape="rect" coords="36,519,82,588" title="Reverse" @click="apiPress('reverse')"/>
        <area shape="rect" coords="101,519,200,588" title="Play/Pause" @click="apiPress('play')"/>
        <area shape="rect" coords="218,519,260,588" title="Forward" @click="apiPress('forward')"/>
        <area shape="rect" coords="39,460,110,502" title="Replay" @click="apiPress('replay')"/>
        <area shape="rect" coords="125,460,176,502" title="Search/Voice" @click="apiPress('search')"/>
        <area shape="rect" coords="196,460,260,502" title="Info" @click="apiPress('info')"/>
        <area shape="rect" coords="284,409,306,457" title="Mute" @click="apiPress('mute')"/>
      </map>
    </div>
    <div>
      <label>
        Type text:
        <input type="text" v-model="literalText" />
      </label>
      <button @click="sendLiteral">Enter</button>
    </div>
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
      literalText: '',
      rokuHost: null,
      rokuHosts: [],
    }
  },
  methods: {
    async apiPress (button) {
      await axios.get(`/api/press/${button}`)
    },
    async sendLiteral () {
      await axios.post(
        '/api/literal',
        {string: this.literalText}
      )
      this.literalText = ''
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

<style lang="scss">
img {
  margin: 2rem;
}
map {
  area {
    cursor: pointer;
  }
}
</style>
