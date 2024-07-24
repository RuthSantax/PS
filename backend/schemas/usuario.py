from pydantic import BaseModel, Field, EmailStr, field_validator, SecretStr, ConfigDict
from fastapi import status
from typing import Optional, List
from fastapi.exceptions import HTTPException
    
class UsuarioAuth(BaseModel):
    email: EmailStr
    password: str

class Id(BaseModel):
    id: int = Field(gt=0, le=1000)

    @classmethod
    def id_duplicado(cls, objeto, lista: List):
        for item in lista:
            if item.id == objeto.id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="El id ya se encuentra registrado."
                )

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    rol: str

    class Config:
        from_attributes = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nombre:str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: SecretStr = Field(min_length=8)
    rol: str = Field(default="2")
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('rol')
    def validate_rol(cls, rol):
        if rol not in ["1", "2"]:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='El campo rol debe ser: "1 -Administrador" o "2 -Cliente", sólo el ingrese el número correspondiente.')
        return rol

    @field_validator('password')
    def validar_password(cls, password: SecretStr) -> SecretStr:
        password_str = password.get_secret_value()

        numeros = '0123456789'
        mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        minusculas = 'abcdefghijklmnopqrstuvwxyz'

        if not any(char in numeros for char in password_str):
            raise HTTPException(
                status_code=status.HTTP_417_EXPECTATION_FAILED,
                detail="El password debe contener al menos un número (0-9)."
            )
        
        if not any(char in mayusculas for char in password_str):
            raise HTTPException(
                status_code=status.HTTP_417_EXPECTATION_FAILED,
                detail="El password debe contener al menos una letra mayúscula (A-Z)."
            )
        
        if not any(char in minusculas for char in password_str):
            raise HTTPException(
                status_code=status.HTTP_417_EXPECTATION_FAILED,
                detail="El password debe contener al menos una letra minúscula (a-z)."
            )
        return password
    
