import time
import os
import requests

from dotenv import load_dotenv, find_dotenv
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict

load_dotenv()

API_KEY = os.environ['API_KEY']
print(API_KEY)

r = requests.get(
    "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/mnr%2Fgtfs-mnr",
    headers={"x-api-key": API_KEY}
)

print(r)