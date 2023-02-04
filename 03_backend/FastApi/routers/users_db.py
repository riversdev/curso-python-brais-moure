from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from db.client import db_client
from db.models.user import User
from db.schemas.user import user_schema, users_schema



# instances
router = APIRouter(
    prefix='/usersdb',
    tags=['usersdb'],
    responses={status.HTTP_400_BAD_REQUEST: {'message': 'No encontrado :v'}},
)



# core functions
def search_user(key: str, value: str):
    try:
        user = db_client.users.find_one({key: value})
        
        return User(**user_schema(user))
    except:
        return None



# routes
# get
@router.get('/', response_model=list[User])
async def get_users():
    return users_schema(db_client.users.find())

# get one
@router.get('/{id}', response_model=User)
async def get_user(id: str):
    user = search_user('_id', ObjectId(id)) # ObjectId porque en la bd no se guarda un string del id, se guarda un ObjectId

    if user:
        return user
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'El usuario no existe')

# post
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=User)
async def post_user(user: User):
    if type(search_user('email', user.email)) == User:
        raise HTTPException(status.HTTP_409_CONFLICT, 'El usuario ya existe')
        
    user_dict = dict(user)
    del user_dict['id'] # eliminar el id para que mongo agregue el suyo _id

    id = db_client.users.insert_one(user_dict).inserted_id # insertar en mongo y obtener el id del documento

    return search_user('_id', ObjectId(id))

# put
@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=User)
async def put_user(user: User):
    user_dict = dict(user)
    del user_dict['id']

    try:
        db_client.users.find_one_and_replace({'_id': ObjectId(user.id)}, user_dict)
    except:
        raise HTTPException(status.HTTP_409_CONFLICT, 'Usuario no actualizado')
    
    return search_user('_id', ObjectId(user.id))

# delete
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    found = db_client.users.find_one_and_delete({'_id': ObjectId(id)})
    
    if not found:
        raise HTTPException(status.HTTP_409_CONFLICT, 'Usuario no eliminado')