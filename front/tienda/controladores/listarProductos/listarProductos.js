import { categoriasServices } from "../../../servicios/categorias-servicios.js";
import { productosServices } from "../../../servicios/productos-servicios.js";

function htmlCategoria(id, categoria) {
    let cad = 
                `<div class="categorias" data-idCategoria="${id}">
                    <h1 class="categoria">${categoria}</h1>
                    <div class="Productos">

                        <!-- Acá listan los productos-->
                        <p class="item-producto">Sin productos.</p>
                    </div>
                </div>            
                `;
    return cad; 
}

function htmlItemproducto(id, subcategoria, categoria) {
    let cad = 
                `<div class="item-producto">

                <p class="producto_nombre" name="Megane">${subcategoria}</p>
                <p class="producto_categoria">${categoria}</p>
            
                <a href="?idproducto=${id}#vistaproducto" type="button" class="producto_enlace" >Ver Ptoducto</a>
            
            </div>`;
    return cad; 

}

async function asignarproducto(id) {
    
    let cad = "";
    let resproducto = await productosServices.listarPorCategoria(id);

    resproducto.forEach(producto => {
        cad += htmlItemproducto(producto.id, producto.categoria, producto.subcategoria, producto.descripcion, producto.nombre, producto.precio);
    });
        
    let itemproducto = document.querySelector("[data-idCategoria='"+ id + "'] .productos");
    itemproducto.innerHTML = cad; 
} 

export async function listarproductos() {
    
     let resCat;

     let listaproductos = document.querySelector(".seccionproductos");

     listaproductos.innerHTML = "";
     resCat =  await categoriasServices.listar();

     resCat.forEach(element => {
        listaproductos.innerHTML += htmlCategoria(element.id, element.nombre, element.descripcion);
        asignarProducto(element.id);
     })
     
}