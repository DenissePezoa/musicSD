<template>
  <div class="Insert">
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
    <div class="ingresa">
        <center>
        <h2> Ingresar información de Canción </h2>
        <table class="caja">
        <table class="tablaForm">
        <tr>
          <td>
            <label for="nombre"><b>Nombre canción</b></label>
          </td>
          <td>
            <input type="text" id='nombreC' placeholder="Ingrese nombre cancion" name="nombrecancion" required>
          </td>
        </tr>
        <tr>
          <td>
          <label for="album"><b>Álbum canción</b></label>
          </td>
          <td>
            <input type="text" id='albumC' placeholder="Ingrese nombre del album" name="albumcancion" required>
          </td>
        </tr>
        <tr>
          <td>
            <label for="autor"><b>Autor canción (banda o solista)</b></label>
          </td>
          <td>
          <input type="text" id='autorC' placeholder="Ingrese nombre del autor" name="autorcancion" required>
          </td>
        </tr>
        <tr>
          <td>
            <label for="genero"><b>Género canción</b></label>
          </td>
          <td>
            <input type="text" id='generoC' placeholder="Ingrese nombre del genero" name="autorcancion" required>
          </td>
        </tr>
        <tr>
          <td colspan="2" align="center">
            
            <input type="button" class="boton" value="Agregar cancion" v-on:click="agregarCancion"/>
          </td>
          <td>
          </td>
        </tr>
        </table>
        </table>
        </center>
      </div>
  </div>
</template>

<script>
var nombre = ""
var album = ""
var autor = ""
var genero = ""
var idCancion = ""

var cancionEsta = true

var idcancion = ""
var idautor = ""
var idgenero = ""

export default {
    methods: {
      funcionnueva: function(){
              console.log("Cancion ID FINAL: "+idcancion)
              console.log("Autor ID FINAL: "+idautor)
              console.log("Genero ID FINAL: "+idgenero)

              this.$http.post('http://localhost:5000/newCancionGenero',{"cancionid":idcancion,"generoid":idgenero}).then(response=>{
              console.log("Intermedio C-G exitoso!")
              },response=>{
              console.log("Fail C-G!")
              });

              this.$http.post('http://localhost:5000/newCancionAutor',{"cancionid":idcancion,"autorid":idautor}).then(response=>{
              console.log("Intermedio C-A exitoso!")
              alert("Se agregó la canción exitosamente")
              document.getElementById("nombreC").value="";
              document.getElementById("albumC").value="";
              document.getElementById("autorC").value="";
              document.getElementById("generoC").value="";
              },response=>{
              console.log("Fail C-A!")
              });


      },
      agregarCancion(){
        if (confirm("Esta seguro que desea ingresar estos datos?")){
          
          console.log("Se confirma el ingreso")

          nombre = document.getElementById("nombreC").value;
          album = document.getElementById("albumC").value;
          autor = document.getElementById("autorC").value;
          genero = document.getElementById("generoC").value;

          if (nombre != "" && album != "" && autor != "" && genero != ""){
            this.$http.get('http://localhost:5000/getIdCancion?nameCan='+nombre+'&albumCan='+album).then(response=>{
            console.log("Exito!")
            //console.log(response.body.cancionId.length)
            if(response.body.cancionId.length == 0){
              console.log("VACIO, cancion no existe!")
              cancionEsta=false;
              if(cancionEsta!=true){
                cancionEsta = true
                this.$http.post('http://localhost:5000/newCancion',{
                "cancionnombre":nombre,
                "cancionalbum":album}).then(response=>{
                  console.log("Exito! Se guardo la cancion!")
                  this.$http.get('http://localhost:5000/getIdCancion?nameCan='+nombre+'&albumCan='+album).then(response=>{
                  console.log("Exito! 2")
                  //console.log(response.body)
                  //console.log(response.body.cancionId[0].idcancion)

                  idcancion = response.body.cancionId[0].idcancion
                  console.log("Cancion ID: "+idcancion)

                  this.$http.get('http://localhost:5000/getIdAutor?nameAutor='+autor).then(response=>{
                    console.log("Exito! 3")
                    //console.log(response.body.autorId.length)
                    //console.log(response.body.autorId)

                    if(response.body.autorId.length == 0){
                      console.log("VACIO, autor no existe!")
                      this.$http.post('http://localhost:5000/newAutor',{"autornombre":autor}).then(response=>{
                        console.log("Exito! 4")
                        this.$http.get('http://localhost:5000/getIdAutor?nameAutor='+autor).then(response=>{
                          console.log("Exito! 5")
                          //console.log(response.body.autorId.length)
                          //console.log(response.body.autorId)

                          idautor = response.body.autorId[0].idautor
                          console.log("Autor ID: "+idautor)

                          this.$http.get('http://localhost:5000/getIdGenero?nameGenero='+genero).then(response=>{
                            console.log("Exito! 6")
                            //console.log(response.body.generoId.length)
                            //console.log(response.body.generoId)
                            if(response.body.generoId.length == 0){
                              console.log("VACIO, genero no existe!")
                              this.$http.post('http://localhost:5000/newGenero',{"generonombre":genero}).then(response=>{
                                console.log("Exito! 7")
                                this.$http.get('http://localhost:5000/getIdGenero?nameGenero='+genero).then(response=>{
                                  console.log("Exito! 8")
                                  //console.log(response.body.generoId.length)
                                  //console.log(response.body.generoId)

                                  idgenero = response.body.generoId[0].idgenero
                                  console.log("Genero ID: "+idgenero)
                                  this.funcionnueva()



                                },response=>{
                                  console.log("No tuvo exito :c")
                                });


                              },response=>{
                                console.log("No tuvo exito :c")

                              });

                            }else{
                              idgenero = response.body.generoId[0].idgenero
                              console.log("Genero ID: "+idgenero)
                              this.funcionnueva()
                              
                            }


                          },response=>{
                              console.log("No tuvo exito :c")
                          });


                      },response=>{
                          console.log("No tuvo exito :c")

                      });
                      

                      },response=>{
                          console.log("No tuvo exito :c")
                      });

                    }else{
                      idautor = response.body.autorId[0].idautor
                      console.log("Autor ID: "+idautor)

                      this.$http.get('http://localhost:5000/getIdGenero?nameGenero='+genero).then(response=>{
                        console.log("Exito! 9")
                        //console.log(response.body.generoId.length)
                        //console.log(response.body.generoId)
                        if(response.body.generoId.length == 0){
                          console.log("VACIO, genero no existe!")
                          this.$http.post('http://localhost:5000/newGenero',{"generonombre":genero}).then(response=>{
                            console.log("Exito! 10")
                            this.$http.get('http://localhost:5000/getIdGenero?nameGenero='+genero).then(response=>{
                              console.log("Exito! 11")
                              //console.log(response.body.generoId.length)
                              //console.log(response.body.generoId)

                              idgenero = response.body.generoId[0].idgenero
                              console.log("Genero ID: "+idgenero)
                              this.funcionnueva()



                            },response=>{
                              console.log("No tuvo exito :c")
                            });


                          },response=>{
                            console.log("No tuvo exito :c")

                          });

                        }else{
                          idgenero = response.body.generoId[0].idgenero
                          console.log("Genero ID: "+idgenero)
                          this.funcionnueva()
                        }


                      },response=>{
                          console.log("No tuvo exito :c")
                      });


                    }


                  },response=>{
                      console.log("No tuvo exito :c")
                  });



                  }, response=>{
                    console.log("No tuvo exito :c")
                  });
              }, response=>{
                console.log("No tuvo exito :c")
              });




            }
              


          }else{alert("Ya existe la canción en la app!");}
            

            
            }, response=>{
              console.log("No tuvo exito :c")
            });
            

        }else{
            alert("Debe ingresar un nombre y album de la cancion. Además de ingresar el autor, y genero de la canción.");
            console.log("No se ingresaron datos!")

          }





          

        }else{
          console.log("No se realiza el ingreso.")
        }
        

      }
      
      },
    
    mounted: function(){
    
    },
    data() {

        return {

          datos: []

        }
    
    }
}
</script>

<style>
.Insert {
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
.caja{
  border-collapse: collapse;
  border: #2fc0da 1px solid;
  margin: 15px;
  padding: 15px;
  background: #2fc0da70;
  WIDTH: 40%;
  height: 90%;
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
.ingresa {
  background-color:#c3d6e9;
  position:absolute; top:240px; left: 0px; right: 0px;
   height: 350px;
}
.boton {
    background-color: #c3c9e9;
    /*aa2e95;*/
    border-color:#8a2be2;
    color: #8a2be2;
    padding: 10px 10px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    font-size: 14px;

}

.boton:hover{
  opacity: 0.80;
  -moz-opacity: 0.80;
  filter:alpha (opacity=80);
  background-color: #8a2be2;
  color:#c3d6e9;
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
</style>