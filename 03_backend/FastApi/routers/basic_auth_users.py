from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



# instances
router = APIRouter(
    prefix='/basicauth',
    tags=['basicauth'],
    responses={status.HTTP_400_BAD_REQUEST: {'message': 'No encontrado :v'}},
)
oauth2 = OAuth2PasswordBearer('login')



# models
class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User): # hereda de User
    password: str



# fake db
users_db = {
    'mouredev': {
        'username': 'mouredev',
        'fullname': 'Brais Moure',
        'email': 'braismoure@moure.com',
        'disabled': False,
        'password': '123456',
    },
    'rivers': {
        'username': 'rivers',
        'fullname': 'Alejandro Rios',
        'email': 'alejandrorios@mail.com',
        'disabled': True,
        'password': '654321',
    }
}



# core functions
def search_user_db(username: str):
    if username in users_db:
        # como desestructuracion de javascript al que a UserDB se le pasan todas las props del diccionario seleccionado
        return UserDB(**users_db[username]) # * agrupa los parametros en una tupla # ** agrupa los parametros en un diccionario

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token) # token es el username

    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Credenciales de autenticacion invalidas', {'WWW-Authenticate': 'Bearer'})
    elif user.disabled:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Usuario inhabilitado')
    else:
        return user



# routes
@router.post('/login')
async def login_user(form: OAuth2PasswordRequestForm = Depends()):
    user_db = search_user_db(form.username)

    if not user_db:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'El usuario no existe')
    
    if form.password != user_db.password:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'La contrasenia es incorrecta')
    
    return {'access_token': user_db.username, 'token_type': 'bearer'}

@router.get('/users/me')
async def get_me(user: User = Depends(current_user)):
    return user