from models.categoria import Categoria as CategoriaModel
from schemas.categoria import Categoria

class CategoriaService:
    def __init__(self, db):
        self.db = db

    def get_categorias(self):
        return self.db.query(CategoriaModel).all()

    def get_categoria_by_id(self, id:str):
        return self.db.query(CategoriaModel).filter(CategoriaModel.id == id).first()

    def create_categoria(self, categoria: Categoria):
        new_categoria = CategoriaModel(**categoria.model_dump())
        self.db.add(new_categoria)
        self.db.commit()

    def update_categoria(self, id: str, data: Categoria):
        categoria = self.db.query(CategoriaModel).filter(CategoriaModel.id == id).first()
        if categoria:
            categoria.nombre = data.nombre
            categoria.categoria_ = data.categoria_
            categoria.descripcion = data.descripcion
            self.db.commit()

    def delete_categoria(self, id: str):
        self.db.query(CategoriaModel).filter(CategoriaModel.id == id).delete()
        self.db.commit()
