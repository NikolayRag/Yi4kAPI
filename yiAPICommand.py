import logging


'''
Public available commands.
'''
commands= []


'''
Class usable to pass to YiAPI.cmd()
.makeCmd() is called then to generate runtime command object.

	params
		dict of non-changing parameters.

	variable
		name or list of names to be assigned later with apply()
'''
class YiAPICommandGen():
	resultReq= None
	resultCB= None

	commandName= ''
	params= None

	variable= None
	values= None	#available values list to assign to .variable. Logging use only.


	def __init__(self,
		_id,
		commandName='',
		values=None,
		params=None,
		variable=[],
		resultReq=None,
		resultCB=None
	):
		self.resultReq= resultReq
		self.resultCB= resultCB

		self.params= {'msg_id':int(_id)}
		if params:
			self.params.update(params)

		if not isinstance(variable, list) and not isinstance(variable, tuple):
			variable= [variable]

		self.variable= variable


		if values:
			self.values= values


		if commandName:
			self.commandName= commandName
			commands.append(self)



	'''
	Create object representing command at runtime.
	Append stored params to provided dict and apply _val to stored .variable respectively

	Return YiAPICommand.
	'''
	def makeCmd(self, _cmdPrep, _val=None):
		_cmdPrep.update(self.params)


		#assign provided _val[] values to stored .variable[] parameters
		if not isinstance(_val, list) and not isinstance(_val, tuple):
			_val= [_val]

		for pair in zip(self.variable,_val):
			_cmdPrep[pair[0]]= pair[1]


		return YiAPICommand(_cmdPrep, self.resultReq, self.resultCB)



	'''
	return response templates required for command to finish
	'''
	def cbTemplates(self):
		defaultTmpl= [{'msg_id': self.params['msg_id']}]

		if self.resultReq:
			defaultTmpl.append(self.resultReq)

		return defaultTmpl




import threading

'''
Runtime command class. Lives from command send to command response.
'''
class YiAPICommand():
	cmdSend= None
	resultReq= None
	resultCB= None
	blockingCnt= 1
	blockingCB= None
	blockingEvent= None

	resultDict= None

	def __init__(self, _cmdSend, _resultReq, _resultCB):
		self.cmdSend= _cmdSend
		self.resultDict= {}
		self.resultReq= _resultReq
		self.resultCB= _resultCB

		if _resultReq:
			self.blockingCnt= 2

		self.blockingCB, self.blockingEvent = self.blockingCBGen()



	def result(self):
		if self.resultDict['rval']:
			logging.warning('Camera error %d' % self.resultDict['rval'])
			return self.resultDict['rval']

		if callable(self.resultCB):
			return self.resultCB(self.resultDict)

		if 'param' in self.resultDict:
			return self.resultDict['param']


	'''
	Generate callback suitable for supplying to YiAPIListener.assing()
	and Event fired at callback call.
	'''
	def blockingCBGen(self):
		cbEvent= threading.Event()
		
		def func(_res):
			self.resultDict.update(_res)


			self.blockingCnt-= 1
			if ('rval' in _res) and (_res['rval']):
				self.blockingCnt= 0

			if not self.blockingCnt:
				cbEvent.set()
				return True

		return (func, cbEvent)

