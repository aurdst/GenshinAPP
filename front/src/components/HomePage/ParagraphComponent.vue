<template>
    <v-container>
        <v-row no-gutters>
            <v-col class="container_paragraph" cols="12">
                <h2 class="anniv text-center">Félicitations !</h2>
                <div id="line"></div>
                <h3 class="para text-center">
                    Récupérez vos récompenses
                </h3>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>

.container_paragraph{
    position: relative;
    top: -100px;
}
.anniv{
    font-family: 'Genshin';
    font-weight: bolder;
    position: relative;
    z-index: 2;
    color: white;
    font-size: 2.3em;
}

.para{
    font-family: 'Genshin';
    font-weight: bolder;
    position: relative;
    color: #fff;
    z-index: 2;
    font-size: 1.5em;
}
#line{
    width: 50%;
    height: 4px;
    border-radius: 20px;
    position: relative;
    display: block;
    z-index: 2;
    margin: auto;
    margin-bottom: 10px;
    background-color: white;
}

</style>

<script>
 export default {
    name: 'ParagraphComponent'
 }
</script>