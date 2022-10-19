from decimal import Subnormal
from http.client import responses
import json
import csv
import requests

magherita=2
nepoletana=1
siciliana=2
farro=1
Bitalian=3
ceasers=1
lasagna=1
carbonara=2
ragu=0
gelato=4
tiramisu=2
Panna=1
lemonade=2
coke=2
water=1
order_number=1

global ldata
ldata=[{'name':'magherita','price':15,'amount':2},{'name':'blognese','price':7,'amount':1}]
while True:
    print('working')

    global response
    response = requests.post('http://localhost:5000/index', json = ldata)



