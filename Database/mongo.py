import datetime
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'macOS'},
    'data': datetime.datetime.utcnow()
}

db_stacks = db.stack1
stack_id = db_stacks.insert_one(stack1).inserted_id
print(stack_id, type(stack_id))
