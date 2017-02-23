import logging
import re, json, threading


'''
Constantly listen to opened Yi4k camera for sultable response.
Most of response will be the result of commands sent to camera, while some of the responce
is camera state, pushed periodically.
'''

class YiAPIListener(threading.Thread):
	jsonTest= re.compile('Extra data: line \d+ column \d+ - line \d+ column \d+ \(char (?P<char>\d+) - \d+\)')

	inputBuffer= ''
	assignedCB= {}	#msgId:cb collection
	constantCB= {}


	def __init__(self, _sock):
		threading.Thread.__init__(self)

		self.sock= _sock
		self.inputBuffer= ''
		self.assignedCB= {}
		self.constantCB= {}

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
			self.inputBuffer+= (recv.decode())


			responseA, jsonDone= self.jsonRestore(self.inputBuffer)
			self.inputBuffer= self.inputBuffer[jsonDone:]


			for resJSON in responseA:
				logging.info('Listen: res= %s' % str(resJSON))
				logging.info('Res %s' % str(resJSON))
				
				cId= resJSON['msg_id']
				cbA= self.assignedCB

				if (cId in cbA) and callable(cbA[cId]):
					logging.info('Callback')

					cbA[cId](resJSON)
					del cbA[cId]


				cbA= self.constantCB

				if (cId in cbA) and callable(cbA[cId]):
					logging.info('Callback static')
					cbA[cId](resJSON)



	'''
	Assign callback for awaited command responce.
	'''
	def assign(self, _msgId, _cb):
		self.assignedCB[_msgId]= _cb








#########
#PRIVATE#
#########


	'''
	Detect json-restored values from string containing several json-encoded blocks.

	Return array of detected json found.
	'''
	def jsonRestore(self, _jsonStr):
		jsonDone= 0
		responseA= []

		while True:
			#try full, then try part
			try:
				jsonTry= json.loads(_jsonStr[jsonDone:])
				responseA.append(jsonTry)	#rest
				
				return responseA, len(_jsonStr)	#json ended up

			except Exception as exc:
				jsonErr= self.jsonTest.match(str(exc))
				if not jsonErr:	#assumed unfinished json
					return responseA, jsonDone

				jsonLen= int(jsonErr.group('char'))
				responseA.append( json.loads(_jsonStr[jsonDone:jsonDone+jsonLen]) )

				jsonDone+= jsonLen

