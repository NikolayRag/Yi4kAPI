import logging

import socket, json

from .yiAPICommand import *
from .yiAPIListener import *








class YiAPI():
	#private commands
	startSession= YiAPICommandGen(257)
	stopSession= YiAPICommandGen(258)


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
				self.sock= socket.create_connection((self.ip,7878),1)
				break
			except:
				None

		if not self.sock:
			logging.critical('Not connected')
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
			logging.error('Camera disconnected')
			return -99999



		runCmd= _command.apply({'token':self.sessionId, 'heartbeat':self.tick}, _val)

		self.listener.assign(runCmd.cmdSend['msg_id'], runCmd.blockingCB)
		
		self.cmdSend(runCmd.cmdSend)

#		if not cbEvent:	#external callback supplied, exit at once
#			return

		#blocked branch from here

		runCmd.blockingEvent.wait()
		res= runCmd.res
		logging.debug('Result %s' % res)

		if res['rval']:
			logging.warning('Camera error %d' % res['rval'])
			return res['rval']

#		if callable(runCmd.resultCB):
#			return runCmd.resultCB(res)

		if 'param' in res:
			return res['param']



	'''
	Sent YiAPICommandGen co camera.
	'''
	def cmdSend(self, _cmdDict):
		logging.debug("Send %s" % _cmdDict)
		
		self.sock.sendall( bytes(json.dumps(_cmdDict),'ascii') )

		self.tick+= 1
