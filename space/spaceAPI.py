# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2023
# Copyright (c) 2023 John Capobianco

# ----------------
# Python
# ----------------
import json
import urllib3
import datetime
import requests
import rich_click as click
import django
django.setup()
from space.models import Space_Credentials,space_api_to_get,space_api_output

urllib3.disable_warnings()

db_token = Space_Credentials.objects.all().values('token')

token = db_token[0]['token']

db_api = space_api_to_get.objects.all().values('space_api')

api = db_api[0]['space_api']

class Space_Plugin():
    def space_plugin(self):
        self.get_json()
   
    def get_json(self):
        if "{ self.token }" in api:
            new_api = api.replace("{ self.token }",token)
        else:
            new_api = api
        response = requests.request("GET", new_api)
        print(f"The API response was { response.status_code }")
        json_response = response.json()

        if new_api == "http://api.open-notify.org/astros.json":
            del(json_response['message'])
        
        if "apod" in new_api:
            del(json_response['media_type'])
            del(json_response['service_version'])

        if "neo" in new_api:
            new_json_response = json_response['near_earth_objects']

            # Get first date
            first_date = list(new_json_response.keys())[0]

            # Get all NEOs on the first date
            neos_on_first_date = new_json_response[first_date]

            # Define the keys to be deleted
            keys_to_delete = ['id', 'links', 'nasa_jpl_url', 'neo_reference_id']

            # Delete the keys from each NEO on the first date
            for neo in neos_on_first_date:
                for key in keys_to_delete:
                    if key in neo:
                        del neo[key]

        if "CME" in new_api:
            today = datetime.date.today()
            filtered_response = []
            for cme in json_response:
                start_time = datetime.datetime.strptime(cme["startTime"], "%Y-%m-%dT%H:%MZ").date()
                if start_time == today:
                    filtered_response.append(cme)

            # Replace the original response with the filtered response
            json_response = filtered_response

        if 'notifications' in new_api:
            notification = json_response[0]
            del(notification['messageID'])
            del(notification['messageType'])
            del(notification['messageURL'])

        if 'EPIC' in new_api:
            first_five = []
            counter = 0
            for photo in json_response:
                if counter == 5:
                    break
                first_five.append(photo)
                counter += 1

        if 'bodies?filter[]=isPlanet,eq,true' in new_api:
            for body in json_response['bodies']:
                del(body['alternativeName'])
                del(body['bodyType'])
                del(body['id'])
                del(body['isPlanet'])
                del(body['englishName'])
                del(body['rel'])
                if 'moons' in body and isinstance(body['moons'], list) and body['moons']:
                    for moon in body['moons']:
                        del moon['rel']

        if 'rovers/?api_key=' in new_api:
            for rover in json_response['rovers']:
                if 'id' in rover:
                    del(rover['id'])
                for camera in rover['cameras']:
                    del(camera['id'])

        if "neo" in new_api:   
            chatGPTAnswer=space_api_output(space_api_output = json.dumps(neos_on_first_date,sort_keys=True,indent=4))
        elif 'notifications' in new_api:
            chatGPTAnswer=space_api_output(space_api_output = json.dumps(json_response[0],sort_keys=True,indent=4))
        elif 'eonet.gsfc.nasa.gov' in new_api:
            first_five = []
            counter = 0
            for key, value in json_response.items():
                if key == 'events':
                    for event in value:
                        if counter == 5:
                            break
                        first_five.append(event)
                        counter += 1
            chatGPTAnswer=space_api_output(space_api_output = json.dumps(first_five,sort_keys=True,indent=4))
        elif "EPIC" in new_api:
            chatGPTAnswer=space_api_output(space_api_output = json.dumps(first_five,sort_keys=True,indent=4))
        elif 'bodies?filter[]=isPlanet,eq,true' in new_api:
            chatGPTAnswer=space_api_output(space_api_output = json.dumps(json_response['bodies'],sort_keys=True,indent=4))
        elif 'rovers/?api_key=' in new_api:
            chatGPTAnswer=space_api_output(space_api_output = json.dumps(json_response['rovers'],sort_keys=True,indent=4))
        else:
            chatGPTAnswer=space_api_output(space_api_output = json.dumps(json_response,sort_keys=True,indent=4))
        chatGPTAnswer.save()    

        deleteme = space_api_to_get.objects.all()
        deleteme.delete()

@click.command()
def cli():
    invoke_class = Space_Plugin()
    invoke_class.space_plugin()

if __name__ == "__main__":
    cli()