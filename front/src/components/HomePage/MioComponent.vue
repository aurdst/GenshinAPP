<template>
    <v-container>
        <v-row no-gutters>
            <v-col cols="12">
                <v-img src="../../assets/img/Mio.png" width="400" class="MioComponent"></v-img>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
.MioComponent{
    animation: animate 3s linear infinite;
    top: 100px;
    z-index: 2;
}

@keyframes animate {
    0%,100%{
        transform: translateY(5px);
    }
    50%{
        transform: translateY(20px);
    }
}
</style>

<script>
 export default {
    name: 'MioComponent'
 }
</script>