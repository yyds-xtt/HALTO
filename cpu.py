from flask import Flask, request
from threading import Thread
import requests
import json
import os
import time
headers = {'Content-Type': 'application/json'}
app = Flask(__name__)

@app.route('/',methods=['POST'])
def sockeeet():
	req=request.get_json()
	print(req)
	def computing():	os.system("stress-ng -c 0 -l "+str(req['data'])+' --timeout 7')
	Thread(target=computing).start()			
	i=0
	while i<5:
		with open("output.txt") as f:
			cpu_data={'instance':0,'data':f.read()[-56:-51]}
			print(cpu_data)
			r=requests.request('POST','http://192.168.8.139:5000', headers=headers, data=json.dumps(cpu_data))
			time.sleep(1)
		i+=1
	r=requests.request('POST','http://192.168.8.139:5000', headers=headers, data=json.dumps({'instance':7,'data':0}))
if __name__ == '__main__':
	def writing():	os.system("sar 1 >output.txt")
	Thread(target=writing).start()
	app.debug = True
	app.run(host='0.0.0.0',port=11111)