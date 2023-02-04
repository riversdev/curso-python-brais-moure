from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'message': 'No encontrado :v'}},
)

# Entidad
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str

users_list = [
    User(id = 1, name = 'Brais', surname = 'Moure', age = 35, url = 'https://moure.dev'),
    User(id = 2, name = 'Moure', surname = 'Dev', age = 35, url = 'https://mouredev.com'),
    User(id = 3, name = 'Alejandro', surname = 'Rios', age = 23, url = 'https://rivers.dev'),
]

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)

    try:
        return list(users)[0]
    except:
        return None


# routes
# get
@router.get('/')
async def get_users():
    return users_list


# path parameters
@router.get('/{id}', response_model=User) # response_model es el modelo de respuesta sirve para la documentacion
async def get_user(id: int):
    user = search_user(id)

    if user:
        return user
    else:
        raise HTTPException(404, 'El usuario no existe') # siempre lanzar un error con "raise"


# query parameters
@router.get('/query/', response_model=User)
async def get_user(id: int):
    user = search_user(id)

    if user:
        return user
    else:
        raise HTTPException(404, 'El usuario no existe')


# post
@router.post('/', status_code=201, response_model=User) # status_code es el codigo de respuesta por defecto
async def post_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(409, 'El usuario ya existe')
    else:
        users_list.append(user)
        return user


# put
@router.put('/', status_code=202, response_model=User)
async def put_user(user: User):
    found = False

    for i, saved_user in enumerate(users_list): # tener indices en un for ################################
        if saved_user.id == user.id:
            users_list[i] = user
            found = True
    
    if found:
        return user
    else:
        raise HTTPException(409, 'Usuario no encontrado')


# delete
@router.delete('/{id}', status_code=202, response_model=None)
async def delete_user(id: int):
    found = False

    for i, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[i]
            found = True
    
    if found:
        return
    else:
        raise HTTPException(409, 'Usuario no encontrado')