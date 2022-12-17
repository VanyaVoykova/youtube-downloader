from pytube import YouTube

def Download(link):
    youTubeObject = YouTube(link)
    highestResolutionObject = youTubeObject.streams.get_highest_resolution() #.streams will give the options
    
    try:
        highestResolutionObject.download()
    except:
        print("Error downloading video.")        
    print("Download completed.")
    
link = input("Enter video link: ")
Download(link)
    
    