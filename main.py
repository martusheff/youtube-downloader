from tkinter import *
from pytube import *
from pytube import Playlist, YouTube

root = Tk()

e = Entry(root, width = 80, bg='black',fg='red',borderwidth=5)
e.insert(0, "Enter video/playlist URL...") 
e.pack()
e.get()

def mp4():
	youtube = pytube.YouTube(e.get())
	video = youtube.streams.first()
	video.download()
	success = Label(root, text="Successfully downloaded: " + e.get())
	success.pack()

def playlist():
	p = Playlist(e.get())
	for url in p.video_urls:
		try:
			yt = YouTube(url)
		except:
			failed = Label(root, text=url + " is unavailable. Skipping.")
			failed.pack()
			continue
		else:
			yt.streams.first().download()
			success = Label(root, text="Successfully downloaded: " + url)
			success.pack()



			

mp4 = Button(root, text="MP4", command=mp4)
playlist = Button(root, text="PLAYLIST", command=playlist)

mp4.pack()
playlist.pack()

root.mainloop()