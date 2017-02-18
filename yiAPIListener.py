'''
Constantly listen to opened Yi4k camera for sultable response.
Most of response will be the result of commands sent to camera, while some of the responce
is camera state, pushed periodically.
'''

class YiAPIListener():
	jsonTest= re.compile('Extra data: line \d+ column \d+ - line \d+ column \d+ \(char (?P<char>\d+) - \d+\)')


	def __init__(self, _sock):
		self.sock= _sock


	'''
	Recieve string from socket till its dry.
	'''
	def cmdRecv(self):
		self.sock.settimeout(2)	#wait for a while for camera to execute command
		res= b''

		while True:
			try:
				recv= self.sock.recv(4096)
				res+= recv

				kiLog.verb("part: %s" % recv)

				self.sock.settimeout(.1) #wait a little for detect end-of-data
			except:
				break

		kiLog.verb("Recieved: %d bytes" % len(res))

		return self.jsonRestore( res.decode() )



	'''
	Form array of json-restored values from string containing several json-encoded blocks
	'''
	def jsonRestore(self, _json):
		jsonA= []

		jsonFrom= 0
		while True:
			try:
				jsonTry= json.loads(_json[jsonFrom:])
				jsonA.append(jsonTry)	#rest
				break	#json ended up
			except Exception as exc:
				kiLog.verb('Json result: ' +str(exc))
				
				jsonErr= self.jsonTest.match(str(exc))
				if not jsonErr:
					return False

				jsonFrom2= int(jsonErr.group('char'))
				jsonA.append( json.loads(_json[jsonFrom:jsonFrom+jsonFrom2]) )

				jsonFrom+= jsonFrom2


		return(jsonA)
