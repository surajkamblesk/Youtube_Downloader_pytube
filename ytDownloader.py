from pytube import YouTube
url = input("Enter the YouTube Url")
YouTube(url).streams.first().download()
