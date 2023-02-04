from pymongo import MongoClient



# local
# db_client = MongoClient().local

# remoto
db_client = MongoClient('mongodb+srv://test:test@cluster0.xibw3w1.mongodb.net/?retryWrites=true&w=majority').test # test es la bd creada