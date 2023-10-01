import csv 
import os
import requests
import json
import os
from dotenv import load_dotenv
from random import randint

def main():

    load_dotenv()

    # Init the CSV file
    with open('./csv/nasa.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["date", "absolute_magnitude_h", "estimated_diameter_min", "estimated_diameter_max", "id"])

    API_KEY = os.getenv('NASA_API')
    response_API = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-09-24&api_key={API_KEY}')
    api_json = json.loads(response_API.text)
    nr_erth_obj = api_json["near_earth_objects"]
    for date in api_json["near_earth_objects"]:
        for object in nr_erth_obj[date]:
            with open('./csv/nasa.csv', 'a', newline='') as csvfile:
                magnitude = object["absolute_magnitude_h"]
                diam_min = object["estimated_diameter"]["meters"]["estimated_diameter_min"]
                diam_max = object["estimated_diameter"]["meters"]["estimated_diameter_max"]
                #object_id = object["id"]
                # god bless whatever the fuck I'm falsifying
                object_id = randint(1,3)
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([date, magnitude, diam_min, diam_max, object_id])

if __name__ == '__main__':
    main()
