from models.producto import Producto as ProductoModel
from schemas.producto import Producto


class ProductoService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_productos(self):
        result = self.db.query(ProductoModel).all()
        return result

    def get_producto(self, id):
        result = self.db.query(ProductoModel).filter(ProductoModel.id == id).first()
        return result

    def get_producto_by_categoria(self, categoria_id: str):
        result = self.db.query(ProductoModel).filter(ProductoModel.categoria_id == categoria_id).all()
        return result
    
    def get_producto_by_subcategoria(self, subcateg_id: str):
        result = self.db.query(ProductoModel).filter(ProductoModel.subcateg_id == subcateg_id).all()
        return result
    
    def get_producto_by_name(self, nombre: str):
        result = self.db.query(ProductoModel).filter(ProductoModel.nombre == nombre).all()
        return result
    
    def get_producto_by_precio(self, precio: int):
        result = self.db.query(ProductoModel).filter(ProductoModel.precio == precio).all()
        return result

    def create_producto(self, producto: Producto):
        new_producto = ProductoModel(**producto.model_dump())
        self.db.add(new_producto)
        self.db.commit()
        return

    def update_producto(self, id: int, data: Producto):
        producto = self.db.query(ProductoModel).filter(ProductoModel.id == id).first()
        producto.categoria_id = data.categoria_id
        producto.subcateg_id = data.subcateg_id
        producto.nombre = data.nombre
        producto.precio = data.precio
        producto.descripcion = data.descripcion
        producto.foto = data.foto
        self.db.commit()
        return

    def delete_producto(self, id: int):
       self.db.query(ProductoModel).filter(ProductoModel.id == id).delete()
       self.db.commit()
       return
   