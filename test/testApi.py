import kilog
kilog.names(('',))

'''
Bunch of Yi commands to test.
'''


import sys, os
sys.path.append(os.path.abspath('../..'))

from Yi4kAPI import *



import time


def vid_ok(_res):
	print('Video recorded:', _res['param'], _res['msize'], 'bytes')

def set_ok(_res):
	print('Setting changed')

a= YiAPI()
a.setCB('video_record_complete', vid_ok)
a.setCB('setting_changed', set_ok)

print('Started: %s' % str(bool(a)))
res= a.cmd(getSettings)
print('getSettings: %s' % str(res))
res= a.cmd(stopRecording)
print('(err:stopped) stopRecording: %s' % str(res))
time.sleep(40)
print('=============Paused to test manual recording tart/stop and shange settings')
print('')


resEv= a.cmd(getVideoExposureValue)
print('getVideoExposureValue: %s' % str(resEv))
res= a.cmd(setVideoExposureValue, '+1.5')
print('setVideoExposureValue: %s' % str(res))
res= a.cmd(startRecording)
print('startRecording: %s' % str(res))

time.sleep(4)
print('Video')

res= a.cmd(stopRecording)
print('stopRecording: %s' % str(res))
res= a.cmd(setVideoExposureValue, resEv)
print('setVideoExposureValue: %s' % str(res))
time.sleep(4)
print('=============')
print('')

res= a.cmd(capturePhoto)
print('(err:mode) capturePhoto: %s' % str(res))
res= a.cmd(capturePhoto)
print('capturePhoto: %s' % str(res))
res= a.cmd(capturePhoto)
print('capturePhoto: %s' % str(res))
time.sleep(4)
print('=============')
print('')

#+
res= a.cmd(getFileList)
print('getFileList: %s' % str(res))
res= a.cmd(capturePhoto)
print('capturePhoto: %s' % str(res))
time.sleep(4)
print('=============')
print('')

#+
res= a.cmd(startViewFinder)
print('startViewFinder: %s' % str(res))
res= a.cmd(stopViewFinder)
print('stopViewFinder: %s' % str(res))
res= a.cmd(capturePhoto)
print('capturePhoto: %s' % str(res))
time.sleep(4)
print('=============')
print('')

#+
res= a.cmd(setDateTime, '2017-02-24 00:25:01')
print('setDateTime: %s' % str(res))
res= a.cmd(capturePhoto)
print('capturePhoto: %s' % str(res))
time.sleep(4)
print('=============')
print('')

#+
res= a.cmd(setSystemMode, "record")
print('setSystemMode: %s' % str(res))
res= a.cmd(capturePhoto)
print('capturePhoto: %s' % str(res))
time.sleep(4)
print('=============')
print('')

res= a.cmd(setRecordMode, "record")
print('setRecordMode: %s' % str(res))
res= a.cmd(capturePhoto)
print('(err:mode) capturePhoto: %s' % str(res))
time.sleep(4)
print('=============')
print('')

res= a.cmd(setRecordMode, "record")
print('setRecordMode: %s' % str(res))
res= a.cmd(setCaptureMode, "precise quality")
print('setCaptureMode: %s' % str(res))
res= a.cmd(capturePhoto)
print('capturePhoto: %s' % str(res))
time.sleep(4)
print('=============')
print('')

res= a.cmd(setRecordMode, "record_loop")
print('setRecordMode: %s' % str(res))

res= a.close()
print('Stop state: %s' % str(res))
