from pydantic import BaseModel, Field
from typing import Optional, List


class id_categoria(BaseModel):
    id: int

class Categoria(id_categoria):
    
    nombre: str = Field(min_length=1, max_length=30)
    categ: Optional[str] = Field(min_length=1, max_length=30)
    descripcion: str = Field(min_length=5, max_length=100)
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "nombre": "Categoria 1",
                "categ": "C",
                "descripcion": "Esta es la categoria 1"
            }
        }

class Subcategoria(id_categoria):
        nombre: str = Field(min_length=1, max_length=30)
        subcategoria: Optional[str] = Field(min_length=1, max_length=30)
        descripcion: str = Field(min_length=5, max_length=100)
        
        class Config:
            from_attributes = True
            json_schema_extra = {
                "example": {
                    "id": "2",
                    "nombre": "Categoria 1",
                    "subcategoria": "C",
                    "descripcion": "Esta es la categoria 1"
                }
            }