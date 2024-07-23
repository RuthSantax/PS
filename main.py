from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from conf.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.usuario import usuario_router
from routers.producto import producto_router
from routers.categoria import categoria_router
from routers.subcategoria import subcategoria_router
from routers.venta import venta_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "Saba Joyas"
app.version = "0.0.1"


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

app.add_middleware(ErrorHandler)

## Acá con los CORS (Cross-Origin Resource Sharing)
## defino todos los origenes que van a poder utitlizar/consultar el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], ##habilito el back para cualquier dominio que quiera consultar
    allow_credentials=True,
    allow_methods=["*"],##habilito todos los métodos HTTP( GET, POST, PUT, HEAD, OPTION, etc)
    allow_headers=["*"],##habilito todos los headers que se puedan enviar desde un navegador.
)

app.include_router(usuario_router)
app.include_router(producto_router)
app.include_router(venta_router)
app.include_router(categoria_router)
app.include_router(subcategoria_router)


Base.metadata.create_all(bind=engine)
