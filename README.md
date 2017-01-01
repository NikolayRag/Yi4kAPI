# Yi4kAPI
Lightweight python API for Yi 4k camera.

It is reverse-engineered from official Java API.  
Current limits are:
- values provided to commands should be correct strings,
- camera data exchanging operations are blocking,
- no callbacks are supported.

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
