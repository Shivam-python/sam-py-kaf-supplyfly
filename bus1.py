from pykafka import KafkaClient
import json
from datetime import datetime
import uuid
import time
import requests
import polyline
from itertools import permutations
import math


#READ COORDINATES FROM GEOJSON
input_file = open('./indore/silicon.json')
json_array = json.load(input_file)
coordinates = json_array['features'][0]['geometry']['coordinates']

#GENERATE UUID
def generate_uuid():
    return uuid.uuid4()

#KAFKA PRODUCER
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['geodata']
producer = topic.get_sync_producer()

#CONSTRUCT MESSAGE AND SEND IT TO KAFKA
data = {}
data['busline'] = '00001'

def preset_coordinates(coordinates):
    # @TODO This is to be removed. This is just a patch
    # altering order of lat-long data for drawing polyline.
    fixed = []
    for i in range(len(coordinates)):
        fixed.append([coordinates[i][1],coordinates[i][0]])
    return fixed

def generate_checkpoint(coordinates):
    i = 0
    coordinates = preset_coordinates(coordinates)
    route = coordinates#get_navigation_route_with_stops(coordinates)
    print("initial route calculated")
    while i < len(coordinates):
        data['key'] = data['busline'] + '_' + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['current'] = {'latitude': coordinates[i][0],'longitude': coordinates[i][1]}
        data['route'] = route

        message = json.dumps(data)
        producer.produce(message.encode('ascii'))
        time.sleep(1)

        #if bus reaches last coordinate, start from beginning
        if i == len(coordinates)-1:
            i = 0
            route = coordinates
        else:
            i += 1
            route = coordinates[i:]

generate_checkpoint(coordinates)