# Yi4kAPI
Python API for Yi 4k camera.

It is based on official Yi 4k Java API.  
Differences from original API:
- Commands are blocking waiting for result, while in original API they return promices.
- 'stopRecording' and 'capturePhoto' waits till operation is really ended and return produced file name.
- Values provided to commands should be correct strings, compared to integers in original API.
- 'adapter', 'adapter_status' and 'battery_status' callbacks are available in addition to all other. .setCB() used to set/get callbacks.

Try not to call same commands simultaneously from different threads: camera response is not clearly identified with caller and response can be mixed.

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
