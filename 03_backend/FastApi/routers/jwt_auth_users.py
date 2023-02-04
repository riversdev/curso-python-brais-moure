from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError                                                          # pip install "python-jose[cryptography]"
from passlib.context import CryptContext                                                # pip install "passlib[bcrypt]"
from datetime import datetime, timedelta



# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = '901cc97e201a392d722ad95805bd060b16389e1b0bc9dd8c13c02889a44043d8'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 1



# instances
router = APIRouter(
    prefix='/jwtauth',
    tags=['jwtauth'],
    responses={status.HTTP_400_BAD_REQUEST: {'message': 'No encontrado :v'}},
)
oauth2 = OAuth2PasswordBearer('login')
crypt = CryptContext(['bcrypt']) # algoritmo de encriptacion



# models
class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str



# fake db
users_db = {
    'mouredev': {
        'username': 'mouredev',
        'fullname': 'Brais Moure',
        'email': 'braismoure@moure.com',
        'disabled': False,
        'password': '$2a$12$8DtbXbS5YKXfagvPVk0Ws.Gu7wcT0Fs31sprZq6zslPUYwMLwBy12',
    },
    'rivers': {
        'username': 'rivers',
        'fullname': 'Alejandro Rios',
        'email': 'alejandrorios@mail.com',
        'disabled': True,
        'password': '$2a$12$1uPCc2ttAWlYg3ci/W.n6.1NhFi/HNiTyoqN/cQu8FRq6V/W7Vdyu',
    }
}



# core functions
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username]) 

async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(status.HTTP_401_UNAUTHORIZED, 'Credenciales de autenticacion invalidas', {'WWW-Authenticate': 'Bearer'})

    try:
        username: str = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get('sub')
        
        if username is None:
            raise exception
    except JWTError:
        raise exception
    
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Usuario inhabilitado')
    else:
        return user



# routes
@router.post('/login')
async def login_user(form: OAuth2PasswordRequestForm = Depends()):
    user_db = search_user_db(form.username)

    if not user_db:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'El usuario no existe')
    
    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'La contrasenia es incorrecta')

    access_token = {
        'sub': user_db.username, 
        'exp': datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    
    return {'access_token': jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM), 'token_type': 'bearer'}

@router.get('/users/me')
async def get_me(user: User = Depends(current_user)):
    return user