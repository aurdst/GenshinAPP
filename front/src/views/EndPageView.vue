<template>
  <v-container>
    <TopComponent/>
    <router-link to="/">
      <v-btn>Retour</v-btn>
    </router-link>
  </v-container>
</template>

<style scoped>
</style>

<script>
import TopComponent from '@/components/HomePage/TopComponent.vue';

  export default {
    name: 'EndPage',

    components: {
      TopComponent
    }
  }

</script>