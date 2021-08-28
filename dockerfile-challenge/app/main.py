from functions import get_characters_info
from functions import get_characters_info_eath
from functions import get_name_location_imageLink
from flask import request
from flask import jsonify
from flask import Flask


app = Flask(__name__) # create an instance of this class

@app.route("/characters_info", methods=["GET"])
def characters_info():
    url = "https://rickandmortyapi.com/api/character/?species=human&status=alive"
    characters_info = get_characters_info(url)

    print("[ INFO ] Getting list of characters from earth locations")
    characters_info_earth = get_characters_info_eath(characters_info)

    print("[ INFO ] Getting Name, Location and image link data")
    return get_name_location_imageLink(characters_info_earth)

@app.route("/healthcheck", methods=["GET"])
def health():
    return {'message': 'Healthy'}, 200


app.run(debug=True,host="0.0.0.0")  