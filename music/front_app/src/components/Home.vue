<template>
<div class="Home">
   <div class="barra_menu"> 
          <h5>Nombre Web</h5> 
          <h4><a href="#/"><span class="link_buscar">BUSCAR</span></a></h4>
          <h4><a href="#/insert"><span class="link_agregar">AGREGAR DATOS</span></a></h4>
          <hr>
    </div>
    <div class="cabecera">
      <center>
        <h3 >Bienvenido! </h3>
        <img  src="../assets/a.png" height="100" width="100">
      </center>
    </div>
    <div class="buscador">
      <input id="texto" class="inputBuscar" type="text" placeholder="Buscar canción.."/>
      <select class="selectBuscar" id="opciones" >
                    <option value="1">Título</option>
                    <option value="2">Autor/Grupo</option>
                    <option value="1">Género</option>
      </select>
      <input class="inputBoton"  type="button" value="Buscar" v-on:click="buscar">

    </div>
    <div class="resultados">
      <center><h2>Resultados...</h2></center>
      <table v-for="data in res" class="cajas">
        <tr>
          <td colspan="2">
             <img  src="../assets/album.png" height="90" width="90">
          </td>
          <td colspan="2">
            <label><b>Nombre canción:</b></label>
          </td> 
          <td>
            {{data.nombrecancion}}
          </td>
        </tr>
        <tr>
          <td colspan="2" > 
             <center><label ><b>03:24 </b></label></center>
          </td>
           <!--<td >
            <label ><b>Autor </b></label>
          </td> 
          <td>
            {{data.nombrecancion}}
          </td>-->
        </tr>
        <tr>
          <td colspan="2">
          </td>
           <td  >
            <label ><b>Álbum: </b></label>
          </td> 
          <td>
            {{data.albumcancion}}
          </td>
        </tr>
        <tr>
          <td colspan="2">
          </td>
         
           <td colspan="2" >
              
          </td>
          <td >
              <a href="javascript:play()"><img  src="../assets/y-play.png" height="40" width="40" v-on:click="buscar"></a>
              <a href="javascript:descargar()"><img  src="../assets/des.png" height="40" width="40"></a>
          </td>
        </tr>
      </table>
      
     
      
    </div>
   
    
  </div>
</template>

<script>
export default {
  
  data () {
    return {
      res:[]
    }
  },
  methods: {
      buscar: function(){
        var texto = document.getElementById('texto').value
        var opciones = document.getElementById('opciones')
        var tipoBusqueda = opciones.options[opciones.selectedIndex].value
        console.log("esto se buscara "+texto)
        console.log("tipo de busqueda  "+tipoBusqueda)
        if (tipoBusqueda==1){
            console.log("entroo aquii")
            this.$http.get('http://localhost:5000/busquedaNC?cancion='+texto)
            .then(response =>{
                this.res = response.body.resultados
                console.log(this.res[0])
                }, response =>{
                    console.log("falla ")
                });
        }
        else if (tipoBusqueda=="2"){
               this.$http.get('http://localhost:5000/busquedaAC?autor='+texto)
                .then(response =>{
                this.res = response.body.resultados
                console.log(this.res[1])
                }, response =>{
                    console.log("falla ")
                });
        }
        else{
           this.$http.get('http://localhost:5000/busquedaGC?genero='+texto)
            .then(response =>{
                this.res = response.body.resultados
                console.log(this.res[0])
                }, response =>{
                    console.log("falla ")
                });
        }
        
      }

  }
}

</script>

<style>
.Home {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #aa2e95;
}

a{
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #aa2e95;
}
a:hover{
  color: #8a2be2;
}
.barra_menu{
  background-color: #2fc0da;
  position:absolute; top:0px; left: 0px; right: 0px;
  text-align: left;
  
}

.link_buscar{
  position: absolute;; top:20px; right: 200px;
  
}
.link_agregar{
  position: absolute;; top:20px; right: 40px;
  
}
.cabecera{
  background-color:#2fc0da;
  position:absolute; top:62px; left: 0px; right: 0px;
  height: 180px;
  
}



.buscador {
  background-color:#c3d6e9;
  position:absolute; top:240px; left: 0px; right: 0px;
  height: 150px;
}

.resultados{
  background-color:#c3d6e9;
  position:absolute; top:360px; left: 0px; right: 0px; bottom: 0px;
  width: auto;
  height: auto;
}

hr { 
    display: block;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
    margin-left: auto;
    margin-right: auto;
    border-style:dotted;
    border-width: 0.5px;
    color:#d3d8f0;
     /*#aa2e95;*/
} 

.inputBuscar {
    background-color: #faeff9;
    background-image: url("../assets/buscar.png");
    background-repeat: no-repeat;
    background-size: 45px 45px;
    padding-left: 50px;
    position: relative; left: 300px; top: 40px;
    width: 30%;
    height: 30%;
    border-color: #9130ec;
    color: #9130ec;
    font-size: 16px;
}

.selectBuscar {
    background-color: #faeff9;
    position: relative; left: 295px; top: 40px;
    width: 10%;
    height: 30%;
    border-color: #9130ec;
    color: #9130ec;
    font-size: 16px;
  
}
.inputBoton {
    background-color: #c3c9e9;
    /*aa2e95;*/
    border-color:#8a2be2;
    color: #8a2be2;
    padding: 15px 25px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    font-size: 16px;
    position: relative;left: 300px; top:40px;

}

.inputBoton:hover{
  opacity: 0.80;
  -moz-opacity: 0.80;
  filter:alpha (opacity=80);
  background-color: #8a2be2;
  color:#c3d6e9;
}
.cajas{
  border-collapse:separate;
  border: #2fc0da 1px solid;
  margin: 15px;
  padding: 15px;
  background: #2fc0da70;
  WIDTH: 400px;
  /*20%;*/
  height: 200px;
  /*45%;*/
  position: relative; left: 250px;
  -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
}
</style>
