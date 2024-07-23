from pydantic import BaseModel, Field

class Categoria(BaseModel):
    id: str
    nombre: str = Field(min_length=5, max_length=30)
    descripcion: str = Field(min_length=5, max_length=100)
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "2",
                "nombre": "Categoria 1",
                "descripcion": "Esta es la categoria 1"
            }
        }
