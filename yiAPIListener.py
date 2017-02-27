import logging
import re, json, threading


'''
Constantly listen to opened Yi4k camera for sultable response.
Most of response will be the result of commands sent to camera, while some of the responce
is camera state, pushed periodically.
'''

class YiAPIListener(threading.Thread):
	assignedCBA= []	#(template, cb) collection
	constantCB= {}

	jsonStream= None

	def __init__(self, _sock):
		threading.Thread.__init__(self)

		self.sock= _sock
		self.assignedCBA= []
		self.constantCB= {}
		self.jsonStream= JSONStream()

		self.start()





	def run(self):
		while True:
			logging.info('Wait...')
			try:
				recv= self.sock.recv(1024)
			except:
				logging.info("...stopped")
				return

			logging.debug("Part %db" % len(recv))
			jsonA= self.jsonStream.find(recv.decode())

			for resJSON in jsonA:
				logging.info('Res %s' % str(resJSON))
				if not 'msg_id' in resJSON:
					logging.warning('Insufficient response, no msg_id')

					continue


				self.assignedCBA= self.applyCB(self.assignedCBA, resJSON)

				self.applyCB(self.constantCB, resJSON)



	'''
	Assign one-time callback for awaited command responce.
	'''
	def instantCB(self, _template, _cb):
		self.assignedCBA.append({'template':_template, 'cb':_cb})




	'''
	Rolling over assigned callbacks, call them if all of template values exists in response.
	Then wipe callback out.
	'''
	def applyCB(self, _assignedCBA, _res):
		unusedCBA= []

		for cCB in _assignedCBA:
			callbackMatch= True
			for cField in cCB['template']:
				if (cField not in _res) or (cCB['template'][cField]!=_res[cField]):
					callbackMatch= False

			wipeCB= False
			if callbackMatch:
				if callable(cCB['cb']):
					logging.info('Callback')
					wipeCB= cCB['cb'](_res)
			
			if not wipeCB:
				unusedCBA.append(cCB)

		return unusedCBA





class JSONStream():
	jsonTest= re.compile('Extra data: line \d+ column \d+ - line \d+ column \d+ \(char (?P<char>\d+) - \d+\)')

	jsonStr= ''


	def __init__(self):
		self.jsonStr= ''



	def find(self, _in=''):
		self.jsonStr+= _in
		
		jsonA, jsonDone= self.jsonRestore()

		self.jsonStr= self.jsonStr[jsonDone:]

		return jsonA



	'''
	Detect json-restored values from string containing several json-encoded blocks.

	Return array of detected json found.
	'''
	def jsonRestore(self):
		jsonDone= 0
		jsonFound= []

		while True:
			#try full, then try part
			try:
				jsonTry= json.loads(self.jsonStr[jsonDone:])
				jsonFound.append(jsonTry)	#rest
				
				return jsonFound, len(self.jsonStr)	#json ended up

			except Exception as exc:
				jsonErr= self.jsonTest.match(str(exc))
				if not jsonErr:	#assumed unfinished json
					return jsonFound, jsonDone

				jsonLen= int(jsonErr.group('char'))
				jsonFound.append( json.loads(self.jsonStr[jsonDone:jsonDone+jsonLen]) )

				jsonDone+= jsonLen

