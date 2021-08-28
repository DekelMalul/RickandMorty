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
    character_location_imageLink_list = list()
    
    for character_info_earth in characters_info_earth:
        character_name = character_info_earth["name"]
        character_location = character_info_earth["location"]["name"]
        character_image_link = character_info_earth["image"]
        character_location_imageLink_list.append(character_name + "," + character_location + "," + character_image_link)

    return character_location_imageLink_list

def save_data_to_csv(character_location_imageLink_list):
    header = ["name","location","image_link"]
    with open('RickandMorty.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for character_info in character_location_imageLink_list:
            character_row = character_info.split(",")
            writer.writerow(character_row)
    file.close()