
import { ventasServices } from "../../servicios/ventas-servicios.js";
import { newRegister as newVenta } from "./ventas-new.js";
import { editRegister as editVenta } from "./ventas-new.js";

const htmlVentas = `
<div class="card">
   <div class="card-header">
   
   <h3 class="card-title"> 
       <a class="btn bg-dark btn-sm btnAgregarVenta" href="#/newVenta">Agregar Venta</a>
   </h3>

   </div>

   <!-- /.card-header -->
   <div class="card-body">            
   <table id="ventasTable" class="table table-bordered table-striped tableVenta" width="100%">
       <thead>
           <tr>
           <th># </th>
           <th>Vehículo ID</th>
           <th>Usuario ID</th>
           <th>Fecha Venta</th>
           <th>Fecha Devolución</th>
           <th>Acciones</th>
           </tr>
       </thead>
   
   </table>
   </div>
   <!-- /.card-body -->
</div> `;

export async function Ventas(){
    let d = document;
    let res = '';
    d.querySelector('.contenidoTitulo').innerHTML = 'Ventas';
    d.querySelector('.contenidoTituloSec').innerHTML = '';
    d.querySelector('.rutaMenu').innerHTML = "Ventas";
    d.querySelector('.rutaMenu').setAttribute('href',"#/ventas");
    let cP = d.getElementById('contenidoPrincipal');
    
    res = await ventasServices.listar();
    res.forEach(element => {
      element.action = "<div class='btn-group'><a class='btn btn-warning btn-sm mr-1 rounded-circle btnEditarVenta'  href='#/editVenta' data-idVenta='"+ element.id +"'> <i class='fas fa-pencil-alt'></i></a><a class='btn btn-danger btn-sm rounded-circle removeItem btnBorrarVenta'href='#/delVenta' data-idVenta='"+ element.id +"'><i class='fas fa-trash'></i></a></div>";
    });  
    
    cP.innerHTML =  htmlVentas;
    llenarTabla(res);

    let btnAgregar = d.querySelector(".btnAgregarVenta");
    btnAgregar.addEventListener("click", agregar);
}

function enlazarEventos(oSettings){
    let d = document;
    let btnEditar = d.querySelectorAll(".btnEditarVenta");
    let btnBorrar = d.querySelectorAll(".btnBorrarVenta");
    for(let i=0 ; i< btnEditar.length ; i++){
        btnEditar[i].addEventListener("click", editar);
        btnBorrar[i].addEventListener("click", borrar);
    } 
}

function agregar(){
    newVenta();
}

function editar(){
    let id = parseInt(this.getAttribute('data-idVenta'), 10);
    editVenta(id);
}

async function borrar(){
    let id = parseInt(this.getAttribute('data-idVenta'), 10);
    let borrar = 0;
    await Swal.fire({
        title: 'Está seguro que desea eliminar el registro?',
        showDenyButton: true,
        confirmButtonText: 'Si',
        denyButtonText: `Cancelar`,
        focusDeny: true
      }).then((result) => {
        if (result.isConfirmed) {
           borrar = 1;
        } else if (result.isDenied) {
           borrar = 0 ;
           Swal.fire('Se canceló la eliminación', '', 'info');
        }
      })
      if (borrar === 1)
            await ventasServices.borrar(id); 
      window.location.href = "#/ventas";  
}

function llenarTabla(res){ 
    let dtable = new DataTable('#ventasTable', {
        responsive:true,
        data : res,
        columns: [
            { data: 'id' },    
            { data: 'producto_id' },
            { data: 'usuario_id' },
            { data: 'fecha_venta' },
            { data: 'fecha_devolucion' },
            { data: 'action', "orderable":false }
        ],
        fnDrawCallback: function (oSettings) {
            enlazarEventos(oSettings);
        },
        deferRender: true,
        retrieve: true,
        processing: true,
        language: {
            sProcessing:     "Procesando...",
            sLengthMenu:     "Mostrar _MENU_ registros",
            sZeroRecords:    "No se encontraron resultados",
            sEmptyTable:     "Ningún dato disponible en esta tabla",
            sInfo:           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_",
            sInfoEmpty:      "Mostrando registros del 0 al 0 de un total de 0",
            sInfoFiltered:   "(filtrado de un total de _MAX_ registros)",
            sInfoPostFix:    "",
            sSearch:         "Buscar:",
            sUrl:            "",
            sInfoThousands:  ",",
            sLoadingRecords: "Cargando...",
            oPaginate: {
                sFirst:    "Primero",
                sLast:     "Último",
                sNext:     "Siguiente",
                sPrevious: "Anterior"
            },
            oAria: {
                sSortAscending:  ": Activar para ordenar la columna de manera ascendente",
                sSortDescending: ": Activar para ordenar la columna de manera descendente"
            }
        }                           
    });
}
