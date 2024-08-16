// Cambios necesarios en Ventas-new.js

import { ventasServices } from "../../servicios/ventas-servicios.js";

const htmlAmVentas = `
<div class="card card-dark card-outline">
	
	<form class="needs-validation frmAmVenta" enctype="multipart/form-data">
	
		<div class="card-header">
               
			<div class="col-md-8 offset-md-2">	
               
				<!--=====================================
                Vehículo ID
                ======================================-->
				
				<div class="form-group mt-5">
					
					<label>Vehículo ID</label>

					<input 
					type="number" 
					class="form-control"
					name="producto_id"
                    id="ventaproductoId"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Usuario ID
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Usuario ID</label>

					<input 
					type="number" 
					class="form-control"
					name="usuario_id"
                    id="ventaUsuarioId"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Fecha Venta
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Fecha Venta</label>

					<input 
					type="date" 
					class="form-control"
					name="fecha_venta"
                    id="ventaFechaVenta"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Fecha Devolución
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Fecha Devolución</label>

					<input 
					type="date" 
					class="form-control"
					name="fecha_devolucion"
                    id="ventaFechaDevolucion"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>
			
			</div>
		
		</div>

		<div class="card-footer">
			
			<div class="col-md-8 offset-md-2">
	
				<div class="form-group mt-3">

					<a href="#/ventas" class="btn btn-light border text-left">Cancelar</a>
					
					<button type="submit" class="btn bg-dark float-right">Guardar</button>

				</div>

			</div>

		</div>

	</form>

</div> `;

var formulario='';
var txtproductoId='';
var txtUsuarioId='';
var txtFechaVenta='';
var txtFechaDevolucion='';
let ventaId=0;

export async function newRegister(){
    let d = document;
    
    d.querySelector('.contenidoTitulo').innerHTML = 'Agregar Venta';
	d.querySelector('.contenidoTituloSec').innerHTML += 'Agregar';
   
    crearFormulario();

    formulario = d.querySelector(".frmAmVenta")
    formulario.addEventListener("submit", guardar);
	
}

export async function editRegister(id){
    let d = document;
    ventaId = id;
    d.querySelector('.contenidoTitulo').innerHTML = 'Editar Venta';
    d.querySelector('.contenidoTituloSec').innerHTML += 'Editar';
    crearFormulario();

    formulario = d.querySelector(".frmAmVenta")
    formulario.addEventListener("submit", modificar);
    let venta = await ventasServices.listar(id);

    txtproductoId.value = venta.producto_id;
    txtUsuarioId.value = venta.usuario_id;
    txtFechaVenta.value = venta.fecha_venta;
    txtFechaDevolucion.value = venta.fecha_devolucion;
}

function crearFormulario(){
    let d = document;
    d.querySelector('.rutaMenu').innerHTML = "Ventas";
    d.querySelector('.rutaMenu').setAttribute('href',"#/ventas");

    let cP =d.getElementById('contenidoPrincipal');
    cP.innerHTML =  htmlAmVentas;
    
    var script = document.createElement( "script" );
    script.type = "text/javascript";
    script.src = '../controladores/validaciones.js';
    cP.appendChild(script);
    
    txtproductoId = d.getElementById('ventaproductoId');
    txtUsuarioId = d.getElementById('ventaUsuarioId');
    txtFechaVenta = d.getElementById('ventaFechaVenta');
    txtFechaDevolucion = d.getElementById('ventaFechaDevolucion');
}

function guardar(e) {
    e.preventDefault();
    const formData = new FormData(e?.target); 
    const values = Object.fromEntries(formData); 
   
    ventasServices.crear(values.producto_id, values.usuario_id, values.fecha_venta, values.fecha_devolucion)
         .then(respuesta => {
             formulario.reset();
             window.location.href = "#/ventas";
         })
         .catch(error => console.log(error));        
}

function modificar(e) {
    e.preventDefault();
	const formData = new FormData(e?.target); 
	const values = Object.fromEntries(formData); 
   
    ventasServices.editar(ventaId,values.producto_id, values.usuario_id, values.fecha_venta, values.fecha_devolucion)
        .then(respuesta => {
            formulario.reset();
            window.location.href = "#/ventas";
        })
        .catch(error => console.log(error))        
}
