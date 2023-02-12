<template>
  <v-container>
    <TopComponent />
    <BannerEventComponent />
    <!-- <ItemPlumeComponent /> -->
    <!-- <ItemSabComponent /> -->
    <!-- <ItemFleurMioComponent /> -->
    <MioComponent />
    <EffectMioComponent/>
    <KazuhaComponent />
    <EffectKazuhaComponent />
    <ParagraphComponent />
    <BGMoraComponent/>
    <!-- <WinCard/> -->
    <BottomComponent />
  </v-container>
</template>

<script>
import { defineComponent } from 'vue';

// Components
import TopComponent from '@/components/HomePage/TopComponent.vue';
import BottomComponent from '@/components/HomePage/BottomComponent.vue'
import BannerEventComponent from '@/components/HomePage/BannerEventComponent.vue'
// import ItemPlumeComponent from '@/components/ItemPlumeComponent.vue'
// import ItemSabComponent from '@/components/ItemSabComponent.vue'
// import ItemFleurMioComponent from '@/components/FlowerMioComponent.vue'
import MioComponent from '@/components/HomePage/MioComponent.vue'
import EffectMioComponent from '@/components/HomePage/EffectMioComponent.vue'
import KazuhaComponent from '@/components/HomePage/KazuhaComponent.vue'
import EffectKazuhaComponent from '@/components/HomePage/EffectKazuhaComponent.vue'
import ParagraphComponent from '@/components/HomePage/ParagraphComponent.vue'
import BGMoraComponent from '@/components/HomePage/BGMoraComponent.vue'
// import WinCard from '@/components/WinCard.vue'

export default defineComponent({
  name: 'HomeView',

  components: {
    TopComponent,
    BannerEventComponent,
    // ItemPlumeComponent,
    // ItemSabComponent,
    // ItemFleurMioComponent,
    MioComponent,
    EffectMioComponent,
    KazuhaComponent,
    EffectKazuhaComponent,
    ParagraphComponent,
    BGMoraComponent,
    BottomComponent,
    // WinCard
  },
});
</script>
 