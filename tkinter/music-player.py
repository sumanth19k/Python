##############################################################
def musicurl():
    try:

        dd=filedialog.askopenfilename(initialdir='C:/Users/RS/Downloads',title="Select Audio File",filetypes=(('MP3','.mp3'),('WAV','.wav')))
    except:
        dd=filedialog.askopenfilename(title="Select Audio File",filetypes=(('MP3','.mp3'),('WAV','.wav')))
    audiotrack.set(dd)



def playmusic():
    try:


        ad=audiotrack.get()
        mixer.music.load(ad)
        progressbarLabel.grid()

        window.mutebutton.grid()
        progressbarmusicLabel.place(x=15,y=350)

        mixer.music.set_volume(0.4)
        progressbarvolume['value']=40
        progressbarvolumeLabel['text']='40%'
        mixer.music.play()
        audiostatuslabel.config(image=playlabel)
        song=MP3(ad)
        totalsonglength=int(song.info.length)
        progressbarmusic['maximum']=totalsonglength
        progressbarendtimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))

        def progressbarmusictick():
            currentsonglength=mixer.music.get_pos()//1000
            progressbarmusic['value']=currentsonglength
            progressbarstarttimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=currentsonglength))))
            progressbarmusic.after(2,progressbarmusictick)

        progressbarmusictick()

    except:
        messagebox.showerror("Error","Can't Play, Select a Song")



def pausemusic():
    mixer.music.pause()
    currentsonglength = mixer.music.get_pos() // 1000
    progressbarmusic['value'] = currentsonglength
    progressbarstarttimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=currentsonglength))))
    window.pausebutton.grid_remove
    window.resumebutton.grid()
    audiostatuslabel.config(image=pauselabel)
def resumemusic():
    window.pausebutton.grid()
    window.resumebutton.grid_remove()
    mixer.music.unpause()
    audiostatuslabel.config(image=playlabel)

def volumeup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.02)
    progressbarvolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressbarvolume['value']=mixer.music.get_volume()*100
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.02)
    progressbarvolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    progressbarvolume['value'] = mixer.music.get_volume() * 100
def stopmusic():



    mixer.music.stop()
    audiostatuslabel.config(image=stoplabel)
    progressbarstarttimeLabel.config(text='0:00:0')


def mutemusic():
    global currentvolume
    window.mutebutton.grid_remove()
    window.unmutebutton.grid()
    currentvolume=mixer.music.get_volume()
    mixer.music.set_volume(0)

def unmutemusic():
    global currentvolume
    window.unmutebutton.grid_remove()
    window.mutebutton.grid()
    mixer.music.set_volume(currentvolume)




def createwidths():
    global audiostatuslabel,progressbarvolume,progressbarvolumeLabel,progressbarLabel,progressbarmusicLabel,progressbarmusic,progressbarstarttimeLabel,progressbarendtimeLabel
    global imbrowse,imstop,implay,impause,imvolumeup,imvolumedown,imresume,immute,musical,imunmute,playlabel,stoplabel,pauselabel
    imstop=PhotoImage(file="stop.png")
    implay=PhotoImage(file="play.png")
    impause=PhotoImage(file="pause.png")
    imresume = PhotoImage(file="resume.png")
    imbrowse=PhotoImage(file="search.png")
    imvolumeup=PhotoImage(file="volumeup.png")
    imvolumedown=PhotoImage(file="volumedown.png")
    immute = PhotoImage(file="mute.png")
    imunmute = PhotoImage(file="unmute.png")
    playlabel = PhotoImage(file="playlabel.png")
    stoplabel = PhotoImage(file="stoplabel.png")
    pauselabel = PhotoImage(file="pauselabel.png")
    musical = PhotoImage(file="musical.png")
    #resumelabel = PhotoImage(file="resumelabel.png")
    #######################################chnge size
    imbrowse = imbrowse.subsample(2, 2)
    imstop=imstop.subsample(2,2)
    implay = implay.subsample(2, 2)
    impause = impause.subsample(2, 2)
    imresume = imresume.subsample(2, 2)
    imvolumeup = imvolumeup.subsample(2, 2)
    imvolumedown = imvolumedown.subsample(2, 2)
    immute = immute.subsample(2, 2)
    imunmute = imunmute.subsample(2, 2)

    ############labeL#########################
    # trackLabel=Label(window,text="Select Audio Track",bg='darkorange1',font=('arial',15,'bold'))
    # trackLabel.grid(row=0,column=0,padx=20,pady=20)
    musicallabel = Label(window,image=musical,bg='darkorange1')
    musicallabel.place(x=750,y=350)

    audiostatuslabel=Label(window,bg='darkorange1',font=('arial',15,'bold'))
    audiostatuslabel.grid(row=1,column=1)

    #############entrybox##################################
    tracklabelentry=Entry(window,font=('arial',16,'bold'),width=35,bg='grey18',fg='white',textvariable=audiotrack)
    tracklabelentry.grid(row=0,column=1,padx=20,pady=20)
    ##############################Buttons####################################
    browsebutton=Button(window,text="Search",bg="lightskyblue",width=140,bd=5,font=('arial',13,'bold'),
    activebackground='deeppink',activeforeground='white',image=imbrowse,compound=RIGHT,command=musicurl)
    browsebutton.grid(row=0,column=2,padx=20,pady=20)

    playbutton = Button(window, text="Play", bg="goldenrod", width=140, bd=5, font=('arial', 13, 'bold'),
                          activebackground='black', activeforeground='white',image=implay,compound=RIGHT,command=playmusic)
    playbutton.grid(row=1, column=0, padx=20, pady=20 )

    window.pausebutton = Button(window, text="Pause", bg="purple1", width=140, bd=5, font=('arial', 13, 'bold'),
                     activebackground='blue', activeforeground='white',image=impause,compound=RIGHT,command=pausemusic)
    window.pausebutton.grid(row=0, column=0, padx=20, pady=20 )

    window.resumebutton = Button(window, text="Resume", bg="purple1", width=140, bd=5, font=('arial', 13, 'bold'),
                         activebackground='blue', activeforeground='white', image=imresume, compound=RIGHT,
                         command=resumemusic)
    window.resumebutton.grid(row=0, column=0, padx=20, pady=20 )
    window.resumebutton.grid_remove()

    volumeupbutton = Button(window, text="Volume Up", bg="orchid1", width=140, bd=5, font=('arial', 13, 'bold'),
                          activebackground='yellow', activeforeground='white',image=imvolumeup,compound=RIGHT,command=volumeup)
    volumeupbutton.grid(row=1, column=2, padx=20, pady=20 )

    stopbutton = Button(window, text="Stop", bg="dodger blue", width=140, bd=5, font=('arial', 13, 'bold'),
                          activebackground='red4', activeforeground='white',image=imstop,compound=RIGHT,command=stopmusic)
    stopbutton.grid(row=2, column=0, padx=20, pady=20 )

    volumedownbutton = Button(window, text="Volume Down", bg="seagreen", width=140, bd=5, font=('arial', 13, 'bold'),
                          activebackground='grey25', activeforeground='white',image=imvolumedown,compound=RIGHT,command=volumedown)
    volumedownbutton.grid(row=2, column=2, padx=20, pady=20 )

    window.mutebutton=Button(window,text='Mute',width=100,bg='yellow',activebackground='purple4',bd=5,image=immute,
                             compound=RIGHT,command=mutemusic)
    window.mutebutton.grid(row=3,column=3)
    window.mutebutton.grid(row=3, column=3)
    window.mutebutton.grid_remove()

    window.unmutebutton = Button(window, text='Unmute', width=100, bg='hotpink4', activebackground='cyan3', bd=5,
                               image=imunmute, compound=RIGHT,command=unmutemusic)
    window.unmutebutton.grid(row=3, column=3)
    window.unmutebutton.grid_remove()

    progressbarLabel=Label(window,text='',bg='red')
    progressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    progressbarLabel.grid_remove()
    progressbarvolume=Progressbar(progressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=120)
    progressbarvolume.grid(row=0,column=0,ipadx=5)

    progressbarvolumeLabel=Label(progressbarLabel,text='0%',bg='white',width=3)
    progressbarvolumeLabel.grid(row=0,column=0)

###############################################################################
    progressbarmusicLabel = Label(window, text='', bg='red')
    progressbarmusicLabel.place(x=15,y=350)
    progressbarmusicLabel.place_forget()
    progressbarstarttimeLabel = Label(progressbarmusicLabel, text='0:00:0', bg='red',width=4)
    progressbarstarttimeLabel.grid(row=0, column=0)

    progressbarmusic = Progressbar(progressbarmusicLabel, orient=HORIZONTAL, mode='determinate', value=0)
    progressbarmusic.grid(row=0, column=1, ipadx=320,ipady=3)


    progressbarendtimeLabel = Label(progressbarmusicLabel, text='0:00:0', bg='red')
    progressbarendtimeLabel.grid(row=0, column=2)


###############################################################
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.ttk import Progressbar
from pygame import mixer
import datetime
from mutagen.mp3 import MP3
window=Tk()
window.geometry('970x500+120+50')
window.title("Music Player Created By vishnu")
window.resizable(0,0)
window.configure(bg="darkorange1")
label=Label(window,bg='darkorange1',height=320)
label.place(x=330,y=70)

################################################################global variables
audiotrack=StringVar()
currentvolume=0
count=0
text=''
totalsonglength=0

ss="Music Player Developed By vishnuvardhan"

silderLabel=Label(window,text=ss,bg='darkorange1',font=('arial','25','bold'))
silderLabel.place(x=80,y=450)

import random
colors=['red','green','blue','yellow','red2','gold2','black','purple','grey','snow','dark slate gray','royal blue4']
def introColor():
    fg=random.choice(colors)
    silderLabel.config(fg=fg)
    silderLabel.after(1000,introColor)

def introlabeltick():
    global  count,text
    if count>=len(ss):
        count=-1
        text=''
        silderLabel.config(text=text)
    else:
        text=text+ss[count]
        silderLabel.config(text=text)
    count+=1
    silderLabel.after(200,introlabeltick)


introColor()
introlabeltick()
mixer.init()



createwidths()




window.mainloop()
