# ==============================================
# NAME: SpartanNash BiZZDesign Mass Update Script 
# 
# VERSION: 2.2
# 
# LAST UPDATED: 01-08-25
# 
# AUTHOR(S): Isaiah Parker
# 
# DESCRIPTION: This script makes use of 
# BiZZDesigns API to update data blocks
# on a larger scale
# ==============================================


# Dependencies
import requests
import jmespath
import csv
import os
import json

from dotenv import load_dotenv, dotenv_values

load_dotenv()

# Get from .env file
BASE_URL = os.getenv("BASE_URL")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


# Class Desc: Handles bearer tokens
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


# Funtion Desc: This function gets the authorization   
def getAuth():
    payload = {"grant_type" : "client_credentials", "client_id" : os.getenv("CLIENT_ID"), "client_secret" : CLIENT_SECRET}

    # From .env file
    AUTH_URL = os.getenv("AUTH_URL")
    
    # POST API request
    a = requests.post(AUTH_URL,params=payload)

    # Format into JSON
    acc = a.json()

    # Create BearerAuth object to handle requests
    access_token = acc["access_token"]
    auth = BearerAuth(access_token)

    return auth


# Function Desc: This function locates (an) object(s) that meet(s) a certain criteria, an then
# updates a specified attribute in a specific data block
def findAndUpdateBlock(find_attribute, find_value, update_attribute, update_value):
    payload = {"collaborationId" : "repositories/6/collaborations/8", "type" : "ArchiMate:ApplicationComponent", "limit" : "2000"}
    
    # Get all data block definitions
    s = requests.get(BASE_URL + "/schemas", auth=getAuth())
    schemas = s.json()

    # Find the appopriate name and namespace for the target datablock
    schemaName = jmespath.search(f"*[?fields[?name == '{update_attribute}']].name[]", schemas)[0]
    schemaNamespace = jmespath.search(f"*[?fields[?name == '{update_attribute}']].namespace[]", schemas)[0]

    
    # Get all objects
    r = requests.get(BASE_URL + "/objects",params=payload, auth=getAuth())
    objects = r.json()
    
    # Filter all objects based on the key value
    filtered_objects = jmespath.search(f"_items[?documents[?values.{find_attribute}=='{find_value}']]", objects)

    

    # Traverse filtered objects
    for obj in filtered_objects:
        if obj == None: 
            continue

        print(json.dumps(obj, indent=4))
        update_block = jmespath.search(f"documents[?schemaName == '{schemaName}']", obj)
        print(json.dumps(update_block, indent=4))

        # Format data as JSON
        data = {
            "objectId" : obj["id"],
            "schemaNamespace" : schemaNamespace,
            "schemaName" : schemaName,
            "values" :{
                f"{update_attribute}" : f"{update_value}"
            }    
        }
        
        # Check if target block exists
        if not update_block:
            # We have to create a new block!" 
            print(requests.post(BASE_URL + "/documents", json=data, auth=getAuth()))
        else:
           # "We have to update the existing block
           # print("EXISTING")
           print(requests.patch(BASE_URL + "/documents/" + update_block[0]["id"], json=data, auth=getAuth()))
           


def main():
    # Manage csv
    with open('map.csv', encoding='utf-8-sig') as data_file:
            
            read = csv.reader(data_file)

            data_read = list(read)

            # Get params before data
            find_attr =  data_read[0][0]
            update_attr = data_read[0][1]

            print(f"{find_attr} {update_attr}")

            # Traverse through csv and send a request for each valid row
            for find_val, update_val in data_read[1:]:  
                print(f"{find_val}: {update_val}")
                findAndUpdateBlock(find_attr, find_val, update_attr, update_val)

            print("Complete.")
main()