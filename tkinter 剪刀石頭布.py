import tkinter as tk
import random
winscore=0
tiescore=0
losescore=0
def button_event():
    global winscore
    global tiescore
    global losescore

    list1=["rock","paper","scissor"]
    a=random.randint(0,2)
    x=int(enter.get())
    if x==0:
        la3["text"]="rock"
    elif x==1:
        la3["text"]="paper"
    elif x==2:
        la3["text"]="scissor"
    la4["text"] = list1[a]

    if x==a:
        la5["text"]="tie"
        tiescore=tiescore + 1
    elif x==0 and a==2 : 
        la5["text"]="you win"
        winscore= winscore + 1
    elif x==0 and a==1  :
        la5["text"]="you lose"
        losescore =losescore + 1
    elif  x==1 and a==0 : 
        la5["text"]="you win"
        winscore  = winscore +1
    elif  x==1 and a==2  :
        la5["text"]="you lose"
        
        losescore = losescore +1
    elif  x==2 and a==1: 
        la5["text"]="you win"
        winscore = winscore +1
    elif  x==2 and a==0 :
        la5["text"]="you lose"
        losescore +=1
def watchscore():
    la7["text"]= "平手:" + str(tiescore) 
    la8["text"]= "贏:" + str(winscore) 
    la9["text"]= "輸" + str(losescore) 
    
    
window = tk.Tk() 
window.title("window") 

window.geometry("600x600")

la=tk.Label(window,text="rock=0 paper=1 scissor=2")
la.place(x=250,y=80)

la1=tk.Label(window,text="player:")
la1.place(x=250,y=200)

la3=tk.Label(window,text="")
la3.place(x=300,y=200)

la2=tk.Label(window,text="npc:")
la2.place(x=250,y=230)

la4=tk.Label(window,text="")
la4.place(x=300,y=230)

la5=tk.Label(window,text="")
la5.place(x=250,y=270)

bu2=tk.Button(window,text="score",command=watchscore)
bu2.place(x=250,y=300)

la7=tk.Label(window,text="")
la7.place(x=250,y=330)

la8=tk.Label(window,text="")
la8.place(x=250,y=360)

la9=tk.Label(window,text="")
la9.place(x=250,y=390)

bu=tk.Button(window,text="press it",command=button_event)
bu.place(x=250,y=160)

enter=tk.Entry()
enter.place(x=250,y=120)

window.mainloop()
