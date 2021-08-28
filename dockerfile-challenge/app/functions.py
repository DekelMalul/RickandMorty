import requests 
import csv

def get_characters_info(url):
    characters_info = list()
    try:
        while url is not None:
            print("[ INFO ] Getting data from",url)
            response = requests.get(url)
            response.encoding = "utf-8"
            response_json = response.json()
            characters_info = characters_info + response_json["results"]
            url = response_json["info"]["next"]
        return characters_info
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')  

def get_characters_info_eath(characters_info):
    characters_info_earth = list()
    for character_info in characters_info:
        if "Earth" in character_info["location"]["name"]:
            characters_info_earth.append(character_info)
    return characters_info_earth

def get_name_location_imageLink(characters_info_earth):
    character_location_imageLink_dict = dict()
    character_location_imageLink_dict["results"] = dict()
    character_id = 0
    
    for character_info_earth in characters_info_earth:
        character_name = character_info_earth["name"]
        character_location = character_info_earth["image"]
        character_image_link = character_info_earth["location"]["name"]
        character_location_imageLink_dict["results"][character_id] = dict()
        character_location_imageLink_dict["results"][character_id]["name"] = character_name
        character_location_imageLink_dict["results"][character_id]["location"] = character_location
        character_location_imageLink_dict["results"][character_id]["image_link"] = character_image_link
        character_id += 1

    return character_location_imageLink_dict