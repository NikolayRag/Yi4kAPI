import socket, json, time, re, os

try:
	from kiLog import *
except:
	class kiLog():
		@staticmethod
		def err(v):
			None
		@staticmethod
		def warn(v):
			None
		@staticmethod
		def ok(v):
			None
		@staticmethod
		def vers(v):
			None



'''
Public available commands.
'''
commands= []


'''
Class usable to pass to YiAPI.cmd()

	params
		dict of non-changing parameters.

	variable
		name or list of names to be assigned later with apply()
'''
class YiAPICommand():
	resultCB= None

	commandName= ''
	params= None
	variable= None

	values= None


	def __init__(self, _id, _commandName='', values=None, params=None, variable=[], resultCB=None):
		self.resultCB= resultCB

		self.params= {'msg_id':int(_id)}
		if params:
			self.params.update(params)

		if not isinstance(variable, list) and not isinstance(variable, tuple):
			variable= [variable]

		self.variable= variable


		if values:
			self.values= values


		if _commandName:
			self.commandName= _commandName
			commands.append(self)



	'''
	Collect dict to be send to camera.
	Append stored params to provided dict and apply _val to stored .variable respectively

	Return complete suitable dict.
	'''
	def apply(self, _dict, _val=None):
		_dict.update(self.params)


		#assign provided _val[] values to stored .variable[] parameters
		if not isinstance(_val, list) and not isinstance(_val, tuple):
			_val= [_val]

		for pair in zip(self.variable,_val):
			_dict[pair[0]]= pair[1]


		return _dict




class YiAPI():
	#private commands
	startSession= YiAPICommand(257)
	stopSession= YiAPICommand(258)


	jsonTest= re.compile('Extra data: line \d+ column \d+ - line \d+ column \d+ \(char (?P<char>\d+) - \d+\)')

	ip= '192.168.42.1'
	sock= None
	tick= 0
	sessionId= 0

	res= []



	@staticmethod
	def defaults(ip):
		if ip:
			YiAPI.ip= ip



	def __init__(self, _ip=None):
		if _ip:
			self.ip= _ip

		#sometimes camera couldnt be connected after a pause. Ping somehow helps to wake it.
		for i in [0,1]:
			os.system("ping -n 1 %s>nul" % self.ip)

		try:
			self.sock= socket.create_connection((self.ip,7878),3)
		except:
			self.res= False
			return

		res= self.cmd(self.startSession)
		if res<0:
			self.sock= None
			self.res= False
		else:
			self.sessionId= res


	#shoud be called at very end to tell camera it's released
	def close(self):
		self.cmd(self.stopSession)

		self.sock= None



	'''
	Run predefined _command.
	if _vals provided, it's a value assigned to YiAPICommand.vals respectively. 
	'''
	def cmd(self, _command, _val=None):
		if not self.sock:
			kiLog.err('Camera disconnected')
			return -99999


		self.cmdSend(_command, _val)
		self.res= self.jsonRestore( self.cmdRecv() )
		if not self.res:
			kiLog.err('Invalid response')
			return -99998


		res= {'rval':0}
		if len(self.res):
			for res in self.res:	#find block with rval
				if 'rval' in res:
					break


		if 'rval' in res and res['rval']:
			kiLog.err('Camera error: %d' % res['rval'])
			kiLog.verb('Full result: %s' % str(self.res))
			return res['rval']

		if callable(_command.resultCB):
			return _command.resultCB(res)

		if 'param' in res:
			return res['param']



	'''
	Sent _command co camera.
	'''
	def cmdSend(self, _command, _val=None):
		out= _command.apply({'token':self.sessionId, 'heartbeat':self.tick}, _val)

		kiLog.verb("Send: %s" % out)
		
		self.sock.sendall( bytes(json.dumps(out),'ascii') )

		self.tick+= 1



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

		return res.decode()



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
