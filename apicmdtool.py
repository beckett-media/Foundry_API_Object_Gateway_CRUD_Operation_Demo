from config import api_bearer_token,getObject_api_url,listObjects_api_url,applyAction_create_api_url,applyAction_delete_api_url,applyAction_update_api_url,objectType,primaryKey
from data import applyAction_createObject_var,applyAction_deleteObject_var,applyAction_updateObject_var
import json
import requests
from argparse import ArgumentParser

headers = {
    "Authorization": "Bearer {}".format(api_bearer_token),
    "Content-type": "application/json"}

def getObject():
    BASE_URL=getObject_api_url
    response = requests.get(BASE_URL,headers=headers)
    return response.json()

def read():
    BASE_URL=listObjects_api_url
    response = requests.get(BASE_URL,headers=headers)
    return response.json()


def applyAction_createObject():
    BASE_URL=applyAction_create_api_url
    data = applyAction_createObject_var
    response = requests.post(BASE_URL,headers=headers,data=json.dumps(data))
    return response.json()


def applyAction_deleteObject():
    BASE_URL=applyAction_delete_api_url
    data = applyAction_deleteObject_var
    response = requests.post(BASE_URL,headers=headers,data=json.dumps(data))
    return response.json()

def applyAction_updateObject():
    BASE_URL=applyAction_update_api_url
    data = applyAction_updateObject_var
    response = requests.post(BASE_URL,headers=headers,data=json.dumps(data))
    return response.json()


if __name__ == '__main__':
   parser = ArgumentParser(description='A command line tool for interacting with our API')
   parser.add_argument('-r', '--read', action='store_true', help='Sends a GET request to the product API to fetch all data from object type.')
   parser.add_argument('-g', '--getObject', action='store_true', help='Sends a GET request to API to fetch specified object data.')
   parser.add_argument('-u', '--updateObject', action='store_true', help='Sends a POST request to applyaction endpoint to udpate the object.')
   parser.add_argument('-c', '--createObject', action='store_true', help='Sends a POST request to applyaction endpoint to create the object.')
   parser.add_argument('-d', '--deleteObject', action='store_true', help='Sends a POST request to applyaction endpoint to delete the object.')

   args = parser.parse_args()

   if args.read:
       read_response = read()
       json_formatted_str = json.dumps(read_response,indent=2)
       print(json_formatted_str)
       print("list of all objects under objectType {}".format(objectType))

   if args.getObject:
       get_response = getObject()
       json_formatted_str = json.dumps(get_response,indent=2)
       print("Object under objectType {} with primaryKey {} ".format(objectType,primaryKey))
       print(json_formatted_str)

   if args.updateObject:
       update_response = applyAction_updateObject()
       if not update_response:
           print("\n Successfully updated object for object id {}\n".format(applyAction_updateObject_var['parameters']['BeckettGradingItem']))
       else:
           print(json.dumps(update_response,indent=2))

   if args.createObject:
       create_response = applyAction_createObject()
       if not create_response:
           print("\n Successfully created object  with object id {}\n".format(applyAction_createObject_var['parameters']['item_id']))
       else:
           print(json.dumps(create_response,indent=2))

   if args.deleteObject:
       delete_response = applyAction_deleteObject()
       if not delete_response:
           print("\n Successfully deleted object  with object id {}\n".format(applyAction_deleteObject_var['parameters']['item_id']))
       else:
           print(json.dumps(update_response,indent=2))
   else:
       print('Use the -h or --help flags for help')
