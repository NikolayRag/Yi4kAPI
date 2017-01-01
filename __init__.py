from .yiClasses import *


'''
Define public commands
'''

startRecording=		YiAPICommand(513, 'startRecording')
stopRecording=		YiAPICommand(514, 'stopRecording')
capturePhoto=		YiAPICommand(16777220, 'capturePhoto',
	params={'param':'precise quality;off'}
)
getFileList=		YiAPICommand(1282, 'getFileList',
	params={'param':'/tmp/fuse_d'},
	resultCB= lambda res: res['listing']
)
#	deleteFile=		YiAPICommand(1281, 'deleteFile', {}, {'param': '/tmp/fuse_d/DCIM'}, resultCB= lambda res: res['listing'])
startViewFinder=		YiAPICommand(259, 'startViewFinder')
stopViewFinder=		YiAPICommand(260, 'stopViewFinder')


getSettings=		YiAPICommand(3,	'getSettings',
	resultCB=lambda res:{key:val for d in res['param'] for key,val in d.items()}
)
#"yyyy-MM-dd HH:mm:ss"
setDateTime=		YiAPICommand(2,	'setDateTime',
	params= {'type':'camera_clock'},
	variable= 'param'
)
#
setSystemMode=		YiAPICommand(2,	'setSystemMode',
	values= ["capture", "record"],
	params= {'type':'system_mode'},
	variable= 'param'
)
#
getVideoResolution=		YiAPICommand(1, 'getVideoResolution',
	params={'type':'video_resolution'}
)
setVideoResolution=		YiAPICommand(2,	'setVideoResolution',
	values= ["3840x2160 30P 16:9", "3840x2160 30P 16:9 super", "2560x1920 30P 4:3", "1920x1440 60P 4:3", "1920x1440 30P 4:3", "1920x1080 120P 16:9", "1920x1080 120P 16:9 super", "1920x1080 60P 16:9", "1920x1080 60P 16:9 super", "1920x1080 30P 16:9", "1920x1080 30P 16:9 super", "1280x960 120P 4:3", "1280x960 60P 4:3", "1280x720 240P 16:9", "1280x720 120P 16:9 super", "1280x720 60P 16:9 super", "840x480 240P 16:9"],
	params= {'type':'video_resolution'},
	variable= 'param'
)
#
getPhotoResolution=		YiAPICommand(1, 'getPhotoResolution',
	params={'type':'photo_size'}
)
setPhotoResolution=		YiAPICommand(2,	'setPhotoResolution',
	values= ["12MP (4000x3000 4:3) fov:w", "7MP (3008x2256 4:3) fov:w", "7MP (3008x2256 4:3) fov:m", "5MP (2560x1920 4:3) fov:m", "8MP (3840x2160 16:9) fov:w"],
	params= {'type':'photo_size'},
	variable= 'param'
)
#
getPhotoWhiteBalance=		YiAPICommand(1, 'getPhotoWhiteBalance',
	params={'type':'iq_photo_wb'}
)
setPhotoWhiteBalance=		YiAPICommand(2,	'setPhotoWhiteBalance',
	values= ["auto", "native", "3000k", "5500k", "6500k"],
	params= {'type':'iq_photo_wb'},
	variable= 'param'
)
#
getVideoWhiteBalance=		YiAPICommand(1, 'getVideoWhiteBalance',
	params={'type':'iq_video_wb'}
)
setVideoWhiteBalance=		YiAPICommand(2,	'setVideoWhiteBalance',
	values= ["auto", "native", "3000k", "5500k", "6500k"],
	params= {'type':'iq_video_wb'},
	variable= 'param'
)
#
getPhotoISO=		YiAPICommand(1, 'getPhotoISO',
	params={'type':'iq_photo_iso'}
)
setPhotoISO=		YiAPICommand(2,	'setPhotoISO',
	values= ["auto", "100", "200", "400", "800", "1600", "6400"],
	params= {'type':'iq_photo_iso'},
	variable= 'param'
)
#
getVideoISO=		YiAPICommand(1, 'getVideoISO',
	params={'type':'iq_video_iso'}
)
setVideoISO=		YiAPICommand(2,	'setVideoISO',
	values= ["auto", "100", "200", "400", "800", "1600", "6400"],
	params= {'type':'iq_video_iso'},
	variable= 'param'
)
#
getPhotoExposureValue=		YiAPICommand(1, 'getPhotoExposureValue',
	params={'type':'iq_photo_ev'}
)
setPhotoExposureValue=		YiAPICommand(2,	'setPhotoExposureValue',
	values= ["-2.0", "-1.5", "-1.0", "-0.5", "0", "+0.5", "+1.0", "+1.5", "+2.0"],
	params= {'type':'iq_photo_ev'},
	variable= 'param'
)
#
getVideoExposureValue=		YiAPICommand(1, 'getVideoExposureValue',
	params={'type':'iq_video_ev'}
)
setVideoExposureValue=		YiAPICommand(2,	'setVideoExposureValue',
	values= ["-2.0", "-1.5", "-1.0", "-0.5", "0", "+0.5", "+1.0", "+1.5", "+2.0"],
	params= {'type':'iq_video_ev'},
	variable= 'param'
)
#
getPhotoShutterTime=		YiAPICommand(1, 'getPhotoShutterTime',
	params={'type':'iq_photo_shutter'}
)
setPhotoShutterTime=		YiAPICommand(2,	'setPhotoShutterTime',
	values= ["auto", "2s", "5s", "10s", "20s", "30s"],
	params= {'type':'iq_photo_shutter'},
	variable= 'param'
)
#
getVideoSharpness=		YiAPICommand(1, 'getVideoSharpness',
	params={'type':'video_sharpness'}
)
setVideoSharpness=		YiAPICommand(2,	'setVideoSharpness',
	values= ["low", "medium", "high"],
	params= {'type':'video_sharpness'},
	variable= 'param'
)
#
getPhotoSharpness=		YiAPICommand(1, 'getPhotoSharpness',
	params={'type':'photo_sharpness'}
)
setPhotoSharpness=		YiAPICommand(2,	'setPhotoSharpness',
	values= ["low", "medium", "high"],
	params= {'type':'photo_sharpness'},
	variable= 'param'
)
#
getVideoFieldOfView=		YiAPICommand(1, 'getVideoFieldOfView',
	params={'type':'fov'}
)
setVideoFieldOfView=		YiAPICommand(2,	'setVideoFieldOfView',
	values= ["wide", "medium", "narrow"],
	params= {'type':'fov'},
	variable= 'param'
)
#
getRecordMode=		YiAPICommand(1, 'getRecordMode',
	params={'type':'rec_mode'}
)
setRecordMode=		YiAPICommand(2,	'setRecordMode',
	values= ["record", "record_timelapse", "record_slow_motion", "record_loop", "record_photo"],
	params= {'type':'rec_mode'},
	variable= 'param'
)
#
getCaptureMode=		YiAPICommand(1, 'getCaptureMode',
	params={'type':'capture_mode'}
)
setCaptureMode=		YiAPICommand(2,	'setCaptureMode',
	["precise quality", "precise self quality", "burst quality", "precise quality cont."],
	{'type':'capture_mode'},
	variable= 'param'
)
#
getMeteringMode=		YiAPICommand(1, 'getMeteringMode',
	params={'type':'meter_mode'}
)
setMeteringMode=		YiAPICommand(2,	'setMeteringMode',
	values= ["center", "average", "spot"],
	params= {'type':'meter_mode'},
	variable= 'param'
)
#
getVideoQuality=		YiAPICommand(1, 'getVideoQuality',
	params={'type':'video_quality'}
)
setVideoQuality=		YiAPICommand(2,	'setVideoQuality',
	values= ["S.Fine", "Fine", "Normal"],
	params= {'type':'video_quality'},
	variable= 'param'
)
#
getVideoColorMode=		YiAPICommand(1, 'getVideoColorMode',
	params={'type':'video_flat_color'}
)
setVideoColorMode=		YiAPICommand(2,	'setVideoColorMode',
	values= ["yi", "flat"],
	params= {'type':'video_flat_color'},
	variable= 'param'
)
#
getPhotoColorMode=		YiAPICommand(1, 'getPhotoColorMode',
	params={'type':'photo_flat_color'}
)
setPhotoColorMode=		YiAPICommand(2,	'setPhotoColorMode',
	values= ["yi", "flat"],
	params= {'type':'photo_flat_color'},
	variable= 'param'
)
#
getElectronicImageStabilizationState=		YiAPICommand(1, 'getElectronicImageStabilizationState',
	params={'type':'iq_eis_enable'}
)
setElectronicImageStabilizationState=		YiAPICommand(2,	'setElectronicImageStabilizationState',
	values= ["on", "off"],
	params= {'type':'iq_eis_enable'},
	variable= 'param'
)
#
getAdjustLensDistortionState=		YiAPICommand(1, 'getAdjustLensDistortionState',
	params={'type':'warp_enable'}
)
setAdjustLensDistortionState=		YiAPICommand(2,	'setAdjustLensDistortionState',
	values= ["on", "off"],
	params= {'type':'warp_enable'},
	variable= 'param'
)
#
getVideoMuteState=		YiAPICommand(1, 'getVideoMuteState',
	params={'type':'video_mute_set'}
)
setVideoMuteState=		YiAPICommand(2,	'setVideoMuteState',
	values= ["on", "off"],
	params= {'type':'video_mute_set'},
	variable= 'param'
)
#
getVideoTimestamp=		YiAPICommand(1, 'getVideoTimestamp',
	params={'type':'video_stamp'}
)
setVideoTimestamp=		YiAPICommand(2,	'setVideoTimestamp',
	values= ["off", "time", "date", "date/time"],
	params= {'type':'video_stamp'},
	variable= 'param'
)
#
getPhotoTimestamp=		YiAPICommand(1, 'getPhotoTimestamp',
	params={'type':'photo_stamp'}
)
setPhotoTimestamp=		YiAPICommand(2,	'setPhotoTimestamp',
	values= ["off", "time", "date", "date/time"],
	params= {'type':'photo_stamp'},
	variable= 'param'
)
#
getLEDMode=		YiAPICommand(1, 'getLEDMode',
	params={'type':'led_mode'}
)
setLEDMode=		YiAPICommand(2,	'setLEDMode',
	values= ["all enable", "all disable", "status enable"],
	params= {'type':'led_mode'},
	variable= 'param'
)
#
getVideoStandard=		YiAPICommand(1, 'getVideoStandard',
	params={'type':'video_standard'}
)
setVideoStandard=		YiAPICommand(2,	'setVideoStandard',
	values= ["PAL", "NTSC"],
	params= {'type':'video_standard'},
	variable= 'param'
)
#
getTimeLapseVideoInterval=		YiAPICommand(1, 'getTimeLapseVideoInterval',
	params={'type':'timelapse_video'}
)
setTimeLapseVideoInterval=		YiAPICommand(2,	'setTimeLapseVideoInterval',
	values= ["0.5", "1", "2", "5", "10", "30", "60"],
	params= {'type':'timelapse_video'},
	variable= 'param'
)
#
getTimeLapsePhotoInterval=		YiAPICommand(1, 'getTimeLapsePhotoInterval',
	params={'type':'precise_cont_time'}
)
setTimeLapsePhotoInterval=		YiAPICommand(2,	'setTimeLapsePhotoInterval',
	values= ["continue", "0.5 sec", "1.0 sec", "2.0 sec", "5.0 sec", "10.0 sec", "30.0 sec", "60.0 sec", "2.0 min", "5.0 min", "10.0 min", "30.0 min", "60.0 min"],
	params= {'type':'precise_cont_time'},
	variable= 'param'
)
#
getTimeLapseVideoDuration=		YiAPICommand(1, 'getTimeLapseVideoDuration',
	params={'type':'timelapse_video_duration'}
)
setTimeLapseVideoDuration=		YiAPICommand(2,	'setTimeLapseVideoDuration',
	values= ["off", "6s", "8s", "10s", "20s", "30s", "60s", "120s"],
	params= {'type':'timelapse_video_duration'},
	variable= 'param'
)
#
getScreenAutoLock=		YiAPICommand(1, 'getScreenAutoLock',
	params={'type':'screen_auto_lock'}
)
setScreenAutoLock=		YiAPICommand(2,	'setScreenAutoLock',
	values= ["never", "30s", "60s", "120s"],
	params= {'type':'screen_auto_lock'},
	variable= 'param'
)
#
getAutoPowerOff=		YiAPICommand(1, 'getAutoPowerOff',
	params={'type':'auto_power_off'}
)
setAutoPowerOff=		YiAPICommand(2,	'setAutoPowerOff',
	values= ["off", "3 minutes", "5 minutes", "10 minutes"],
	params= {'type':'auto_power_off'},
	variable= 'param'
)
#
getVideoRotateMode=		YiAPICommand(1, 'getVideoRotateMode',
	params={'type':'video_rotate'}
)
setVideoRotateMode=		YiAPICommand(2,	'setVideoRotateMode',
	values= ["off", "on", "auto"],
	params= {'type':'video_rotate'},
	variable= 'param'
)
#
getBuzzerVolume=		YiAPICommand(1, 'getBuzzerVolume',
	params={'type':'buzzer_volume'}
)
setBuzzerVolume=		YiAPICommand(2,	'setBuzzerVolume',
	values= ["high", "low", "mute"],
	params= {'type':'buzzer_volume'},
	variable= 'param'
)
#
getLoopDuration=		YiAPICommand(1, 'getLoopDuration',
	params={'type':'loop_rec_duration'}
)
setLoopDuration=		YiAPICommand(2,	'setLoopDuration',
	values= ["5 minutes", "20 minutes", "60 minutes", "120 minutes", "max"],
	params= {'type':'loop_rec_duration'},
	variable= 'param'
)
