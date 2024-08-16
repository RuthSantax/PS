import { productosServices } from "../../servicios/productos-servicios.js";  

const htmlAmProductos = `
<div class="card card-dark card-outline">
	
	<form  class="needs-validation frmAmProducto"  enctype="multipart/form-data">
	
		<div class="card-header">
               
			<div class="col-md-8 offset-md-2">	
               
				<!--=====================================
                Categoria
                ======================================-->
				
				<div class="form-group mt-5">
					
					<label>Categoria</label>

					<input 
					type="text" 
					class="form-control"
					pattern="[A-Za-zñÑáéíóúÁÉÍÓÚ0-9 ]{1,}"
					onchange="validateJS(event,'text')"
					name="categoria"
                    id="productoCategoria"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Subcategoria
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Subcategoria</label>

					<input 
					type="text" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="subcategoria"
                    id="productoSubcategoria"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Nombre
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Nombre</label>

					<input 
					type="text" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="nombre"
                    id="productoNombre"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Descripcion
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Descripcion</label>

					<input 
					type="text" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="descripcion"
                    id="productosDescripcion"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Precio
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Precio ID</label>

					<input 
					type="number" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="precio"
                    id="productosPrecio"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>
			
			</div>
		
		</div>

		<div class="card-footer">
			
			<div class="col-md-8 offset-md-2">
	
				<div class="form-group mt-3">

					<a href="#/productos" class="btn btn-light border text-left">Cancelar</a>
					
					<button type="submit" class="btn bg-dark float-right">Guardar</button>

				</div>

			</div>

		</div>

	</form>

</div> `;

var formulario='';
var txtCategoria='';
var txtSubcategoria='';
var txtNombre='';
var txtDescripcion='';
var txtPrecio='';
let productoId=0;

export async function newRegister(){
    let d = document;
    
    d.querySelector('.contenidoTitulo').innerHTML = 'Agregar Producto';
	d.querySelector('.contenidoTituloSec').innerHTML += 'Agregar';
   
    crearFormulario();

    formulario = d.querySelector(".frmAmProducto")
    formulario.addEventListener("submit", guardar);
	
}

export async function editRegister(id){
    let d = document;
    productoId = id;
    d.querySelector('.contenidoTitulo').innerHTML = 'Editar Producto';
    d.querySelector('.contenidoTituloSec').innerHTML += 'Editar';
    crearFormulario();

    formulario = d.querySelector(".frmAmProducto")
    formulario.addEventListener("submit", modificar);
    let producto =  await productosServices.listar(id);

    txtCategoria.value= producto.categoria;
    txtSubcategoria.value= producto.subcategoria;
	txtNombre.value= producto.nombre;
    txtDescripcion.value= producto.descripcion;
	txtPrecio.value= producto.precio;
}

function crearFormulario(){
    let d = document;
    d.querySelector('.rutaMenu').innerHTML = "Productos";
    d.querySelector('.rutaMenu').setAttribute('href',"#/productos");

    let cP =d.getElementById('contenidoPrincipal');
    cP.innerHTML =  htmlAmProductos;
    
    var script = document.createElement( "script" );
    script.type = "text/javascript";
    script.src = '../controladores/validaciones.js';
    cP.appendChild(script);
    
    txtSubcategoria= d.getElementById('productoCategoria');
	txtCategoria= d.getElementById('productoSubcategoria');
	txtNombre=d.getElementById('productoNombre');
	txtDescripcion= d.getElementById('productoDescripcion');
	txtIdCategoria= d.getElementById('productoPrecio');
}

function guardar(e) {
    e.preventDefault();
    const formData = new FormData(e?.target); 
    const values = Object.fromEntries(formData); 
    console.log(values);
   
    // No incluir 'id' en la solicitud de creación
    productosServices.crear(values.categoria, values.subcategoria, values.nombre, values.descripcion, values.precio)
         .then(respuesta => {
             formulario.reset();
             window.location.href = "#/productos";
         })
         .catch(error => console.log(error));        
}

function modificar(e) {
    e.preventDefault();
	const formData = new FormData(e?.target); 
	const values = Object.fromEntries(formData); 
   
    productosServices.editar(productoId, values.categoria, values.subcategoria, values.nombre, values.descripcion, values.precio)
        .then(respuesta => {
            formulario.reset();
            window.location.href = "#/productos";
        })
        .catch(error => console.log(error))        
}
