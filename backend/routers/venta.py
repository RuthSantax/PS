from fastapi import APIRouter, Depends, Path, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from conf.database import Session
from models.venta import Venta as VentaModel
from schemas.venta import Venta
from services.venta import VentaService
from middlewares.jwt_bearer import JWTBearer
from fastapi.encoders import jsonable_encoder

venta_router = APIRouter()

@venta_router.get('/ventas', tags=['ventas'], response_model=List[Venta], status_code=200, dependencies=[Depends(JWTBearer())])
def get_ventas() -> List[Venta]:
    db = Session()
    result = VentaService(db).get_ventas()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@venta_router.get('/ventas/{id}', tags=['ventas'], response_model=Venta, dependencies=[Depends(JWTBearer())])
def get_venta(id: int = Path(..., ge=1, le=2000)) -> Venta:
    db = Session()
    result = VentaService(db).get_venta(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@venta_router.get('/ventas/usuario/{usuario_id}', tags=['ventas'], response_model=List[Venta], dependencies=[Depends(JWTBearer())])
def get_venta_by_usuario(usuario_id: int) -> List[Venta]:
    db = Session()
    result = VentaService(db).get_venta_by_usuario(usuario_id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Ventas no encontradas para este usuario"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@venta_router.get('/ventas/activas/{usuario_id}', tags=['ventas'], response_model=List[Venta], dependencies=[Depends(JWTBearer())])
def get_venta_activa(usuario_id: int) -> List[Venta]:
    db = Session()
    result = VentaService(db).get_venta_activa(usuario_id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No hay ventas activas para este usuario"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@venta_router.post('/ventas', tags=['ventas'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_venta(venta: Venta) -> dict:
    db = Session()
    try:
        VentaService(db).create_venta(venta)
        return JSONResponse(status_code=201, content={"message": "Se ha registrado la venta."})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@venta_router.put('/ventas/{id}', tags=['ventas'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_venta(id: int, venta: Venta) -> dict:
    db = Session()
    result = VentaService(db).get_venta(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    try:
        VentaService(db).update_venta(id, venta)
        return JSONResponse(status_code=200, content={"message": "Se ha modificado la venta."})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@venta_router.delete('/ventas/{id}', tags=['ventas'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_venta(id: int) -> dict:
    db = Session()
    result: VentaModel = db.query(VentaModel).filter(VentaModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    VentaService(db).delete_venta(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la venta."})
