from pytube import YouTube
from cProfile import label
import youtube_dl as yt
from tkinter import *
from tkinter import Tk, font, ttk


def display_options(*event):

    hide()
    
    ydl_opts = {}
    resolutions = []

    url = link.get()
    
    valid = valid_link(url)  # check the validity of link
 
    if valid:
        with yt.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False) 
            formats = meta.get('formats', meta) 
            vid_title = meta.get('title', meta) # gets the title

        title.config(text=f'Title: {vid_title}')
        title.place(x=220, y=70)

        for f in formats:
            resolutions.append(f['format']) #filter to only formats

        options['values'] = resolutions # sets combobox values to available resolutions

    else:
        error.config(text='Invalid link', fg='red')
        error.place(x=150, y=210)

def valid_link(link): # function to check validity of the link
   
    extractors = yt.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(link) and e.IE_NAME != 'generic':
            return True
    return False


def download():
    hide()
    res = option_lst.get()

    if res !=  'resolution':
        res = int(res[:res.find('-')].strip())
        
        ydl_opts = {'format': f'{res}', 
                    'outtmpl': r'C:\Users\rohit\Downloads\Animated Skills \%(title)s.%(ext)s'} # specify your download path here

        url = link.get()
        
        with yt.YoutubeDL(ydl_opts) as ydl: 
         ydl.download([url]),
         Label_1=Label(root, text="video downloaded sucsessfuly", font='arial 10',bg="grey").place(x=650,y=250)
            
        
    else:
        error.config(text='Invalid resolution', fg='red')
        error.place(x=150, y=210)
    
def hide():
    title.place_forget()
    error.place_forget()


root = Tk()
root.state('zoomed')
root.configure(bg="grey")
root.title('universal downloader')

link = StringVar()
option_lst = StringVar()

link.trace('w', display_options)
option_lst.set('resolution')

link_here = Label(root, text="YouTube video link Paste Here", font='arial 15 bold',pady=50,fg="white",bg="grey")
link_here.pack()

title = Label(root, text='',padx=340,pady=15,bg="grey",fg="red")
title.place(x=220, y=210)
error = Label(root, text='',padx=600,pady=30,bg="grey")
error.place(x=220, y=210)

options = ttk.Combobox(root, textvariable=option_lst, state="readonly") 
options.place(x=600, y=200)

pasted = Entry(root,width=70,textvariable=link,)
pasted.pack()



Button(root,text="Download Video", width=20, bg="black", fg="gray", command=download).place(x=800,y=195)

root.mainloop()
