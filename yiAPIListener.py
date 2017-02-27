import logging
import re, json, threading


'''
Constantly listen to opened Yi4k camera for sultable response.
Most of response will be the result of commands sent to camera, while some of the responce
is camera state, pushed periodically.
'''

class YiAPIListener(threading.Thread):
	commandsCB= []	#runtime commands listening
	constantCB= {}

	jsonStream= None

	def __init__(self, _sock):
		threading.Thread.__init__(self)

		self.sock= _sock
		self.commandsCB= []
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


				self.commandsCB= self.applyCB(self.commandsCB, resJSON)

				self.applyCB(self.constantCB, resJSON)



	'''
	Assign one-time callback for awaited command responce.
	'''
	def instantCB(self, _command):
		self.commandsCB.append(_command)




	'''
	Rolling over assigned callbacks, call them if all of template values exists in response.
	Then wipe callback out.
	'''
	def applyCB(self, _commandsA, _res):
		unusedCBA= []

		for cCommand in _commandsA:
			wipeCB= False
			if cCommand.cbMatch(_res):
				if callable(cCommand.blockingCB):
					logging.info('Callback')
					wipeCB= cCommand.blockingCB(_res)
			
			if not wipeCB:
				unusedCBA.append(cCommand)

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

