from flask import Flask
import json
import requests
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

accessToken = "LWjIXZM4dl5CrDK8zzhZN4w7XUDTd2fcHhqfSLA8"
bot_id = "0762588ce49d56ec028df8dafe"
test_id = "0757dcd554eef85ed5096a34a5"
url = "https://api.groupme.com/v3/bots/post"

payload = {'bot_id' : test_id, 'text': "Testing"}
r = requests.post(url, data = payload)

app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
	data = requests.get_json()
	
	if data['name'] != 'Test Bot':
		msg = '{}, you sent "{}".'.format(data['name'], data['text'])
		send_message(msg)
	
	return "ok", 200
	
def send_message(msg):
	url = "https://api.groupme.com/v3/bots/post"
	
	payloada = {'bot_id' : test_id, 'text': msg}
	r = requests.post(url, data = payloada)
	json = urlopen(request).read().decode()
