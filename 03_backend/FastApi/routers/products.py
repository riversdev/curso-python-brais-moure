from fastapi import APIRouter

router = APIRouter(
    prefix='/products',
    tags=['products'],
    responses={404: {'message': 'No encontrado :v'}},
)

products_list = [
    {'id': 1, 'name': 'Keyboard', 'description': 'HyperX alloy origins 60'},
    {'id': 2, 'name': 'Guitar', 'description': 'Fender CD-60sce'},
    {'id': 3, 'name': 'Cubo rubik', 'description': '3*3 classic'},
]

@router.get('/')
async def get_products():
    return products_list

@router.get('/{id}')
async def get_product(id: int):
    return list(filter(lambda x: x['id'] == id, products_list))[0]