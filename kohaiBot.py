from flask import requests, Flask, json

URL = "https://api.groupme.com/v3/bots/post"
accessToken = "LWjIXZM4dl5CrDK8zzhZN4w7XUDTd2fcHhqfSLA8"
bot_id = "0762588ce49d56ec028df8dafe"
test_id = "0757dcd554eef85ed5096a34a5"
text = "Hope you all have a great day today!"
payload = {"bot_id" : test_id, "text" : text}
received = {"bot_id" : test_id, "text" : "Message received!"}

r = requests.post(URL, data=payload)

app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	
	if data['name'] != 'Test Bot':
		msg = '{}, you sent "{}".'.format(data['name'], data['text'])
		send_message(msg)
	return "ok", 200
	
def send_message(msg):
	data = 	{
			 'bot_id' : test_id,
			 'text'	: msg,
			}
	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()