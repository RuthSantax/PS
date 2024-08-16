from models.venta import Venta as VentaModel
from schemas.venta import Venta
from sqlalchemy.orm import Session
from datetime import date

class VentaService:
    
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_ventas(self):
        result = self.db.query(VentaModel).all()
        return result

    def get_venta(self, id: int):
        result = self.db.query(VentaModel).filter(VentaModel.id == id).first()
        return result

    def get_venta_by_usuario(self, usuario_id: int):
        result = self.db.query(VentaModel).filter(VentaModel.usuario_id == usuario_id).all()
        return result
    
    # def get_venta_activa(self, usuario_id: int):
    #         now = date.now()
    #         result = self.db.query(VentaModel).filter(VentaModel.usuario_id == usuario_id, VentaModel.cantidad >= now).all()
    #         return result

    def is_producto_disponible(self, producto_id: int, cantidad: date):
        existing_ventas = self.db.query(VentaModel).filter(
            VentaModel.producto_id == producto_id,
            VentaModel.cantidad < cantidad
        ).all()
        return len(existing_ventas)

    def create_venta(self, venta: Venta):
        if not self.is_producto_disponible(venta.producto_id, venta.cantidad):
            raise ValueError("El producto no está disponible.")
        new_venta = VentaModel(**venta.model_dump())
        self.db.add(new_venta)
        self.db.commit()
        return new_venta

    def update_venta(self, id: int, data: Venta):
        venta = self.db.query(VentaModel).filter(VentaModel.id == id).first()
        if venta:
            if not self.is_producto_disponible(data.producto_id, data.cantidad, data.fecha_venta):
                raise ValueError("El producto no está disponible para la venta.")
            venta.producto_id = data.producto_id
            venta.usuario_id = data.usuario_id
            venta.cantidad = data.cantidad
            venta.fecha_venta = data.fecha_venta
            self.db.commit()
        return venta

    def delete_venta(self, id: int):
        self.db.query(VentaModel).filter(VentaModel.id == id).delete()
        self.db.commit()
        return
