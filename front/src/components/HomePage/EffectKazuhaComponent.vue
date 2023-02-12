<template>
    <v-container>
        <v-row no-gutters>
            <v-col cols="12">
                <v-img src="../../assets/img/BGKazuhaDiago.png" class="effect"></v-img>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
.effect{
    position: relative;
    width: 100%;
    z-index: 2;
    top: -200px;
    animation: animate 5s linear infinite;
}


@keyframes animate {
    0%,100%{
        transform: translateY(-35px);

    }
    50%{
        transform: translateY(-10px);
    }
}
</style>

<script>
 export default {
    name: 'EffectKazuhaComponent'
 }
</script>