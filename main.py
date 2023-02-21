from pytube import YouTube

link = input('Enter the video link: ')

yt = YouTube(link)

yt.streams.get_highest_resolution().download()