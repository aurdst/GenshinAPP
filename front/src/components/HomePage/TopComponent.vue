<template>
    <v-container>
        <v-row no-gutters> 
            <v-col cols="12">
                <v-img src="../../assets/img/BGMio.png" width="100%" height="auto" alt="BGMio" class="mx-0 BGMio"/>
            </v-col>
        </v-row>

        <v-row no-gutters>
            <v-col>
                <v-img src="../../assets/img/LogoGenshin.png" width="170" class="mx-auto mt-5"></v-img>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
 export default {
    name: 'TopComponent'
 }
</script>

<style scooped>

.v-container{
    margin: 0;
    padding: 0;
}

.BGMio{
    position: absolute;
    animation: animate 5s linear infinite;
    opacity: 0.5;
}

@keyframes animate {
    0%,100%{
        opacity: 0.2;
    }
    55%{
        opacity: 0.4;
    }
}
</style>