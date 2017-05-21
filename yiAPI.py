import logging

import socket, json, threading

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

	commandTimeout= 10
	connectionTimeout= .5
	connectionTries= 10

	listener= None



	@staticmethod
	def defaults(ip):
		if ip:
			YiAPI.ip= ip



	def __init__(self, _ip=None):
		if _ip:
			self.ip= _ip

		#sometimes camera couldnt be connected after a pause. Try to connect several times.
		for i in range(0,self.connectionTries):
			try:
				self.sock= socket.create_connection((self.ip,7878),self.connectionTimeout)
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
	def cmd(self, _command, _val=None):
		if not self.sock:
			logging.error('Camera disconnected')
			return -99999


		runCmd= _command.makeCmd({'token':self.sessionId, 'heartbeat':self.tick}, _val)
		self.listener.instantCB(runCmd)
		
		timeoutCmd= threading.Timer(self.commandTimeout, runCmd.blockingEvent.set)
		timeoutCmd.start()

		if not self.cmdSend(runCmd.cmdSend):
			logging.critical('Socket error while sending')

			runCmd.blockingEvent.set()
			self.sock= None

		runCmd.blockingEvent.wait()
		timeoutCmd.cancel()

		logging.debug('Result %s' % runCmd.resultDict)

		return runCmd.result()



	'''
	Sent YiAPICommandGen co camera.
	'''
	def cmdSend(self, _cmdDict):
		logging.debug("Send %s" % _cmdDict)
		
		try:
			self.sock.sendall( bytes(json.dumps(_cmdDict),'ascii') )
		except:
			return

		self.tick+= 1
		return True



	def setCB(self, _type=None, _cb=None):
		if not self.listener:
			return

		return self.listener.setCB(_type, _cb)
