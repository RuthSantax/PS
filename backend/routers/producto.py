from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from conf.database import Session
from models.producto import Producto as ProductoModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.producto import ProductoService
from schemas.producto import Producto
from utils.jwt_manager import create_token

producto_router = APIRouter()

@producto_router.get('/productos', tags=['productos'], response_model=List[Producto], status_code=200)
def get_productos() -> List[Producto]:
    db = Session()
    result = ProductoService(db).get_productos()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@producto_router.get('/productos/{id}', tags=['productos'], response_model=Producto, dependencies=[Depends(JWTBearer())])
def get_producto(id: int = Path(ge=1, le=2000)) -> Producto:
    db = Session()
    result = ProductoService(db).get_producto(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Producto no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@producto_router.get('/productos/precio/{precio}', tags=['productos'], response_model=List[Producto], dependencies=[Depends(JWTBearer())])
def get_producto_by_precio(precio: int) -> List[Producto]:
    db = Session()
    result = ProductoService(db).get_producto_by_precio(precio)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Vehículo no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@producto_router.get('/productos/nombre/{nombre}', tags=['productos'], response_model=List[Producto], dependencies=[Depends(JWTBearer())])
def get_producto_by_name(nombre: str) -> List[Producto]:
    db = Session()
    result = ProductoService(db).get_producto_by_name(nombre)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Producto no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@producto_router.get('/productos/categoria/{categoria_id}', tags=['productos'], response_model=List[Producto], dependencies=[Depends(JWTBearer())])
def get_producto_by_categoria(categoria_id: str) -> List[Producto]:
    db = Session()
    result = ProductoService(db).get_producto_by_categoria(categoria_id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Producto no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@producto_router.get('/productos/categoria/{subcateg_id}', tags=['productos'], response_model=List[Producto], dependencies=[Depends(JWTBearer())])
def get_producto_by_subcategoria(subcateg_id: str) -> List[Producto]:
    db = Session()
    result = ProductoService(db).get_producto_by_subcategoria(subcateg_id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Producto no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@producto_router.post('/productos', tags=['productos'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_producto(producto: Producto) -> dict:
    db = Session()
    ProductoService(db).create_producto(producto)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el producto con éxito."})

@producto_router.put('/productos/{id}', tags=['productos'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_producto(id: int, producto: Producto)-> dict:
    db = Session()
    result = ProductoService(db).get_producto(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Producto no encontrado"})
    
    ProductoService(db).update_producto(id, producto)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el producto con éxito."})

@producto_router.delete('/productos/{id}', tags=['productos'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_producto(id: int)-> dict:
    db = Session()
    result: ProductoModel = db.query(ProductoModel).filter(ProductoModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Producto no encontrado"})
    ProductoService(db).delete_producto(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el producto con éxito."})