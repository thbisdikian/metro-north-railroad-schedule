import time
import os
import requests

from dotenv import load_dotenv, find_dotenv
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict

load_dotenv()

API_KEY = os.environ['API_KEY']

response = requests.get(
    "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/mnr%2Fgtfs-mnr",
    headers={"x-api-key": API_KEY}
)

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(response.content)
train_data = protobuf_to_dict(feed)['entity']

hudson_trips = []

for trip in train_data:
    if trip['trip_update']['trip']['route_id'] == '1':
        hudson_trips.append(trip)

for trip in hudson_trips:
    print(trip)