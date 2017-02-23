'''
Modify logging output by adding class name
'''
import logging, inspect
logging.basicConfig(level= logging.DEBUG, format= '%(name)s %(levelname)s: %(message)s')

def kiLog(_name, _level, _fn, _ln, _msg, _args, _exInfo, _func, _stack):
	stack= inspect.stack()
	callObj= stack[5][0].f_locals
	_name= (
		('self' in callObj)
	 	and hasattr(callObj['self'],'__class__')
	 	and callObj['self'].__class__.__name__
	 	or ''
 	)

	return logging.LogRecord(_name, _level, _fn, _ln, _msg, _args, _exInfo)

logging.setLogRecordFactory(kiLog)
