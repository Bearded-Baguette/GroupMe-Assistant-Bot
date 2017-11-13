import requests

group_id = 35125865
URL = "https://api.groupme.com/v3/bots/post"
accessToken = "LWjIXZM4dl5CrDK8zzhZN4w7XUDTd2fcHhqfSLA8"
bot_id = "0762588ce49d56ec028df8dafe"
text = "I'm still learning how to communicate! Bear with me for a moment!"
payload = {"bot_id" : bot_id, "text" : text}

r = requests.post(URL, data=payload)
