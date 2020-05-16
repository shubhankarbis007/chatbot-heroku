from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
	return "hello world"

@app.route('/bot', methods=['POST','GET'])
def bot():
	incoming_msg = request.values.get('Body', '').lower()
	resp = MessagingResponse()
	msg = resp.message()
	responded = False
	if 'hii' in incoming_msg:
		msg.body('hi i am shubhankar the bot how can i help you?')        
		# return a quote
		#r = requests.get('http://api.icndb.com/jokes/random')
		#if r.status_code == 200:
			#data = r.json()
			#quote = f'{data["content"]} ({data["author"]})'
	elif 'joke' in incoming_msg:
		msg.body('https://api.jokes.one')
		
	else:
		#quote = 'can you first introduce yourself plzz?'
        	msg.body('can you first introduce yourself plzz?')
        	responded = True
	#if 'joke' in incoming_msg:
        	#msg.body('i will tell you a joke after one week as my databse is still not ready :)')
		#return a cat pic
        	#msg.media('https://cataas.com/cat')
        	#responded = True
	if not responded:
        	msg.body('sir/madam')
	return str(resp)
if __name__ == "__main__":
            app.run()
