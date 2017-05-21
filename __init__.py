'''
Lightweighted version of Yi4k API, based on official Java API.
Values provided to commands should be correct strings.

deleteFile and getFileList commands require path relative to DCIM folder.
deleteFile though could be unsafe by supplying '..' path.

Commands not implemented:

	formatSDCard
		NSFW

	downloadFile
	cancelDownload
		Redundant, available by http

	getRtspURL
		Redundant, available at YiAPI() creation

	buildLiveVideoQRCode
		Maybe later

	startRecording datetime
		Lazy to implement, due to different input value format
'''



from .yiAPI import *


'''
Define public commands
'''

startRecording=		YiAPICommandGen(513, 'startRecording')
stopRecording=		YiAPICommandGen(514, 'stopRecording',
	resultReq= {'msg_id': 7, 'type': 'video_record_complete'}
)

capturePhoto=		YiAPICommandGen(16777220, 'capturePhoto',
	params= {'param':'precise quality;off'},
	resultReq= {'msg_id': 7, 'type': 'photo_taken'}
)

getFileList=		YiAPICommandGen(1282, 'getFileList',
	params= {'param':'/tmp/fuse_d/DCIM/'},
	variable= 'param',
	resultCB= lambda res: res['listing']
)

deleteFile=		YiAPICommandGen(1281, 'deleteFile',
	params= {'param':'/tmp/fuse_d/DCIM/'},
	variable= 'param'
)

startViewFinder=		YiAPICommandGen(259, 'startViewFinder')
stopViewFinder=		YiAPICommandGen(260, 'stopViewFinder')


getSettings=		YiAPICommandGen(3,	'getSettings',
	resultCB= lambda res:{key:val for d in res['param'] for key,val in d.items()}
)

setDateTime=		YiAPICommandGen(2,	'setDateTime "yyyy-MM-dd HH:mm:ss"',
	params= {'type':'camera_clock'},
	variable= 'param'
)

setSystemMode=		YiAPICommandGen(2,	'setSystemMode',
	values= ["capture", "record"],
	params= {'type':'system_mode'},
	variable= 'param'
)

getVideoResolution=		YiAPICommandGen(1, 'getVideoResolution',
	params={'type':'video_resolution'}
)
setVideoResolution=		YiAPICommandGen(2,	'setVideoResolution',
	values= ["3840x2160 30P 16:9", "3840x2160 30P 16:9 super", "2560x1920 30P 4:3", "1920x1440 60P 4:3", "1920x1440 30P 4:3", "1920x1080 120P 16:9", "1920x1080 120P 16:9 super", "1920x1080 60P 16:9", "1920x1080 60P 16:9 super", "1920x1080 30P 16:9", "1920x1080 30P 16:9 super", "1280x960 120P 4:3", "1280x960 60P 4:3", "1280x720 240P 16:9", "1280x720 120P 16:9 super", "1280x720 60P 16:9 super", "840x480 240P 16:9"],
	params= {'type':'video_resolution'},
	variable= 'param'
)

getPhotoResolution=		YiAPICommandGen(1, 'getPhotoResolution',
	params={'type':'photo_size'}
)
setPhotoResolution=		YiAPICommandGen(2,	'setPhotoResolution',
	values= ["12MP (4000x3000 4:3) fov:w", "7MP (3008x2256 4:3) fov:w", "7MP (3008x2256 4:3) fov:m", "5MP (2560x1920 4:3) fov:m", "8MP (3840x2160 16:9) fov:w"],
	params= {'type':'photo_size'},
	variable= 'param'
)

getPhotoWhiteBalance=		YiAPICommandGen(1, 'getPhotoWhiteBalance',
	params={'type':'iq_photo_wb'}
)
setPhotoWhiteBalance=		YiAPICommandGen(2,	'setPhotoWhiteBalance',
	values= ["auto", "native", "3000k", "5500k", "6500k"],
	params= {'type':'iq_photo_wb'},
	variable= 'param'
)

getVideoWhiteBalance=		YiAPICommandGen(1, 'getVideoWhiteBalance',
	params={'type':'iq_video_wb'}
)
setVideoWhiteBalance=		YiAPICommandGen(2,	'setVideoWhiteBalance',
	values= ["auto", "native", "3000k", "5500k", "6500k"],
	params= {'type':'iq_video_wb'},
	variable= 'param'
)

getPhotoISO=		YiAPICommandGen(1, 'getPhotoISO',
	params={'type':'iq_photo_iso'}
)
setPhotoISO=		YiAPICommandGen(2,	'setPhotoISO',
	values= ["auto", "100", "200", "400", "800", "1600", "6400"],
	params= {'type':'iq_photo_iso'},
	variable= 'param'
)

getVideoISO=		YiAPICommandGen(1, 'getVideoISO',
	params={'type':'iq_video_iso'}
)
setVideoISO=		YiAPICommandGen(2,	'setVideoISO',
	values= ["auto", "100", "200", "400", "800", "1600", "6400"],
	params= {'type':'iq_video_iso'},
	variable= 'param'
)

getPhotoExposureValue=		YiAPICommandGen(1, 'getPhotoExposureValue',
	params={'type':'iq_photo_ev'}
)
setPhotoExposureValue=		YiAPICommandGen(2,	'setPhotoExposureValue',
	values= ["-2.0", "-1.5", "-1.0", "-0.5", "0", "+0.5", "+1.0", "+1.5", "+2.0"],
	params= {'type':'iq_photo_ev'},
	variable= 'param'
)

getVideoExposureValue=		YiAPICommandGen(1, 'getVideoExposureValue',
	params={'type':'iq_video_ev'}
)
setVideoExposureValue=		YiAPICommandGen(2,	'setVideoExposureValue',
	values= ["-2.0", "-1.5", "-1.0", "-0.5", "0", "+0.5", "+1.0", "+1.5", "+2.0"],
	params= {'type':'iq_video_ev'},
	variable= 'param'
)

getPhotoShutterTime=		YiAPICommandGen(1, 'getPhotoShutterTime',
	params={'type':'iq_photo_shutter'}
)
setPhotoShutterTime=		YiAPICommandGen(2,	'setPhotoShutterTime',
	values= ["auto", "2s", "5s", "10s", "20s", "30s"],
	params= {'type':'iq_photo_shutter'},
	variable= 'param'
)

getVideoSharpness=		YiAPICommandGen(1, 'getVideoSharpness',
	params={'type':'video_sharpness'}
)
setVideoSharpness=		YiAPICommandGen(2,	'setVideoSharpness',
	values= ["low", "medium", "high"],
	params= {'type':'video_sharpness'},
	variable= 'param'
)

getPhotoSharpness=		YiAPICommandGen(1, 'getPhotoSharpness',
	params={'type':'photo_sharpness'}
)
setPhotoSharpness=		YiAPICommandGen(2,	'setPhotoSharpness',
	values= ["low", "medium", "high"],
	params= {'type':'photo_sharpness'},
	variable= 'param'
)

getVideoFieldOfView=		YiAPICommandGen(1, 'getVideoFieldOfView',
	params={'type':'fov'}
)
setVideoFieldOfView=		YiAPICommandGen(2,	'setVideoFieldOfView',
	values= ["wide", "medium", "narrow"],
	params= {'type':'fov'},
	variable= 'param'
)

getRecordMode=		YiAPICommandGen(1, 'getRecordMode',
	params={'type':'rec_mode'}
)
setRecordMode=		YiAPICommandGen(2,	'setRecordMode',
	values= ["record", "record_timelapse", "record_slow_motion", "record_loop", "record_photo"],
	params= {'type':'rec_mode'},
	variable= 'param'
)

getCaptureMode=		YiAPICommandGen(1, 'getCaptureMode',
	params={'type':'capture_mode'}
)
setCaptureMode=		YiAPICommandGen(2,	'setCaptureMode',
	["precise quality", "precise self quality", "burst quality", "precise quality cont."],
	{'type':'capture_mode'},
	variable= 'param'
)

getMeteringMode=		YiAPICommandGen(1, 'getMeteringMode',
	params={'type':'meter_mode'}
)
setMeteringMode=		YiAPICommandGen(2,	'setMeteringMode',
	values= ["center", "average", "spot"],
	params= {'type':'meter_mode'},
	variable= 'param'
)

getVideoQuality=		YiAPICommandGen(1, 'getVideoQuality',
	params={'type':'video_quality'}
)
setVideoQuality=		YiAPICommandGen(2,	'setVideoQuality',
	values= ["S.Fine", "Fine", "Normal"],
	params= {'type':'video_quality'},
	variable= 'param'
)

getVideoColorMode=		YiAPICommandGen(1, 'getVideoColorMode',
	params={'type':'video_flat_color'}
)
setVideoColorMode=		YiAPICommandGen(2,	'setVideoColorMode',
	values= ["yi", "flat"],
	params= {'type':'video_flat_color'},
	variable= 'param'
)

getPhotoColorMode=		YiAPICommandGen(1, 'getPhotoColorMode',
	params={'type':'photo_flat_color'}
)
setPhotoColorMode=		YiAPICommandGen(2,	'setPhotoColorMode',
	values= ["yi", "flat"],
	params= {'type':'photo_flat_color'},
	variable= 'param'
)

getElectronicImageStabilizationState=		YiAPICommandGen(1, 'getElectronicImageStabilizationState',
	params={'type':'iq_eis_enable'}
)
setElectronicImageStabilizationState=		YiAPICommandGen(2,	'setElectronicImageStabilizationState',
	values= ["on", "off"],
	params= {'type':'iq_eis_enable'},
	variable= 'param'
)

getAdjustLensDistortionState=		YiAPICommandGen(1, 'getAdjustLensDistortionState',
	params={'type':'warp_enable'}
)
setAdjustLensDistortionState=		YiAPICommandGen(2,	'setAdjustLensDistortionState',
	values= ["on", "off"],
	params= {'type':'warp_enable'},
	variable= 'param'
)

getVideoMuteState=		YiAPICommandGen(1, 'getVideoMuteState',
	params={'type':'video_mute_set'}
)
setVideoMuteState=		YiAPICommandGen(2,	'setVideoMuteState',
	values= ["on", "off"],
	params= {'type':'video_mute_set'},
	variable= 'param'
)

getVideoTimestamp=		YiAPICommandGen(1, 'getVideoTimestamp',
	params={'type':'video_stamp'}
)
setVideoTimestamp=		YiAPICommandGen(2,	'setVideoTimestamp',
	values= ["off", "time", "date", "date/time"],
	params= {'type':'video_stamp'},
	variable= 'param'
)

getPhotoTimestamp=		YiAPICommandGen(1, 'getPhotoTimestamp',
	params={'type':'photo_stamp'}
)
setPhotoTimestamp=		YiAPICommandGen(2,	'setPhotoTimestamp',
	values= ["off", "time", "date", "date/time"],
	params= {'type':'photo_stamp'},
	variable= 'param'
)

getLEDMode=		YiAPICommandGen(1, 'getLEDMode',
	params={'type':'led_mode'}
)
setLEDMode=		YiAPICommandGen(2,	'setLEDMode',
	values= ["all enable", "all disable", "status enable"],
	params= {'type':'led_mode'},
	variable= 'param'
)

getVideoStandard=		YiAPICommandGen(1, 'getVideoStandard',
	params={'type':'video_standard'}
)
setVideoStandard=		YiAPICommandGen(2,	'setVideoStandard',
	values= ["PAL", "NTSC"],
	params= {'type':'video_standard'},
	variable= 'param'
)

getTimeLapseVideoInterval=		YiAPICommandGen(1, 'getTimeLapseVideoInterval',
	params={'type':'timelapse_video'}
)
setTimeLapseVideoInterval=		YiAPICommandGen(2,	'setTimeLapseVideoInterval',
	values= ["0.5", "1", "2", "5", "10", "30", "60"],
	params= {'type':'timelapse_video'},
	variable= 'param'
)

getTimeLapsePhotoInterval=		YiAPICommandGen(1, 'getTimeLapsePhotoInterval',
	params={'type':'precise_cont_time'}
)
setTimeLapsePhotoInterval=		YiAPICommandGen(2,	'setTimeLapsePhotoInterval',
	values= ["continue", "0.5 sec", "1.0 sec", "2.0 sec", "5.0 sec", "10.0 sec", "30.0 sec", "60.0 sec", "2.0 min", "5.0 min", "10.0 min", "30.0 min", "60.0 min"],
	params= {'type':'precise_cont_time'},
	variable= 'param'
)

getTimeLapseVideoDuration=		YiAPICommandGen(1, 'getTimeLapseVideoDuration',
	params={'type':'timelapse_video_duration'}
)
setTimeLapseVideoDuration=		YiAPICommandGen(2,	'setTimeLapseVideoDuration',
	values= ["off", "6s", "8s", "10s", "20s", "30s", "60s", "120s"],
	params= {'type':'timelapse_video_duration'},
	variable= 'param'
)

getScreenAutoLock=		YiAPICommandGen(1, 'getScreenAutoLock',
	params={'type':'screen_auto_lock'}
)
setScreenAutoLock=		YiAPICommandGen(2,	'setScreenAutoLock',
	values= ["never", "30s", "60s", "120s"],
	params= {'type':'screen_auto_lock'},
	variable= 'param'
)

getAutoPowerOff=		YiAPICommandGen(1, 'getAutoPowerOff',
	params={'type':'auto_power_off'}
)
setAutoPowerOff=		YiAPICommandGen(2,	'setAutoPowerOff',
	values= ["off", "3 minutes", "5 minutes", "10 minutes"],
	params= {'type':'auto_power_off'},
	variable= 'param'
)

getVideoRotateMode=		YiAPICommandGen(1, 'getVideoRotateMode',
	params={'type':'video_rotate'}
)
setVideoRotateMode=		YiAPICommandGen(2,	'setVideoRotateMode',
	values= ["off", "on", "auto"],
	params= {'type':'video_rotate'},
	variable= 'param'
)

getBuzzerVolume=		YiAPICommandGen(1, 'getBuzzerVolume',
	params={'type':'buzzer_volume'}
)
setBuzzerVolume=		YiAPICommandGen(2,	'setBuzzerVolume',
	values= ["high", "low", "mute"],
	params= {'type':'buzzer_volume'},
	variable= 'param'
)

getLoopDuration=		YiAPICommandGen(1, 'getLoopDuration',
	params={'type':'loop_rec_duration'}
)
setLoopDuration=		YiAPICommandGen(2,	'setLoopDuration',
	values= ["5 minutes", "20 minutes", "60 minutes", "120 minutes", "max"],
	params= {'type':'loop_rec_duration'},
	variable= 'param'
)
