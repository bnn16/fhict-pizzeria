
from flask import Flask
from flask import render_template
from flask import request, redirect
import json
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
currentReadings = []
Orders={}
removeid=1
DOrders={}
data={}
order_num_test= 0
global orderNum
ordernum= -1
if ordernum<0:
    ordernum=0
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global data, order_number, order_num_test,ordernum
        data = request.json
        
        for entry in data:
            order_number =entry['orderNum'] +ordernum
        ordernum=ordernum+1
        Orders[order_number]=data
        print(data)
        if order_number in Orders:
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return render_template("PizzaOrders.html",
    Orders=Orders, order_number = order_number)
print(Orders)
@app.route('/')
def ret():
    
    return render_template('PizzaOrders.html',
        Orders=Orders)

@app.route('/remove',methods = ['POST'])
def remove():
    
    Orders[removeid]={'order_number':0-removeid,'magherita':data['magherita'],'nepoletana':data['nepoletana'],'siciliana':data['siciliana'],'farro':data['farro'],'Bitalian':data['Bitalian'],'ceasers':data['ceasers'],'lasagna':data['lasagna'],'corbonara':data['corbonara'],'ragu':data['ragu'],'gelato':data['gelato'],'tiramisu':data['tiramisu'],'PC':data['PC'],'lemonade':data['lemonade'],'coke':data['coke'],'water':data['water']}
    Dorder_number=Orders[removeid]['order_number']
    DOrders[Dorder_number]={'order_number':Dorder_number,'magherita':data['magherita'],'nepoletana':data['nepoletana'],'siciliana':data['siciliana'],'farro':data['farro'],'Bitalian':data['Bitalian'],'ceasers':data['ceasers'],'lasagna':data['lasagna'],'corbonara':data['corbonara'],'ragu':data['ragu'],'gelato':data['gelato'],'tiramisu':data['tiramisu'],'PC':data['PC'],'lemonade':data['lemonade'],'coke':data['coke'],'water':data['water']}
    print(removeid)
    print(Orders)
    return render_template('PizzaOrders.html',
    DOrders=DOrders,
    Orders=Orders)

