import pafy
def download_youtube(url):
    print (type(url))
    video=pafy.new(url)
    print (video.thumb)
    print ("Description about the video")
    print ("---------"+video.title+"---------")
    print (video.rating)
    print (video.viewcount)
    print ("Is this the video you are looking for")
    a=input()
    if a == "yes":
        print ("Download audio")
        print ("Download video")
        b=input()
    else:
        print ("Please input correct url")
        exit()
    if b =="audio":
        audio_streams=video.audiostreams
        print ("Bitrate of all the available audio streams are")
        i=0
        for s in audio_streams:
            print(i,s.bitrate,s.filename,s.extension)
            i=i+1
        c=input(int)
        filepath="C:/"
        audio_streams[int(c)].download(filepath)
    if(b=="video"):
        video_streams=video.ge
        print ("Select the resolution to download")
        i=0
        for s in video_streams:
            print(i,s.resolution,s.get_filesize,s.extension)
            i=i+1
        c=input(int)
        filepath="C:/"
        video_streams[int(c)].download(filepath)
url="https://www.youtube.com/watch?v=bMt47wvK6u0"
download_youtube(url)    