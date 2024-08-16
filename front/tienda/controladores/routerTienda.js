import { Carrusel } from "./carrusel/carrusel.js";
import {listarproductos } from "./listarProductos/listarProductos.js";
import { vistaproducto } from "./listarProductos/vistaProducto.js";
import { getUsuarioAutenticado, login, mostrarUsuario, register, setUsuarioAutenticado } from "./login/login.js";

export function RouterTienda(){
    let session = getUsuarioAutenticado();
    setSession(session); 
    let hash = location.hash;
   
    if (hash === '#vistaproducto'){
        
        vistaproducto();

    }else if (hash === '#login' ) {
       
        login(); 
    }else if (hash === '#register' ) {      
        
        register();    

    }else if (hash === '#logout' ) {      
        
        setUsuarioAutenticado(false, -1);
        location.replace("tienda.html");

    }else if (hash === '' ) {
        
        Carrusel();
        listarproductos();
        
    }    
    console.log (hash);
}

function setSession(session){
   /**
    * Esta función se utiliza para recuperar los datos de sessión cada vez que se recarga la página.
    */ 
   let d=document;
   if ( session.autenticado ) {
        mostrarUsuario(session.email);

   }
   

}