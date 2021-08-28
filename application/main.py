from functions import get_characters_info
from functions import get_characters_info_eath
from functions import get_name_location_imageLink
from functions import save_data_to_csv
   


url = "https://rickandmortyapi.com/api/character/?species=human&status=alive"
characters_info = get_characters_info(url)

print("[ INFO ] Getting list of characters from earth locations")
characters_info_earth = get_characters_info_eath(characters_info)

print("[ INFO ] Getting Name, Location and image link data")
character_location_imageLink_list = get_name_location_imageLink(characters_info_earth)

print("[ INFO ] Saving the data to csv file RickandMorty.csv")
save_data_to_csv(character_location_imageLink_list)
