import pymongo

from pymongo import Connection
connection = Connection('localhost', 27017)

db = connection.testing

responses = db.responses

item = responses.find_one()

print item['author']
