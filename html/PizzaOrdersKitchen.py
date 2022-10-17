
from flask import Flask
from flask import render_template
from flask import request, redirect
import json
import random


app = Flask(__name__)
currentReadings = []
Orders={}
global removeid
removeid=0

@app.route('/data', methods = ['POST'])
def also_add_volunteer():
    data = request.get_json()
    order_number=data['order_number']
    Orders[order_number]={'order_number':data['order_number'],'magherita':data['magherita'],'nepoletana':data['napoletana'],'siciliana':data['siciliana'],'farro':data['farro'],'Bitalian':data['Bitalian'],'ceasers':data['ceasers'],'lasagna':data['lasagna'],'corbonara':data['corbonara'],'ragu':data['ragu'],'gelato':data['gelato'],'tiramisu':data['tiramisu'],'PC':data['PC'],'lemonade':data['lemonade'],'coke':data['coke'],'water':data['water']}
    return render_template('index.html',
        Orders=Orders)
print(Orders)
@app.route('/')
def ret():
    return render_template('PizzaOrders.html',
        Orders=Orders)

@app.route('/remove',methods = ['POST'])
def remove():
    global removeid

    removeid+=1

    Orders[removeid]={'order_number':0,'magherita':0,'nepoletana':0,'siciliana':0,'farro':0,'Bitalian':0,'ceasers':0,'lasagna':0,'corbonara':0,'ragu':0,'gelato':0,'tiramisu':0,'PC':0,'lemonade':0,'coke':0,'water':0}

    print(removeid)
    print(Orders)
    return render_template('PizzaOrders.html',
    Orders=Orders)
    