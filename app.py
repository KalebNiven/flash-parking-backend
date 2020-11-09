from flask import Flask, request, redirect, session, url_for, jsonify, Response
from flask_cors import CORS, cross_origin
from database import *
import pymongo
from pprint import pprint
import json



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#database client
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#database
# mydb = myclient["mydatabase"]



@app.route("/getParkingLot", methods=['GET'])
def getParkingLot():
	res = None

	if request.method == 'GET':
		arg_list = request.args
		lot = arg_list['lot']
		currentLot = database[lot]

	res = currentLot
	pprint(res)

	return jsonify(res)


@app.route("/arrival", methods=['POST'])
def arrival():
	res = None
	print(request)
	if request.method == 'POST':
		
		arg_list = request.data
		arg_list = json.loads(arg_list)
		print(arg_list)
		totalParkingSpots = arg_list['totalParkingSpots']
		carsInLot = arg_list['carsInLot']
		spotsAvailable = arg_list['spotsAvailable']

		
		carsInLot +=1 
		spotsAvailable -= 1

		res = {'totalParkingSpots': totalParkingSpots, 'carsInLot': carsInLot, 'spotsAvailable': spotsAvailable}

	return jsonify(res)


@app.route("/departure", methods=['POST'])
def departure():
	res = None

	if request.method == 'POST':
		
		arg_list = request.data
		arg_list = json.loads(arg_list)
		print(arg_list)
		totalParkingSpots = arg_list['totalParkingSpots']
		carsInLot = arg_list['carsInLot']
		spotsAvailable = arg_list['spotsAvailable']

		
		carsInLot -= 1
		spotsAvailable += 1


		res = {'totalParkingSpots': totalParkingSpots, 'carsInLot': carsInLot, 'spotsAvailable': spotsAvailable}

	return jsonify(res)


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
