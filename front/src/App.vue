<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
}
</script>

<style scoped>
main{
  overflow-x: hidden;
  height: 100vh;
  background: #0f0c29;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #000000, #11101f, #000000);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #000000, #11101f, #000000); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
</style>