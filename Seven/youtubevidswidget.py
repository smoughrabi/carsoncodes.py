#code is based on the following two articles:
#1. Azuelo, G., &amp; patil, K. (2022, September 16). YouTube video downloader using python with source code. SourceCodeHero. Retrieved September 23, 2022, from https://sourcecodehero.com/youtube-video-downloader-using-python-with-source-code/
#2. Creating a simple YouTube video downloader using Python. Section. (n.d.). Retrieved September 23, 2022, from https://www.section.io/engineering-education/youtube-video-downloader-using-python/

from tkinter import *
from pytube import YouTube

#creating a tkinter window
gui = Tk()
gui.geometry("370x200")
gui.title('🤖')
gui['background']='#248888'

SAVE_PATH = '/Users/sarahelmoughrabi/Documents/CarsonCodes/Seven'
link = StringVar()


#.pack() is used to expand the contents with the screen size so that they're always centered
Label(gui,text="MP4-Now", font='work-sans 18 bold',bg='#248888',fg='#f7e2d1').pack()
Label(gui,text="Your desktop companion for downloading Youtube videos ad-free", font='work-sans 11',bg='#248888',fg='#f7e2d1').pack()
Label(gui,text="Paste your link here:", font='work-sans 12 bold',bg='#248888',fg='#f7e2d1').place(x=10,y=80,height=30)
link_inputbox = Entry(gui, width=20,textvariable=link).place(x=150, y=80)


#def downloader():
#    url = YouTube(str(link.get()))
#    url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
#    Label(url, text='Downloaded! Enjoy :), font = open-sans 12').place(x=260,y=125)

def downloader():
   url = YouTube(str(link.get()))
   video = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
   video.download(SAVE_PATH)
   Label(gui, text='Downloaded! Enjoy :)',font='work-sans 12 bold',bg='#248888',fg='#f7e2d1').place(x=220,y=160)

Button(gui, text='click to download', font='work-sans 12 bold', fg='#248888', padx=2,command=downloader).place(x=220, y=125)




gui.mainloop()
