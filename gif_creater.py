import sys
import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import requests
import json
import urllib
from random import randint

def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]

def create_gif(word_list):
    input1, input2 = split_list(word_list)
    gif_input1 = ' '.join(input1)
    gif_input2 = ' '.join(input2)
    if (randint(1,2) == 1):
        gif_input = gif_input1
    else:
        gif_input = gif_input2
    # create an instance of the API class
    api_instance = giphy_client.DefaultApi()
    api_key = 'hcEWU2HFEOYx0HU0mPvh4pKNRbOJUJAN' # str | Giphy API Key.
    q = gif_input # str | Search query term or prhase.
    limit = 2 # int | The maximum number of records to return. (optional) (default to 25)
    offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
    rating = 'g' # str | Filters results by specified rating. (optional)
    lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
    fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
    try: 
        # Search Endpoint
        api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
        count = 0
        for gifs in api_response.__dict__['_data']:
            count += 1
            gif = gifs.__dict__
            image = gif['_images'].__dict__
            url = image['_downsized'].__dict__['_url']
            print url
            urllib.urlretrieve(url, 'myfile%d.gif'%(count))            
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)    


if __name__ == "__main__":
    create_gif(['take','me','to','church'])
