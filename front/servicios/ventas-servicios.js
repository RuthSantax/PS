
const url = "http://127.0.0.1:8000/ventas";

async function listar(id) {
    let cadUrl;
    if (isNaN(id))
        cadUrl = url;
    else
        cadUrl = url + "/" + id;
    return await fetch(cadUrl, {
            headers: {
                "accept": "application/json",
                "Content-type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem('token')
            }
        })
        .then(respuesta => respuesta.json());
}

async function crear(producto_id, usuario_id, fecha_venta, fecha_devolucion) {
    return await fetch(url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem('token')
        },
        body: JSON.stringify({
            producto_id: producto_id,
            usuario_id: usuario_id,
            fecha_venta: fecha_venta,
            fecha_devolucion: fecha_devolucion
        })
    })
    .then(respuesta => respuesta.json());
}

async function editar(id, producto_id, usuario_id, fecha_venta, fecha_devolucion) {
    let urlPut = url + "/" + id;
    return await fetch(urlPut, {
            method: 'PUT',
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem('token')
            },
            body: JSON.stringify({
                producto_id: producto_id,
                usuario_id: usuario_id,
                fecha_venta: fecha_venta,
                fecha_devolucion: fecha_devolucion
            })
        })
        .then(respuesta => respuesta.json());
}

async function borrar(id) {
    let urlDelete = url + "/" + id;
    return await fetch(urlDelete, {
            method: 'DELETE',
            headers: {
                "Authorization": "Bearer " + localStorage.getItem('token')
            }
        })
        .then(respuesta => respuesta.json());
}

export const ventasServices = {
    listar,
    crear,
    editar,
    borrar,
};

