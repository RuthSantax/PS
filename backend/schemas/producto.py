from pydantic import BaseModel, Field, EmailStr, field_validator, SecretStr
from fastapi import status
from typing import Optional, List
from fastapi.exceptions import HTTPException


class Producto(BaseModel):
    id: Optional[int] = None
    categoria: str = Field(min_length=5, max_length=30)
    nombre: str = Field(min_length=5, max_length=30)
    descripcion: str = Field(min_length=5, max_length=100)
    precio: int = Field(gt=0)
    
    
    class Config:
        json_scheme_extra = {
            "example": {
                "id": 1,
                "categoria": "AR",
                "nombre": "Aro stras",
                "descripcion": "Aros con stras y prendedor de acero quirurgico",
                "precio": 2000,
            }
        }
