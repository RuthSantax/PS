from models.usuario import Usuario as UsuarioModel
from schemas.usuario import Usuario, Id
from sqlalchemy.orm import Session
from typing import List


class UsuarioService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_usuarios(self)-> List[UsuarioModel]:
        result = self.db.query(UsuarioModel).all()
        return result

    def get_usuario(self, id):
        result = self.db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
        return result

    def get_usuario_by_email(self, email):
        result = self.db.query(UsuarioModel).filter(UsuarioModel.email == email).all()
        return result

    def create_usuario(self, usuario: Usuario):
        new_usuario = UsuarioModel(**usuario.model_dump())
        Id.id_duplicado(new_usuario, self.db.query(UsuarioModel).all())
        self.db.add(new_usuario)
        self.db.commit()
        return


    def update_usuario(self, id: int, data: Usuario):
        usuario = self.db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
        usuario.nombre = data.nombre
        usuario.email = data.email
        usuario.password = data.password
        usuario.rol = data.rol
        self.db.commit()
        return

    def delete_usuario(self, id: int):
       self.db.query(UsuarioModel).filter(UsuarioModel.id == id).delete()
       self.db.commit()
       return