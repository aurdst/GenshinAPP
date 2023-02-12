<template>
    <v-container>
        <v-row>
            <v-col cols='12'>
                <v-img src="../../assets/img/Header_coffre_anniv.png"></v-img>

                <v-card>
                    <div>
                        <br>
                        <v-img src="../../assets/img/Cristal.png" class="intoWinImg"></v-img>
                        <p>x 1980 Crital primaire</p>
                        <br>
                    </div>

                    <div>
                        <br>
                        <v-img src="../../assets/img/Faveur.png" class="intoWinImg"></v-img>
                        <p>x 1 Faveur de l'astre de la nuit</p>
                        <br>
                    </div>

                    <div>
                        <br>
                        <v-img src="../../assets/img/coffrePB.png" class="intoWinImg"></v-img>
                        <p>x 1 PB</p>
                        <br>
                    </div>
                </v-card>
                <router-link to="/end">
                    <v-img src="../../assets/img/Reclamerrecompense.png" ></v-img>
                </router-link>
            </v-col>
        </v-row>
    </v-container>

</template>
<style scoped>
.intoWinImg{
    width: 80px;
    display: block;
    margin: auto;
}

p{
    text-align: center;
    font-family: Genshin;
    font-weight: 900;
}

.v-card.v-theme--light.v-card--density-default.v-card--variant-elevated{
    width: 350px!important;
    display: block;
    margin: auto;
}

.HeadBottom{
    background-color: rgba(5, 55, 5, 0);
}

</style>
<script>
    export default {
        name: 'WinCard',
        // props: ["showWin", "toggleShowWin"]
    }

</script>