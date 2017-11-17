from flask import Flask, request
import json
import requests
import pprint
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen
import time

botName = "Michiko"
botNickName = "Miko-kun"
accessToken = "LWjIXZM4dl5CrDK8zzhZN4w7XUDTd2fcHhqfSLA8"
bot_id = "0762588ce49d56ec028df8dafe"
test_id = "0757dcd554eef85ed5096a34a5"
url = "https://api.groupme.com/v3/bots/post"
group_id = "36138177"
request_params = {'token': accessToken}

pp = pprint.PrettyPrinter(indent=4)

def postMessage(msg):
	url = "https://api.groupme.com/v3/bots/post"
	bot_id = test_id
	payload = {'bot_id' : bot_id, 'text': msg}
	requests.post(url, data = payload)


wakeUpText = "Hello friends! My name is " + botName + ", but you can call me " + botNickName + "! I am the new assistant for your chat! I do not know how to do many things, but I will learn more and continue to improve as time goes on! I'm excited to meet you all!"
postMessage(wakeUpText)


while True:
	response = requests.get('https://api.groupme.com/v3/groups/36138177/messages', params = request_params)
	if (response.status_code == 200):
		response_messages = response.json()['response']['messages']

	for message in response_messages:
		if(message['text'] == "What's the forecast " + botNickName + "?"):
			location_name = 'Penn State Behrend'
			location_coords = {'x':'-79.9880', 'y':'42.1189'}
			request_params = {'token':accessToken}
			weather_response=requests.get('https://api.weather.gov/points/'+ location_coords['y'] + ',' + location_coords['x'] + '/forecast').json()
			current_weather = weather_response['properties']['periods'][0]['detailedForecast']
			weather_text = 'Weather for ' + location_name + ': ' + current_weather
			postMessage(weather_text)
			request_params['since_id'] = message['id']
			break
	
	time.sleep(5)
