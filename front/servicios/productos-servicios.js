const url = "http://127.0.0.1:8000/productos";

async function listar(id) {
    let cadUrl;
    if (isNaN(id))
        cadUrl = url;
    else
        cadUrl = url + "/" + id;
    return await fetch(cadUrl, {
        method: 'GET',
        headers: {
            "Content-type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem('token')
        }
        })
        .then(respuesta => respuesta.json());
}

async function crear(categoria, subcategoria, nombre, descripcion, precio) {
    console.log()
    return await fetch(url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem('token')
        },
        body: JSON.stringify({
            categoria: categoria,
            subcategoria: subcategoria,
            nombre: nombre,
            descripcion: descripcion,
            precio: precio
        })
    })
    .then(respuesta => respuesta.json());
}

async function editar(id, categoria, subcategoria, nombre, descripcion, precio) {
    let urlPut = url + "/" + id;
    return await fetch(urlPut, {
            method: 'PUT',
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem('token')
            },
            body: JSON.stringify({
                categoria: categoria,
                subcategoria: subcategoria,
                nombre: nombre,
                descripcion: descripcion,
                precio: precio
            })
        })
        .then(respuesta => respuesta.json());
}

async function borrar(id) {
    let urlPut = url + "/" + id;
    return await fetch(urlPut, {
            method: 'DELETE',
            headers: {
                "Authorization": "Bearer " + localStorage.getItem('token')
            }
        })
        .then(respuesta => respuesta.json());
}

async function listarPorCategoria(idCategoria) {
    const newUrl = new URL(url + '/');
    newUrl.searchParams.append('idCategoria', idCategoria);
    return await fetch(newUrl)
        .then(respuesta => respuesta.json());
}


export const productosServices = {
    listar,
    crear,
    editar,
    borrar,
    listarPorCategoria,
}
