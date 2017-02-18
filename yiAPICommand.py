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

