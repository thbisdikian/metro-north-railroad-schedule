""" a library of functions used to read data from the MTA static files """
import csv

def readStops():
    with open('.\\static\\stops.txt', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print("id: {}, name: {}".format(row['stop_id'], row['stop_name']))
    return

def getStopIDFromName(name):
    with open('.\\static\\stops.txt', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['stop_name'] == name:
                return row['stop_id']
        else:
            raise Exception('Invalid stop name: {}'.format(name))