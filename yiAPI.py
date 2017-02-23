import socket, json, threading

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
		def verb(v):
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



	@staticmethod
	def defaults(ip):
		if ip:
			YiAPI.ip= ip



	def __init__(self, _ip=None):
		if _ip:
			self.ip= _ip

		#sometimes camera couldnt be connected after a pause. Try to connect several times.
		for i in range(0,5):
			try:
				self.sock= socket.create_connection((self.ip,7878),.5)
				break
			except:
				None

		if not self.sock:
			print('Not connected')
			return


		self.sock.settimeout(None)
		self.listener= YiAPIListener(self.sock)

		res= self.cmd(self.startSession)
		if res<0:
			self.sock= None
		else:
			self.sessionId= res


	#shoud be called at very end to tell camera it's released
	def close(self):
		self.cmd(self.stopSession)

		if self.sock:
			self.sock.close()
		self.sock= None



	'''
	Run predefined _command.
	if _vals provided, it's a value assigned to YiAPICommand.values respectively. 
	'''
	def cmd(self, _command, _val=None, cb=None):
		if not self.sock:
			kiLog.err('Camera disconnected')
			return -99999


		cbEvent= None
		if not cb:
			cb, cbEvent= self.blockingCB()

		self.listener.assign(_command.params['msg_id'], cb)
		
		self.cmdSend(_command, _val)
		self.tick+= 1

		if not cbEvent:	#external callback supplied, exit at once
			return

		#

		cbEvent.wait()
		res= cbEvent.res 	#bound by generated cb, see blockingCB()
		print('res', res)

		if res['rval']:
			kiLog.err('Camera error: %d' % res['rval'])
			kiLog.verb('Full result: %s' % str(res))
			return res['rval']

#		if callable(_command.resultCB):
#			return _command.resultCB(res)

		if 'param' in res:
			return res['param']



	'''
	Sent _command co camera.
	'''
	def cmdSend(self, _command, _val=None):
		out= _command.apply({'token':self.sessionId, 'heartbeat':self.tick}, _val)

		kiLog.verb("Send: %s" % out)
		
		self.sock.sendall( bytes(json.dumps(out),'ascii') )



	'''
	Generate callback suitable for supplying to YiAPIListener.assing()
	and Event fired at callback call.
	'''
	def blockingCB(self):
		cbEvent= threading.Event()
		cbEvent.res= False
		
		def func(_res):
			cbEvent.res= _res
			cbEvent.set()

		return (func, cbEvent)

