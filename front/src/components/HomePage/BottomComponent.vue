<template>
    <v-container>
        <v-row no-gutters>
            <v-col cols="12">
                <v-img src="../../assets/img/BGKazuha.png" alt="BGKazuha" class="mx-0 BGKazuha"/>
                <p class="p_copy">Design ADSTDesign</p>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
 export default {
    name: 'BottomComponent'
 }
</script>

<style scooped>

.BGKazuha{
    position: absolute;
    bottom: 0px;
    opacity: .6;
    z-index: 0;
    width: 100%;
}


.p_copy{
    bottom: 0px;
    color: white;
    text-align: center;
    position: relative;
}
</style>