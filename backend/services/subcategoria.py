from models.subcategoria import Subcategoria as SubcategoriaModel
from schemas.subcategoria import Subcategoria

class SubcategoriaService:
    def __init__(self, db):
        self.db = db

    def get_subcategorias(self):
        return self.db.query(SubcategoriaModel).all()

    def get_subcategoria_by_id(self, id:str):
        return self.db.query(SubcategoriaModel).filter(SubcategoriaModel.id == id).first()

    def create_subcategoria(self, subcategoria: Subcategoria):
        new_subcategoria = SubcategoriaModel(**subcategoria.model_dump())
        self.db.add(new_subcategoria)
        self.db.commit()

    def update_subcategoria(self, id: str, data: Subcategoria):
        subcategoria = self.db.query(SubcategoriaModel).filter(SubcategoriaModel.id == id).first()
        if subcategoria:
            subcategoria.categoria_id = data.categoria_id
            subcategoria.nombre = data.nombre
            subcategoria.descripcion = data.descripcion
            self.db.commit()

    def delete_subcategoria(self, id: str):
        self.db.query(SubcategoriaModel).filter(SubcategoriaModel.id == id).delete()
        self.db.commit()
