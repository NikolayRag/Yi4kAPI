# Yi4kAPI
Python API for Yi 4k camera.

It is based on official Yi 4k Java API.  
Current limits are:
- values provided to commands should be correct strings,
- commands are blocking while waiting for result,
- try not to call same commands simultaneous from different threads, response can be a mess.


###Commands not implemented:

-	formatSDCard  
		NSFW

-	deleteFile  
		Considered vulnerable, maybe later

-	downloadFile
-	cancelDownload  
		Redundant, available by http

-	getRtspURL  
		Redundant, available at YiAPI() creation

-	buildLiveVideoQRCode  
		Maybe later

-	startRecording datetime  
		Lazy to implement
