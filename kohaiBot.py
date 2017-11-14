from flask import requests, Flask, json

URL = "https://api.groupme.com/v3/bots/post"
accessToken = "LWjIXZM4dl5CrDK8zzhZN4w7XUDTd2fcHhqfSLA8"
bot_id = "0762588ce49d56ec028df8dafe"
test_id = "0757dcd554eef85ed5096a34a5"
received = {"bot_id" : test_id, "text" : "Message received!"}

app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	
	if data['name'] != 'Test Bot':
		msg = '{}, you sent "{}".'.format(data['name'], data['text'])
		send_message(msg)
	return "ok", 200
	
def send_message(msg):
	payload = 	{
			 'bot_id' : test_id,
			 'text'	: msg,
			}
	r = requests.post(URL, data=payload)
	json = urlopen(request).read().decode()