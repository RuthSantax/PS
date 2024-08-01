from pydantic import BaseModel, Field
from schemas import subcategoria as s

class Categoria(BaseModel):
    id: str
    nombre: str = Field(min_length=1, max_length=30)
    categ: str = Field(min_length=1, max_length=30)
    subc: s.Subcategoria.subcategoria_id 
    descripcion: str = Field(min_length=5, max_length=100)
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "2",
                "nombre": "Categoria 1",
                "categ": "C",
                "subc": "x",
                "descripcion": "Esta es la categoria 1"
            }
        }
