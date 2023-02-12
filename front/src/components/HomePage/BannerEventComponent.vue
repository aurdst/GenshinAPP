<template>
    <v-container>
        <v-row no-gutters>
            <v-col cols="12">
                <v-img src="../../assets/img/event_banner.png" width="280" class="mx-auto mt-16 EventBanner"></v-img>
                <v-img src="../../assets/img/DateBanner.png" width="150" class="mx-auto topBanner"></v-img>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
.topBanner{
    position: relative;
    top: 47px;
}

.EventBanner{
    top: 50px;
}
</style>

<script>
 export default {
    name: 'BannerEventComponent'
 }
</script>