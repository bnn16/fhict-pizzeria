from flask import Flask
from flask import render_template
from flask import request, redirect
import json
import random
import requests
import csv
from flask_cors import CORS
from fhict_cb_01.CustomPymata4 import CustomPymata4
import time
import sys

DHTPIN  = 12
LDRPIN = 2

global board
board = CustomPymata4(com_port = "COM7")
board.set_pin_mode_dht(DHTPIN, sensor_type=11, differential=0.05)


app = Flask(__name__)

CORS(app)
currentReadings = []
currentNames = []
currentAmounts = []
nameQuantity = []
allNumberQuantity = []
orderNumbers = []
thisOrderName = []
allOrderNames = []
orderIndexes = []
orderIndexes1 = []
pickupOrderIndexes = []
pickupOrderNumbers = []
pickupAllNumberQuantity = []

Orders={}

global removeid
removeid = 0
pickupCounter = -1

totalQuantity = 0
orderIndex = 0
lenSofar = 0
thisOrderQuantity = 0
counter = 0
currentIndex = -1
orderDifferential = 0
subtractor = 0

removeid=1
DOrders={}
data={}
order_num_test= 0
global orderNum
ordernum= -1
if ordernum<0:
    ordernum=0
order_number = 0


empty = 0

Key2Name =  { # To display the proper name from the key value
'margherita': 'Pizza Margherita',
'napoletana': 'Pizza Napoletana',
'siciliana': 'Pizza Siciliana',
'farro': 'Farro Salad',
'ceaser': 'Ceaser Salad',
'italian': 'Big Italian Salad',
'lasagna': 'Lasagna',
'carbonara': 'Carbonara',
'ragu': 'Spaghetti al ragú', 
'gelato': 'Gelato', 
'tiramisu': 'Tiramisu',
'panna': 'Panna Cotta',
'lemoande': 'Lemonade',
'cola': 'Coca Cola',
'water': 'Water'
}

with open('OrderHistory.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow("Order")

@app.route('/data', methods = ['POST'])
def also_add_volunteer(allNumberQuantity = allNumberQuantity, orderIndex = orderIndex, currentNames = currentNames, currentAmounts = currentAmounts, empty = empty, orderDifferencial = orderDifferential, subtractor = subtractor, orderIndexes = orderIndexes, orderIndexes1 = orderIndexes1, pickupCounter = pickupCounter):
    data = request.get_json()
    order_number=data['order_number']
    Orders[order_number]={'order_number':data['order_number'],'magherita':data['magherita'],'nepoletana':data['napoletana'],'siciliana':data['siciliana'],'farro':data['farro'],'Bitalian':data['Bitalian'],'ceasers':data['ceasers'],'lasagna':data['lasagna'],'corbonara':data['corbonara'],'ragu':data['ragu'],'gelato':data['gelato'],'tiramisu':data['tiramisu'],'PC':data['PC'],'lemonade':data['lemonade'],'coke':data['coke'],'water':data['water']}
    return render_template('PizzaOrders.html',
        Orders=Orders, orderIndexes = orderIndexes)



@app.route('/index', methods=['GET', 'POST'])
def index(orderIndex = orderIndex, allNumberQuantity = allNumberQuantity, counter = counter, totalQuantity = totalQuantity, thisOrderQuantity = thisOrderQuantity, lenSofar = lenSofar, thisOrderName = thisOrderName, allOrderNames = allOrderNames, orderNumbers = orderNumbers, currentIndex = currentIndex, empty = empty, orderDifferencial = orderDifferential, subtractor = subtractor, orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes, pickupCounter = pickupCounter):

    if request.method == 'POST':
        global data, order_number, order_num_test,ordernum, name, amount
        data = request.json

        
        if totalQuantity == thisOrderQuantity:
                thisOrderName = []
                nameQuantity = []
                lenSofar += thisOrderQuantity
                thisOrderQuantity = 0

        totalQuantity = len(data) - lenSofar
        print("totalQuantity: "+str(totalQuantity))
        
        for entry in data:
            thisOrderQuantity += 1

            
            
            print("thisOrderQuantity: "+str(thisOrderQuantity))


            order_number =entry['orderNum'] +ordernum
            print("order_number = "+str(order_number))
            orderIndex = order_number - 1

            print("orderIndex = "+str(orderIndex))

            name = entry['name']
            print(name)
            currentNames.append(name)
            print(currentNames)

            amount = entry['amount']
            print(amount)
            currentAmounts.append(amount)
            print("amounts: "+str(currentAmounts))

            nameQuantity.append(("".join((Key2Name[name]," x ",str(amount)))))
            print("nQ: "+str(nameQuantity))
            
            thisOrderName.append(name)
            print("tON: "+str(thisOrderName))
            
        allOrderNames.append(thisOrderName)
        print("allOrderNames = "+str(allOrderNames))
        orderNumbers.append(order_number)
        print("oN: "+str(orderNumbers))
        # counter = order_number
        # print("The Counter is: "+str(counter))
        ordernum = ordernum+1
        pickupCounter = orderNumbers[-1]
        print("orderNumbers[-1]: "+str(orderNumbers[-1]))
        print("Order number: "+str(order_number))
        print(("PICKUP: "+str(pickupCounter)))
        allNumberQuantity.append(nameQuantity)
        print("ANQ: "+str(allNumberQuantity))
        Orders[order_number] = data
        print(data)

        orderIndexes.clear()

        print("orderIndexes: "+str(orderIndexes))

        for i in range(0, len(allNumberQuantity)):
            orderIndexes.append(i)
        print("orderIndexes: "+str(orderIndexes))

        orderIndexes1 = orderIndexes

        print("orderIndexes1: "+str(orderIndexes1))




        if order_number in Orders:
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        
    return render_template("PizzaOrders.html",
    Orders=Orders, order_number = order_number, name = name, amount = amount, currentNames = currentNames, currentAmounts = currentAmounts, allNumberQuantity = allNumberQuantity, orderIndex = orderIndex, orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes, orderNumbers = orderNumbers, allOrderNames = allOrderNames, empty = empty, orderDifferential = orderDifferential, pickupCounter = pickupCounter)
print("+++++++++++++++++++++++"+str(orderIndexes1))


@app.route('/', methods = ['GET','POST'])
def ret(pickupOrderIndexes = pickupOrderIndexes, pickupOrderNumbers = pickupOrderNumbers, pickupAllNumberQuantity = pickupAllNumberQuantity, empty = empty, orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes):
    
    
    orderIndexes1 = orderIndexes
    
    humidity, temperature, timestamp = board.dht_read(DHTPIN)
    brightness, timestamp = board.analog_read(LDRPIN)

    print("Temp: "+str(temperature))
    print("Bright: "+str(brightness))
    print("**orderIndexes: "+str(orderIndexes)+"**")
    print("**orderIndexes1: "+str(orderIndexes1)+"**")
    print("orderNumbers: "+str(orderNumbers))

    


    return render_template('PizzaOrders.html',
        Orders = Orders, order_number = order_number, allNumberQuantity = allNumberQuantity, currentNames = currentNames, currentAmounts = currentAmounts, orderIndex = orderIndex, orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes, orderNumbers = orderNumbers, allOrderNames = allOrderNames, empty = empty, temperature = temperature, brightness = brightness)


@app.route('/remove',methods = ['GET','POST'])
def remove(orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes, orderNumbers = orderNumbers, pickupCounter = pickupCounter + 1):
    print("_________Your Order has been placed in the oven!_____________"+str(orderIndexes1)+str(orderIndexes))

    print("orderIndexes: "+str(orderIndexes1))
    print("orderNumbers: "+str(orderNumbers))
    print("allNumberQuantity: "+str(allNumberQuantity))

    print("--------------------------------------------")

    print("pickup Counter: "+str(pickupCounter))

    # pickupOrderIndexes.append((orderIndexes[0]))
    # global calculation
    # global itm
    # itm = orderIndex[0]
    # calculation = itm + pickupCounter
    # print("CALCULATION = "+str(calculation))
    ## pickupOrderIndexes.append(orderIndexes[0]) # pickup page grabs the first item from the order indexes
    ## pickupOrderNumbers.append((orderNumbers[0])) # pickup page grabs the first item from the order numbers
    pickupAllNumberQuantity.append((allNumberQuantity[0]))

    pickupOrderIndexes.clear()

    pickupOrderNumbers.clear()

    print("pickupOrderNumbers: "+str(pickupOrderNumbers))

    print("pickupOrderIndexes: "+str(pickupOrderIndexes))

    for a in range(0, len(pickupAllNumberQuantity)):
        pickupOrderIndexes.append(a)
        pickupOrderNumbers.append(a + 1)
    print("pickupOrderIndexes: "+str(pickupOrderIndexes))

    

    ## for e in range(1, len(pickupAllNumberQuantity)):
    ##     pickupOrderNumbers.append(e)
    ## print("pickupOrderNumbers: "+str(pickupOrderNumbers))



    orderIndexes.pop(-1) # Removes the first item
    allNumberQuantity.pop(0)

    print("orderIndexes: "+str(orderIndexes1))
    print("orderNumbers: "+str(orderNumbers))
    print("allNumberQuantity: "+str(allNumberQuantity))

    return render_template("PizzaOrders.html",
    Orders=Orders, order_number = order_number, currentNames = currentNames, currentAmounts = currentAmounts, allNumberQuantity = allNumberQuantity, orderIndex = orderIndex, orderNumbers = orderNumbers, allOrderNames = allOrderNames, empty = empty, orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes)
print(Orders)

    # global removeid

    # removeid+=1

    # Orders[removeid]={'order_number':0,'magherita':0,'nepoletana':0,'siciliana':0,'farro':0,'Bitalian':0,'ceasers':0,'lasagna':0,'corbonara':0,'ragu':0,'gelato':0,'tiramisu':0,'PC':0,'lemonade':0,'coke':0,'water':0}

    
    # Orders[removeid]={'order_number':0-removeid,'magherita':data['magherita'],'nepoletana':data['nepoletana'],'siciliana':data['siciliana'],'farro':data['farro'],'Bitalian':data['Bitalian'],'ceasers':data['ceasers'],'lasagna':data['lasagna'],'corbonara':data['corbonara'],'ragu':data['ragu'],'gelato':data['gelato'],'tiramisu':data['tiramisu'],'PC':data['PC'],'lemonade':data['lemonade'],'coke':data['coke'],'water':data['water']}
    # Dorder_number=Orders[removeid]['order_number']
    # DOrders[Dorder_number]={'order_number':Dorder_number,'magherita':data['magherita'],'nepoletana':data['nepoletana'],'siciliana':data['siciliana'],'farro':data['farro'],'Bitalian':data['Bitalian'],'ceasers':data['ceasers'],'lasagna':data['lasagna'],'corbonara':data['corbonara'],'ragu':data['ragu'],'gelato':data['gelato'],'tiramisu':data['tiramisu'],'PC':data['PC'],'lemonade':data['lemonade'],'coke':data['coke'],'water':data['water']}
    # print(removeid)
    # print(Orders)

    # return render_template('PizzaOrders.html',
    # DOrders=DOrders,
    # Orders=Orders)

@app.route('/pickup', methods = ['GET','POST'])
def pickup(pickupOrderIndexes = pickupOrderIndexes, pickupOrderNumbers = pickupOrderNumbers, pickupAllNumberQuantity = pickupAllNumberQuantity, orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes):
    return render_template("Pick-up.html", pickupOrderIndexes = pickupOrderIndexes, pickupOrderNumbers = pickupOrderNumbers, pickupAllNumberQuantity = pickupAllNumberQuantity, orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes)

@app.route('/deliver', methods = ['GET','POST'])   
def deliver(pickupOrderIndexes = pickupOrderIndexes, pickupOrderNumbers = pickupOrderNumbers, pickupAllNumberQuantity = pickupAllNumberQuantity, orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes):

    # with open('OrderHistory.csv', 'a') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(str(pickupAllNumberQuantity[0]))

    pickupOrderIndexes.pop(-1)
    pickupOrderNumbers.pop(0)
    pickupAllNumberQuantity.pop(0)

    return render_template("Pick-up.html", pickupOrderIndexes = pickupOrderIndexes, pickupOrderNumbers = pickupOrderNumbers, pickupAllNumberQuantity = pickupAllNumberQuantity, orderIndexes1 = orderIndexes1, orderIndexes = orderIndexes)

@app.route('/oven', methods = ['GET','POST'])
def ovengo():
    board.displayShow(88)
    print("Your Pizza is being placed in the oven")
    return redirect('/')