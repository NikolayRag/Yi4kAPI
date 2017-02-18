import socket, json, time, re, os

from .yiAPICommand import *
from .yiAPIListener import *


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







class YiAPI():
	#private commands
	startSession= YiAPICommand(257)
	stopSession= YiAPICommand(258)


	ip= '192.168.42.1'
	sock= None
	tick= 0
	sessionId= 0

	listener= None
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


		self.listener= YiAPIListener(self.sock)

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
	if _vals provided, it's a value assigned to YiAPICommand.values respectively. 
	'''
	def cmd(self, _command, _val=None):
		if not self.sock:
			kiLog.err('Camera disconnected')
			return -99999


		self.cmdSend(_command, _val)
		self.res= self.listener.cmdRecv()
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
