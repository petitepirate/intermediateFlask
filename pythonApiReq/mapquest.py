import requests 
from secrets import key


response = requests.get('http://open.mapquestapi.com/geocoding/v1/address', params ={'key': key, 'location': 'Denver, CO'})
