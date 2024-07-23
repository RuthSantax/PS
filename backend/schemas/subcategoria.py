from pydantic import BaseModel, Field

class Subcategoria(BaseModel):
    id: str
    categoria_id: str
    nombre: str = Field(min_length=5, max_length=30)
    descripcion: str = Field(min_length=5, max_length=100)
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "2",
                "categoria_id": "AG",
                "nombre": "Subcategoria 1",
                "descripcion": "Esta es la subcategoria 1"
            }
        }
