import pafy

#input the video url that you want to download
url = input('Enter the video url : ')

video = pafy.new(url);
print('\nVideo at this url : ',video.title)

flag = input('You want to continue with download (Y/N) : ')

if(flag=='Y'):

	#specify the stream that you want to download
	download_choice = input('Downlod audio(A)/video(V)/both(B) ? ')
	streams = video.streams
	 
	if(download_choice=='A'):
		streams = video.audiostreams
	
	if(download_choice=='V'):
		streams  = video.videostreams
	i=0
	
	#list the acailable streams
	for stream in streams :
		print (i+1,stream)
		i=i+1
	
	index = input('Enter your desired choice : ')
	index = int(index) - 1
	
	if(index>i):
		index = i-1
	
	#download the specific stream
	print('Downloading file ',video.title,'  ...')
	streams[index].download(quiet = True)
	print('File downloaded..')
