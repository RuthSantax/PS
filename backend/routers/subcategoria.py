from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from conf.database import Session
from services.subcategoria import SubcategoriaService
from schemas.subcategoria import Subcategoria
from middlewares.jwt_bearer import JWTBearer

subcategoria_router = APIRouter()

@subcategoria_router.get('/subcategorias', tags=['subcategorias'], response_model=List[Subcategoria], status_code=200, dependencies=[Depends(JWTBearer())])
def get_subcategorias():
    db = Session()
    result = SubcategoriaService(db).get_subcategorias()
    return JSONResponse(status_code=200, content=result)

@subcategoria_router.get('/subcategorias/{id}', tags=['subcategorias'], response_model=Subcategoria, dependencies=[Depends(JWTBearer())])
def get_subcategoria_by_id(id: int = Path(...)):
    db = Session()
    result = SubcategoriaService(db).get_subcategoria_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "La subcategoría no se ha encontrado."})
    return JSONResponse(status_code=200, content=result)

@subcategoria_router.post('/subcategorias', tags=['subcategorias'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_subcategoria(subcategoria: Subcategoria):
    db = Session()
    SubcategoriaService(db).create_subcategoria(subcategoria)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la subcategoría con éxito."})

@subcategoria_router.put('/subcategorias/{id}', tags=['subcategorias'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_subcategoria(id: int, subcategoria: Subcategoria):
    db = Session()
    result = SubcategoriaService(db).get_subcategoria_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No se ha encontrado la subcategoría."})
    SubcategoriaService(db).update_subcategoria(id, subcategoria)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la subcategoría con éxito."})

@subcategoria_router.delete('/subcategorias/{id}', tags=['subcategorias'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_subcategoria(id: int):
    db = Session()
    result = SubcategoriaService(db).get_subcategoria_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la subcategoría."})
    SubcategoriaService(db).delete_subcategoria(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la subcategoría con éxito."})
