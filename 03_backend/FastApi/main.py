# documentacion con swagger     http://127.0.0.1:8000/docs
# documentacion con redocly     http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Iniciar sevidor       # uvicorn users:app --reload

# routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

# recursos estaticos
app.mount('/staticimages', StaticFiles(directory='./static'), name='staticimages') # /static para que quedara igual que como es el directorio


# routes
@app.get('/')
async def root():
    return 'Hello fast api'

@app.get('/url')
async def url():
    return {'url_curso': 'https://mouredev.com/python'}