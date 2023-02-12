<template>
    <v-container>
        <v-row no-gutters>
            <v-col cols="12" class="container_coffre">
                <v-img src="../../assets/img/BGMora.png" class="mora"></v-img>
                <v-img src="../../assets/img/CoffreAnniv.png" alt="coffre" class="coffre_anniv"/>
                <v-btn class="btn" v-on:click="toggleShowWin">
                    Ouvrir
                </v-btn>
                <win-card v-if="showWin" class="win"/>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
.container_coffre{
    position: relative;
    top: -100px;
}
.mora{
    position: relative;
    width: 100%;
    z-index: 2;
    animation: animate 20s linear infinite;
}


.btn{
    display: block;
    margin: auto;
    text-transform: capitalize;
    font-weight: bolder;
    font-size: 1.4em;
    color: black;
    position: relative;
    top: -100px;
    padding: 28px;
    border-radius: 50px;
    width: 43%;
    z-index: 2;
    text-align: center;
    line-height: 0;
    font-family: 'Noto Serif Khojki', serif;
}
.coffre_anniv{
    width: 30%;
    position: relative;
    z-index: 2;
    top: -250px;
    display: block;
    margin: auto;
}

.win{
    position: absolute;
    top: -50px;
    z-index: 99;
}

@keyframes animate {
    0%,100%{
        rotate: 0deg;
    }
    50%{
        rotate: 130deg;
    }
}
</style>

<script>
import WinCard from './WinCard.vue'

 export default {
    components: { WinCard },

    name: 'BGMoraComponent',

    data () {
        return {
            showWin: false,
        }
    },

    methods: {
        toggleShowWin: function() {
            this.showWin = !this.showWin
        }
    }
 }
</script>