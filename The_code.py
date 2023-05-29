import sys
from tkinter import *
import pygame.mixer
import librosa
import numpy as np
import soundfile as sf
from tkinter import filedialog
from pygame import mixer
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
import wave

root = Tk()
root.title("MediaPlayer")
pygame.mixer.init()
mixer.init()
root.configure(bg='green')
root.geometry("703x473")


def play():
    pygame.mixer.music.load(play_list.get(ACTIVE))
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def resume():
    pygame.mixer.music.unpause()
def selcet():
    temp=filedialog.askopenfilenames(initialdir="Music/",filetypes=(("MP3files","*.mp3"),))
    for i in temp:
        play_list.insert(END,i)
def next_music():
    next1=play_list.curselection()
    next1=next1[0]+1
    song=play_list.get(next1)
    song=f'{song}'
    mixer.music.load(song)
    mixer.music.play()
    play_list.select_clear(0,END)
    play_list.activate(next1)
    play_list.select_set(next1)
def back_audio():
    next1=play_list.curselection()
    next1=next1[0]-1
    song=play_list.get(next1)
    song=f'{song}'
    mixer.music.load(song)
    mixer.music.play()
    play_list.select_clear(0,END)
    play_list.activate(next1)
    play_list.select_set(next1)
def add_white_noise(signal, noise_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_factor
    return augmented_signal
def white_noise():
    signal, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal1 = add_white_noise(signal, 0.1)
    sf.write("augmented1.wav", augmented_signal1, sr)
    pygame.mixer.music.load("augmented1.wav")
    pygame.mixer.music.play(loops=0)
    wav0=wave.open("augmented1.wav", "r")
    raw=wav0.readframes(-1)
    raw=np.frombuffer(raw,"int16")
    sampleRate=wav0.getframerate()
    if wav0.getnchannels()==2:
        print("stereo files aren't supported.")
        sys.exit(0)
    #################
    time =np.linspace(0,len(raw)/sampleRate, num =len(raw))
    plt.title (" audio ")
    plt.plot(time,raw,color="blue")
    plt.ylabel("Amp")
    plt.show()
def comp():
    signal, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal2 = librosa.effects.time_stretch(signal,rate=3)
    sf.write("augmented2.wav", augmented_signal2, sr)
    pygame.mixer.music.load("augmented2.wav")
    mixer.music.play()
    wav0=wave.open("augmented2.wav", "r")
    raw=wav0.readframes(-1)
    raw=np.frombuffer(raw,"int16")
    sampleRate=wav0.getframerate()
    if wav0.getnchannels()==2:
        print("stereo files aren't supported.")
        sys.exit(0)
    ################
    time =np.linspace(0,len(raw)/sampleRate, num =len(raw))
    plt.title (" audio ")
    plt.plot(time,raw,color="blue")
    plt.ylabel("Amp")
    plt.show()
def exp():
    signal, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal3 = librosa.effects.time_stretch(signal,rate=0.5)
    sf.write("augmented3.wav", augmented_signal3, sr)
    pygame.mixer.music.load("augmented3.wav")
    mixer.music.play()
    wav0=wave.open("augmented3.wav", "r")
    raw=wav0.readframes(-1)
    raw=np.frombuffer(raw,"int16")
    sampleRate=wav0.getframerate()
    if wav0.getnchannels()==2:
        print("stereo files aren't supported.")
        sys.exit(0)
    #################
    time =np.linspace(0,len(raw)/sampleRate, num =len(raw))
    plt.title (" audio ")
    plt.plot(time,raw,color="blue")
    plt.ylabel("Amp")
    plt.show()
def inc_amp():
    signal, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal4 = librosa.effects.pitch_shift(signal,sr=sr,n_steps=5)
    sf.write("augmented4.wav", augmented_signal4, sr)
    pygame.mixer.music.load("augmented4.wav")
    mixer.music.play()
def dec_amp():
    signal, sr = librosa.load(play_list.get(ACTIVE))
    augmented_signal5 = librosa.effects.pitch_shift(signal,sr=sr,n_steps=-5)
    sf.write("augmented5.wav", augmented_signal5, sr)
    pygame.mixer.music.load("augmented5.wav")
    mixer.music.play()
def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)
def skip_step():
    current_pos = mixer.music.get_pos() // 1000
    new_pos = current_pos + 0.001
    mixer.music.set_pos(new_pos * 10)
    mixer.music.unpause()
def reverse_audio():
    rev, sr = librosa.load(play_list.get(ACTIVE))
    revearse_1 = rev[::-1]
    sf.write("augmented6.wav", revearse_1, sr)
    pygame.mixer.music.load("augmented6.wav")
    mixer.music.play()

#########################################################################
#########################################################################

play_audio = Button(root,text='Play',font=('Times_New_Roman',15),command=play,bg="lightgray",width=7,height=1)
stop_audio = Button(root,text='Stop',font=('Times_New_Roman',15),command=stop,bg="lightgray",width=7,height=1)
pause_audio = Button(root,text='Pause',font=('Times_New_Roman',15),command=pause,bg="lightgray",width=7,height=1)
resume_audio = Button(root,text='Resume',font=('Times_New_Roman',15),command=resume,bg="lightgray",width=7,height=1)
select_audio = Button(root,text='Select',font=('Times_New_Roman',15),command=selcet,bg="lightgray",width=7,height=1)
next_audio = Button(root,text='Next',font=('Times_New_Roman',15),command=next_music,bg="lightgray",width=7,height=1)
back_audio = Button(root,text='Back',font=('Times_New_Roman',15),command=back_audio,bg="lightgray",width=7,height=1)
white_noise_audio = Button(root,text='noise',font=('Times_New_Roman',15),command=white_noise,bg="lightgray",width=7,height=1)
exp_noise_audio = Button(root,text='Expansion noise',font=('Times_New_Roman',15),command=exp,bg="lightgray",width=15,height=1)
comp_noise_audio = Button(root,text='Compression noise',font=('Times_New_Roman',15),command=comp,bg="lightgray",width=15,height=1)
inc_audio = Button(root,text='Increase audio',font=('Times_New_Roman',15),command=inc_amp,bg="lightgray",width=15,height=1)
dec_audio = Button(root,text='Decrease audio',font=('Times_New_Roman',15),command=dec_amp,bg="lightgray",width=15,height=1)
skp = Button(root,text='Skip',font=('Times_New_Roman',15),command=skip_step,bg="lightgray",width=7,height=1)
reverse = Button(root,text='Reverse',font=('Times_New_Roman',15),command=reverse_audio,bg="lightgray",width=7,height=1)
set_volume = Scale(root,from_=0,to=100,orient=HORIZONTAL,font=('Times_New_Roman',10),command=set_vol,bg="lightgray",length=519,tickinterval=20)
set_volume.set(50)


play_audio.place(x=0,y=0)
stop_audio.place(x=88,y=0)
pause_audio.place(x = 176,y=0)
resume_audio.place(x = 264,y=0)
select_audio.place(x = 352,y=0)
next_audio.place(x = 440,y=0)
back_audio.place(x = 528,y=0)
white_noise_audio.place(x = 616,y=0)
exp_noise_audio.place(x = 0,y=40)
comp_noise_audio.place(x = 176,y=40)
inc_audio.place(x = 352,y=40)
dec_audio.place(x = 528,y=40)
skp.place(x = 0,y=83)
reverse.place(x = 88,y=83)
set_volume.place(x = 176,y=80)

play_list = Listbox(root,bg="lightgreen",fg="darkgreen",font=('arial'),height=18,width=77,selectmode=SINGLE,selectbackground="dark blue",selectforeground="lightgreen")
play_list.place(x = 3,y=125 )

root.mainloop()