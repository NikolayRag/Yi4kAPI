import kilog

import sys, os
sys.path.append(os.path.abspath('../..'))

from Yi4kAPI import *



import time

a= YiAPI()
logging.critical('Started: %s' % str(bool(a)))
res= a.cmd(getSettings)
logging.critical('getSettings: %s' % str(res))
time.sleep(4)
logging.critical('')


resEv= a.cmd(getVideoExposureValue)
logging.critical('getVideoExposureValue: %s' % str(resEv))
res= a.cmd(setVideoExposureValue, '+1.5')
logging.critical('setVideoExposureValue: %s' % str(res))
res= a.cmd(startRecording)
logging.critical('startRecording: %s' % str(res))

time.sleep(4)
logging.critical('Video')

res= a.cmd(stopRecording)
logging.critical('stopRecording: %s' % str(res))
res= a.cmd(setVideoExposureValue, '+1.0')
logging.critical('setVideoExposureValue: %s' % str(res))
time.sleep(4)
logging.critical('')

res= a.cmd(capturePhoto)
logging.critical('capturePhoto: %s' % str(res))
res= a.cmd(capturePhoto)
logging.critical('capturePhoto: %s' % str(res))
res= a.cmd(capturePhoto)
logging.critical('capturePhoto: %s' % str(res))
time.sleep(4)
logging.critical('')

#+
res= a.cmd(getFileList)
logging.critical('getFileList: %s' % str(res))
res= a.cmd(capturePhoto)
logging.critical('capturePhoto: %s' % str(res))
time.sleep(4)
logging.critical('')

#+
res= a.cmd(startViewFinder)
logging.critical('startViewFinder: %s' % str(res))
res= a.cmd(stopViewFinder)
logging.critical('stopViewFinder: %s' % str(res))
res= a.cmd(capturePhoto)
logging.critical('capturePhoto: %s' % str(res))
time.sleep(4)
logging.critical('')

#+
res= a.cmd(setDateTime, '2017-02-24 00:25:01')
logging.critical('setDateTime: %s' % str(res))
res= a.cmd(capturePhoto)
logging.critical('capturePhoto: %s' % str(res))
time.sleep(4)
logging.critical('')

#+
res= a.cmd(setSystemMode, "record")
logging.critical('setSystemMode: %s' % str(res))
res= a.cmd(capturePhoto)
logging.critical('capturePhoto: %s' % str(res))
time.sleep(4)
logging.critical('')

res= a.cmd(setRecordMode, "record")
logging.critical('setRecordMode: %s' % str(res))
res= a.cmd(capturePhoto)
logging.critical('capturePhoto: %s' % str(res))
time.sleep(4)
logging.critical('')

res= a.cmd(setRecordMode, "record")
logging.critical('setRecordMode: %s' % str(res))
res= a.cmd(setCaptureMode, "precise quality")
logging.critical('setCaptureMode: %s' % str(res))
res= a.cmd(capturePhoto)
logging.critical('capturePhoto: %s' % str(res))
time.sleep(4)
logging.critical('')

res= a.cmd(setRecordMode, "record_loop")
logging.critical('setRecordMode: %s' % str(res))

res= a.close()
logging.critical('Stop state: %s' % str(res))
