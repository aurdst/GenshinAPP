<template>
    <v-container>
        <v-row no-gutters>
            <v-col cols="12">
                <v-img src="../../assets/img/BGMioDiago.png" class="effect"></v-img>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
.effect{
    position: relative;
    z-index: 2;
    width: 100%;
    top: -100px;
    animation: animate 5s linear infinite;
}

@keyframes animate {
    0%,100%{
        transform: translateY(0px);

    }
    50%{
        transform: translateY(10px);
    }
}
</style>

<script>
 export default {
    name: 'EffectMioComponent'
 }
</script>