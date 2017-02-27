import kilog
kilog.names(('',))



import sys, os
sys.path.append(os.path.abspath('../..'))

from Yi4kAPI import *



import time

a= YiAPI()
logging.info('Started: %s' % str(bool(a)))
res= a.cmd(getSettings)
logging.info('getSettings: %s' % str(res))
res= a.cmd(stopRecording)
logging.info('(err:stopped) stopRecording: %s' % str(res))
time.sleep(4)
logging.info('=============')
print('')


resEv= a.cmd(getVideoExposureValue)
logging.info('getVideoExposureValue: %s' % str(resEv))
res= a.cmd(setVideoExposureValue, '+1.5')
logging.info('setVideoExposureValue: %s' % str(res))
res= a.cmd(startRecording)
logging.info('startRecording: %s' % str(res))

time.sleep(4)
logging.info('Video')

res= a.cmd(stopRecording)
logging.info('stopRecording: %s' % str(res))
res= a.cmd(setVideoExposureValue, resEv)
logging.info('setVideoExposureValue: %s' % str(res))
time.sleep(4)
logging.info('=============')
print('')

res= a.cmd(capturePhoto)
logging.info('(err:mode) capturePhoto: %s' % str(res))
res= a.cmd(capturePhoto)
logging.info('capturePhoto: %s' % str(res))
res= a.cmd(capturePhoto)
logging.info('capturePhoto: %s' % str(res))
time.sleep(4)
logging.info('=============')
print('')

#+
res= a.cmd(getFileList)
logging.info('getFileList: %s' % str(res))
res= a.cmd(capturePhoto)
logging.info('capturePhoto: %s' % str(res))
time.sleep(4)
logging.info('=============')
print('')

#+
res= a.cmd(startViewFinder)
logging.info('startViewFinder: %s' % str(res))
res= a.cmd(stopViewFinder)
logging.info('stopViewFinder: %s' % str(res))
res= a.cmd(capturePhoto)
logging.info('capturePhoto: %s' % str(res))
time.sleep(4)
logging.info('=============')
print('')

#+
res= a.cmd(setDateTime, '2017-02-24 00:25:01')
logging.info('setDateTime: %s' % str(res))
res= a.cmd(capturePhoto)
logging.info('capturePhoto: %s' % str(res))
time.sleep(4)
logging.info('=============')
print('')

#+
res= a.cmd(setSystemMode, "record")
logging.info('setSystemMode: %s' % str(res))
res= a.cmd(capturePhoto)
logging.info('capturePhoto: %s' % str(res))
time.sleep(4)
logging.info('=============')
print('')

res= a.cmd(setRecordMode, "record")
logging.info('setRecordMode: %s' % str(res))
res= a.cmd(capturePhoto)
logging.info('(err:mode) capturePhoto: %s' % str(res))
time.sleep(4)
logging.info('=============')
print('')

res= a.cmd(setRecordMode, "record")
logging.info('setRecordMode: %s' % str(res))
res= a.cmd(setCaptureMode, "precise quality")
logging.info('setCaptureMode: %s' % str(res))
res= a.cmd(capturePhoto)
logging.info('capturePhoto: %s' % str(res))
time.sleep(4)
logging.info('=============')
print('')

res= a.cmd(setRecordMode, "record_loop")
logging.info('setRecordMode: %s' % str(res))

res= a.close()
logging.info('Stop state: %s' % str(res))
