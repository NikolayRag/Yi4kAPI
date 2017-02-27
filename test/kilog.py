'''
Modify logging output by adding class name
'''
import logging, inspect


DEBUG= logging.DEBUG
INFO= logging.INFO
WARNING= logging.WARNING
ERROR= logging.ERROR
CRITICAL= logging.CRITICAL


namesAllowed= {}

def hook(_name, _level, _fn, _ln, _msg, _args, _exInfo, _func, _stack):
	stack= inspect.stack()
	callObj= stack[5][0].f_locals #skip stack to first 'outer' level
	_name= (
		('self' in callObj)
	 	and hasattr(callObj['self'],'__class__')
	 	and callObj['self'].__class__.__name__
	 	or ''
 	)

	if len(namesAllowed):
		if not (_name in namesAllowed):
			_level= -1

	return logging.LogRecord(_name, _level, _fn, _ln, _msg, _args, _exInfo)

logging.setLogRecordFactory(hook)



def names(_names, _state=True):
	for name in _names:
		if _state:
			namesAllowed[name]= True
			continue

		if name in namesAllowed:
			del namesAllowed[name]
			

def config(level= WARNING):
	logging.basicConfig(level= level, format= '%(name)s %(levelname)s: %(message)s')

config(DEBUG)
