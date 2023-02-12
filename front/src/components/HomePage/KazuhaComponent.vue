<template>
    <v-container>
        <v-row no-gutters>
            <v-col cols="12">
                <v-img src="../../assets/img/Kazuha.png" width="600" class="kazuha"></v-img>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
.kazuha{
    width: 100%;
    position: relative;
    z-index: 2;
    top: -100px;
}
</style>

<script>
 export default {
    name: 'KazuhaComponent'
 }
</script>