from tkinter import*
import time
import math
import random
root=Tk()
cback='SteelBlue4'
c=Canvas(master=root,bg=cback,width=1300,height=700)
c.pack()
root.title('Shooter')
picstring=b'R0lGODlhMgAyAPcAAAEBAQsFBQwKCRMKChkNDRYQDhUTEhsVExwcHCAWFCEYFiQaGSofHy0hHiUlJS4uLjEjITkpJjMvLj0sKTExMT47PEoYF1IbGUEvLEgqKkIwLE84NEM+Pk8+O1c+Ol9EPzlZd1NQT1FRUXRTTW1cWGJiYoZbRoZeSoJcVYphTp1vT59xT4tjW5JnVZZpV5RqWZxtXJ5yUaByT6FzUaZ6W6t7XZ5xYKZ0ZKZ+Yad2bah3aKp5abJ/ZbF9brB+cKyEZq6KbbWBZrSCabuFbrCKbK+LcLaAc72Gcr2Ge76IfLWTebuZf8CHcsOKdcSKfMqOfR5XgEtrjEl+rVeApl6EqE2RvW6Mr3y015SUlLaIgL2KgJqltZinvL6opbqzt8WLgcqOg82RhM6Tic6YjtKThdOVitiXituZjcqclN2ek8GjjcSplMegmcmgmciumd2glcqxn+CnneConseno8y0os+4p8+yrdKwq9O+rs65tsm7udO5tNG+u+KrouSxqOa4r+e9tdfFttnIvJC00cjEx9TIx93NwtTT09zc3OzLxePVyu/SzObb0vPe2uvi2/Ti3uTk5Ozs7Pbl4vXp5fLs6fnu7PXx7vb08/r19Pv49/79/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJsALAAAAAAyADIAAAj+ADcJHEiwoMGDCBMqXMiwoUOGmjIxCoQHjxs4SuAAUQNnjaNMmjQ9dKiJEp0YK2KoXJFypUqULIEYAjkS4SVHRGawlCFjBs+fMliu4AmzZ51MNQlqCjT0ZVOYLaE6lbFSCSWRNTUVGUp1ZdSgM1RSDYsyhs6zMeggfehI586wO3um7Bl0Z9kVM8gOnaFkLUNLLfFGZen0ZYy6XgMTjvGDEcNLeceandvTbE+yZn2GzUvY59gZS7Ai1ESEcGevVIO6dKlY7+IVihQKwos5L9nKKm3DtZ05L0rftpWINvgDbmazU7sC931Zt++oKCnZ1Nl883PdvanbZrk95QwaZPH+IMSzgsaQI0eYMGnCnv0T90/ixw9DP0yZ+/jNnNnPH+WSg5rgsEIQ/BVo4IEIJsgfDeUByJIQCkYo4YE1+DScQJmgNMSEE5aRxA4wuGDDDk4UyMNQF25yiYYFhuEDDC28AMMNRCRRRoJOvJCCCTz2aEIKOuw3hE5+DbTiCk3sB4YNPppwQo8lIijECzcYkUQWSYQBhhMwnFBiE0MVKdCRSTrhpA5GfCEGf2WAQUaEY3gRBRRXHJLHGGeEgcQZTqgk5iYZrvDEGUbsIEYZc1ABwiCIFMKGhGHoQYgVU2yxxx1oFEgGSjQppdKgN57RxSFVTMEFH3awESqHCh5mhh/+omnyCINhKKgfqxOGtZ9ok5wRhAxv4iqsgUMQeAavZzwxxKrCMitsGqJhMuyBa057xh9KvWEtm9tKUlAl2+7nLKt9pChJuIcOu0iKAkmirbVl1IoruwNJO+191bJKr0Ca9BEurnEwdO6/HAICURrWmhHvlhIu0lAiChqxwQEGVFyAxQckkMACC2ywZ4LeMmQvgmCAMS6C+R6ISUOayJFgGSkfiF+btx6477cJ2jfzzicb+EEHK7NMQgTBEswfCwCUcHNBlyAAARhG7+dEASIsbRAkACgANcFgLPCA1QdB4sDT/3YdQCRJDZQJBQl83OIXcDsB9xdOyMufBgAgkjZ8QZYIUIDb+3kAwOABBDA4ABgUOAIAh+xdUCQGNMCs4IMPMMDhie+HAgBYOG6QJU5vfQblB2SQgQGDZ54DABSA/RDWWgc+OAcWXFBB6meUsYADf3ou0CEBTCD7AAQwwIDlAEyABAYGXOJ7QpBQIIAAhhdufeECICCC3g0FBAA7'
ico=PhotoImage(data=picstring)
root.tk.call('wm', 'iconphoto', root._w, ico)
#root.iconbitmap("finalIcon.ico")
c.config(cursor='none')
##bullet settings
gmode=1
shootspd=110
bulletcolor='black'
blength=50
bdamage=5
bspd=20
eshooting=False
shooting=False
##enemy settings
ex1=8
ebcheck=0
pf3=1
pf2=1
gamem=1
ebulletcolor='black'
scores='You: 0 | AI: 0'
escore=0
eshootspd=15
ex1=0
ey1=0
every10=0
edamage=5
score=0
ex=600
ey=450
elife1=100
exs=10
teys=10
beys=40
ejnum=0
ejcount=2
echeck=False
echeck2=False
egcheck=False
epsafe=False
epsafe2=False
epsafe3=False
ejcheck=False
epcheck=False
epcheck2=False
echeckR=False
echeckL=False
##end enemy settings
spd=6
x=600
y=650
x1=0
y1=0
who='player'
hcolor='wheat2'
jcount=10
jnum=0
gforce=.75
every2=1
every22=1
every222=1
## Boolean variable sets
checkL=False
checkR=False
gcheck=False
jcheck=False
pcheck=False
gsafe=False
psafe=False
psafe2=False
psafe3=False
pcheck2=False
faceup=False
end=False
shooting=True
pause=False
cface=1
lag1=1
life=200
btag=0
def einitial():
    global elife
    global ex1
    global ey1
    global every10
    global ex
    global ey
    global elife1
    global gamem
    ex1=0
    ey1=0
    every10=0
    if gamem==1:
        elife1=100
        emover()
    else:
        elife1=200
    ejnum=0
    echeck2=False
    egcheck=False
    epsafe=False
    epsafe2=False
    epsafe3=False
    ejcheck=False
    epcheck=False
    epcheck2=False
    if ex<650:
        ex=random.randint(650,1250)
    else:
        ex=random.randint(50,650)
    ey=random.randint(200,600)
    cenemy()
    eupdate()
    egravity()
def initialize():
    global restart
    try:
        restart.destroy()
    except:
        None
    global end
    global life
    global x
    global y
    global bcheck
    global every22
    global every2
    global spd
    global jnum
    global elife1
    end=False
    every22=1
    every2=1
    x1=0
    y1=0
    life=200
    who='player'
    hcolor='wheat2'
    btag=0
    jnum=0    
    life=200
    if x<650:
        x=random.randint(650,1250)
    else:
        x=random.randint(50,650)
    y=random.randint(200,600)
    lifebar()
    cplayer()
    update()
    sides()
    gravity()
    gamemode()
## platform animations
c.create_line(150,300,450,300,width=5,fill='brown')
c.create_line(850,300,1150,300,width=5,fill='brown')
c.create_line(0,695,1300,695,width=10,fill='brown')
c.create_line(500,500,800,500,width=5,fill='brown')
c.create_line(0,5,1300,5,width=5,fill='brown')

## Life bar outline
c.create_rectangle(28,28,232,52,width=4)
c.create_rectangle(1272,28,1068,52,width=4)
def lifebar():
    global life
    global end
    global restart
    global elife1
    global score
    global escore
    global scores
    global gamem
    c.delete('scoret')
    if gamem==1:
        scores='You: '+str(score)+'  AI: '+str(escore)
    else:
        scores='Player1: '+str(score)+'  Player2: '+str(escore)
    c.create_text(840,20,fill='black',font=('bold 20'),text=scores,tags='scoret')
    try:
        c.delete('lifebart')
    except:
        None
    if life<=0:
        if gamem==1:
            end=True
            restart=Button(root,text='respawn',command=initialize)
            restart.place(x=600,y=330)
            escore=escore+1
            root.after(500,eupdate)
        else:
            escore=escore+1
            end=True
            root.after(300,initialize)
    if life>150:
        lbc='green'
    elif life>100:
        lbc='chartreuse2'
    elif life>50:
        lbc='DarkOliveGreen1'
    elif life>25:
        lbc='orange'
    else:
        lbc='red'
    if elife1>75:
        elbc='green'
    elif elife1>50:
        elbc='chartreuse2'
    elif elife1>40:
        elbc='DarkOliveGreen1'
    elif elife1>25:
        elbc='orange'
    else:
        elbc='red'
    if end==False:
        c.create_line(30,40,life+30,40,width=20,fill=lbc,tags='lifebart')
    if elife1>0:
        if gamem==1: 
            c.create_line(1070,40,1070+2*elife1,40,width=20,fill=elbc,tags='lifebart')
        else:
            c.create_line(1070,40,1070+elife1,40,width=20,fill=elbc,tags='lifebart')
def cplayer():
    global x
    global y
    mx = root.winfo_pointerx() - root.winfo_rootx()
    my = root.winfo_pointery() - root.winfo_rooty()
    tx1=x-mx
    c.create_oval(x-10,y-10,x+10,y+10,fill=hcolor,tags=who)
    c.create_line(x,y+10,x,y+25,width=3,tags=who)
    c.create_line(x,y+25,x-5,y+40,width=2,tags=who)
    c.create_line(x,y+25,x+5,y+40,width=2,tags=who)
    if gamem==1:
        if tx1>0:
                c.create_line(x-6,y-1,x-3,y-1,width=2,fill='blue',tags=('player','faces'))
                c.create_line(x-3,y+6,x-7,y+6,width=3,tags=('player','faces'))
        else:
                c.create_line(x+6,y-1,x+3,y-1,width=2,fill='blue',tags=('player','faces'))
                c.create_line(x+3,y+6,x+7,y+6,width=3,tags=('player','faces'))
    else:
        if pf2<0:
            c.create_line(x-6,y-1,x-3,y-1,width=2,fill='blue',tags=('player','faces'))
            c.create_line(x-3,y+6,x-7,y+6,width=3,tags=('player','faces'))
            armp=-10
            c.create_line(x,y+15,x-20,y+15,width=3,tags=('gun','player'))
            c.create_line(x+armp,y+19,x-17,y+18,width=3,tags=('gun','player'))
            c.create_line(x,y+15,x+armp,y+18,width=3,tags=('gun','player'))
        else:
            armp=10
            c.create_line(x+6,y-1,x+3,y-1,width=2,fill='blue',tags=('player','faces'))
            c.create_line(x+3,y+6,x+7,y+6,width=3,tags=('player','faces'))
            c.create_line(x,y+15,x+20,y+15,width=3,tags=('gun','player'))
            c.create_line(x+armp,y+19,x+17,y+18,width=3,tags=('gun','player'))
            c.create_line(x,y+15,x+armp,y+18,width=3,tags=('gun','player'))
def sides():
    global x
    global y
    global y1
    global end
    global pause
    if pause==False:
        if end==False:
            if y1<=0:
                if y<15:
                    y1=1
                    root.after(500,gravity)
            if x<0:
                x=1300
                try:
                    c.delete('player')
                except:
                    None
                cplayer()
            if x>1300:
                x=0
                try:
                    c.delete('player')
                except:
                    None
                cplayer()
            root.after(50,sides)
def update():
    global x1
    global y1
    global y
    global x
    global cface
    global faceup
    global face1
    global face2
    global end
    global pause
    if pause==False:
        if end==False:
        ##per frame balancing
        ##    try:
        ##        lag2=lag1
        ##        lag1=time.time()
        ##        lag=(lag1-lag2)*10
        ##    except:
        ##        lag=1
            xforce=x1
            yforce=y1
            y=y+y1
            x=x+xforce
    ##gun position updates
            if gamem==1:
                mx = root.winfo_pointerx() - root.winfo_rootx()
                my = root.winfo_pointery() - root.winfo_rooty()
                tx1=x-mx
                ty1=18+y-my
                try:
                    ang=math.atan(ty1/tx1)
                    by1=(math.sin(ang))
                    bx1=(math.cos(ang))
                except:
                     if ty1>0:
                        by1=-.99
                     else:
                         by1=.99
                     bx1=0
                try:
                    c.delete('gun')
                except:
                    None
                armp=10
                c.move('player',xforce,y1)
                if tx1>0:
                    bx1=-bx1
                    by1=-by1
                    armp=-5
                cface=cface+1
                if cface % 2 ==0:
                    if tx1>0:
                        face1=True
                    else:
                        face1=False
                else:
                    if tx1>0:
                        face2=True
                    else:
                        face2=False
                if cface>4:
                    if face1!=face2:
                        faceup=True
                if faceup==True:
                    try:
                        c.delete('faces')
                    except:
                        None
                    if tx1>0:
                        c.create_line(x-6,y-1,x-3,y-1,width=2,fill='blue',tags=('player','faces'))
                        c.create_line(x-3,y+6,x-7,y+6,width=3,tags=('player','faces'))
                    else:
                        c.create_line(x+6,y-1,x+3,y-1,width=2,fill='blue',tags=('player','faces'))
                        c.create_line(x+3,y+6,x+7,y+6,width=3,tags=('player','faces'))
                    faceup=False
                c.create_line(x,y+15,x+armp,y+19+20*by1,width=3,tags='gun')
                c.create_line(x+armp,y+19+20*by1,x+20*bx1,y+15+20*by1,width=3,tags='gun')
                c.create_line(x,y+15,x+25*bx1,y+15+25*by1,width=3,tags='gun')
            else:
                c.move('player',xforce,y1)
            root.after(20,update)
        else:
            c.delete('player')
##def checkers():
##    global y
##    print(y)
##    root.after(500,checkers)
##root.after(800,checkers)
def gravity():
    global y
    global y1
    global x
    global gcheck
    global jnum
    global hcolor
    global who
    global pcheck
    global psafe
    global gforce
    global psafe2
    global pcheck2
    global psafe3
    if x>145 and x<455 or x>845 and x<1155:
        if y>260:
            if pcheck2==True:
                if x>145 and x<455:
                    if y<260:
                        y1=y1+gforce
                        root.after(30,gravity)
                        pcheck2=True
                    else:
                        y1=0
                        jnum=0
                        gcheck=False
                        c.delete('player')
                        hcolor='wheat2'
                        who='player'
                        y=260
                        cplayer()
                        psafe2=False
                        root.after(30,pgravity2)
                else:
                    if y<260:
                        y1=y1+gforce
                        root.after(30,gravity)
                        pcheck2=True
                    else:
                        y1=0
                        jnum=0
                        gcheck=False
                        c.delete('player')
                        hcolor='wheat2'
                        who='player'
                        y=260
                        cplayer()
                        psafe3=False
                        root.after(30,pgravity3)
            else:
             if x>495 and x<805: ##platform x value check
                if y>460: ##platform y check
                    if pcheck==True:
                        if y<460:
                            y1=y1+gforce
                            root.after(30,gravity)
                            pcheck=True
                            pcheck2=False
                        else:
                            y1=0
                            jnum=0
                            gcheck=False
                            c.delete('player')
                            hcolor='wheat2'
                            who='player'
                            y=460
                            cplayer()
                            psafe=False
                            psafe2=False
                            psafe3=False
                            root.after(30,pgravity)
                    else:
                        if y<650:
                            y1=y1+gforce
                            pcheck2=False
                            root.after(30,gravity)
                        else:
                            y1=0
                            jnum=0
                            gcheck=False
                            c.delete('player')
                            hcolor='wheat2'
                            who='player'
                            y=650
                            cplayer()
                            psafe=False
                            psafe2=False
                            psafe3=False
                else:
                    if y<460:
                        y1=y1+gforce
                        root.after(30,gravity)
                        pcheck=True
                        pcheck2=False
                    else:
                        y1=0
                        jnum=0
                        gcheck=False
                        c.delete('player')
                        hcolor='wheat2'
                        who='player'
                        y=460
                        cplayer()
                        psafe=False
                        psafe2=False
                        psafe3=False
                        root.after(30,pgravity)
             else:
                if y<650:
                    y1=y1+gforce
                    root.after(30,gravity)
                    pcheck=False
                    pcheck2=False
                else:
                    y1=0
                    jnum=0
                    gcheck=False
                    c.delete('player')
                    hcolor='wheat2'
                    who='player'
                    y=650
                    cplayer()
                    psafe=False
                    psafe2=False
                    psafe3=False
        else:
            if x>145 and x<455:
                if y<260:
                    y1=y1+gforce
                    root.after(30,gravity)
                    pcheck2=True
                else:
                    y1=0
                    jnum=0
                    gcheck=False
                    c.delete('player')
                    hcolor='wheat2'
                    who='player'
                    y=260
                    cplayer()
                    psafe=False
                    psafe2=False
                    psafe3=False
                    root.after(30,pgravity2)
            else:
                if y<260:
                    y1=y1+gforce
                    root.after(30,gravity)
                    pcheck2=True
                else:
                    y1=0
                    jnum=0
                    gcheck=False
                    c.delete('player')
                    hcolor='wheat2'
                    who='player'
                    y=260
                    cplayer()
                    psafe=False
                    psafe2=False
                    psafe3=False
                    root.after(30,pgravity3)
    else:
            if x>495 and x<805: ##platform x value check
                if y>460: ##platform y check
                    if pcheck==True:
                        if y<460:
                            y1=y1+gforce
                            root.after(30,gravity)
                            pcheck=True
                            pcheck2=False
                        else:
                            y1=0
                            jnum=0
                            gcheck=False
                            c.delete('player')
                            hcolor='wheat2'
                            who='player'
                            y=460
                            cplayer()
                            psafe=False
                            psafe2=False
                            psafe3=False
                            root.after(30,pgravity)
                    else:
                        if y<650:
                            y1=y1+gforce
                            root.after(30,gravity)
                            pcheck2=False
                        else:
                            y1=0
                            jnum=0
                            gcheck=False
                            c.delete('player')
                            hcolor='wheat2'
                            who='player'
                            y=650
                            cplayer()
                            psafe=False
                            psafe2=False
                            psafe3=False
                else:
                    if y<460:
                        y1=y1+gforce
                        root.after(30,gravity)
                        pcheck=True
                        pcheck2=False
                    else:
                        y1=0
                        jnum=0
                        gcheck=False
                        c.delete('player')
                        hcolor='wheat2'
                        who='player'
                        y=460
                        cplayer()
                        psafe=False
                        psafe2=False
                        psafe3=False
                        root.after(30,pgravity)
            else:
                if y<650:
                    y1=y1+gforce
                    root.after(30,gravity)
                    pcheck=False
                    pcheck2=False
                else:
                    y1=0
                    jnum=0
                    gcheck=False
                    c.delete('player')
                    hcolor='wheat2'
                    who='player'
                    y=650
                    cplayer()
                    psafe=False
                    psafe2=False
                    psafe3=False
def pgravity():
    global x
    global y1
    global psafe
    global jnum
    if x>495 and x<805 and y==460:
        root.after(100,pgravity)
    elif y==460:
        psafe=True
        jnum=1
        root.after(60,gravity)
def pgravity2():
    global x
    global y1
    global psafe2
    global jnum
    if x>145 and x<455 and y==260:
        root.after(100,pgravity2)
    elif y==260:
        psafe2=True
        jnum=1
        root.after(0,gravity)
def pgravity3():
    global x
    global y1
    global psafe3
    global jnum
    if x>845 and x<1155 and y==260:
        root.after(50,pgravity3)
    elif y==260:
        jnum=1
        psafe3=True
        root.after(0,gravity)
def egravity():
    global ey
    global ey1
    global ex
    global egcheck
    global ejnum
    global hcolor
    global echeck
    global echeck2
    global epsafe
    global gforce
    global epsafe2
    global echeck2
    global epsafe3
    global ejcheck
    if ex>145 and ex<455 or ex>845 and ex<1155:
        if ey>260:
            if echeck2==True:
                if ex>145 and ex<455:
                    if ey<260:
                        ey1=ey1+gforce
                        root.after(30,egravity)
                        echeck2=True
                    else:
                        ey1=0
                        ejnum=0
                        egcheck=False
                        c.delete('enemy')
                        hcolor='wheat2'
                        ey=260
                        cenemy()
                        epsafe2=False
                        root.after(30,epgravity2)
                else:
                    if ey<260:
                        ey1=ey1+gforce
                        root.after(30,egravity)
                        echeck2=True
                    else:
                        ey1=0
                        ejnum=0
                        egcheck=False
                        c.delete('enemy')
                        hcolor='wheat2'
                        ey=260
                        cenemy()
                        epsafe3=False
                        root.after(30,epgravity3)
            else:
             if ex>495 and ex<805: ##platform x value check
                if ey>460: ##platform y check
                    if echeck==True:
                        if ey<460:
                            ey1=ey1+gforce
                            root.after(30,egravity)
                            echeck=True
                            echeck2=False
                        else:
                            ey1=0
                            ejnum=0
                            egcheck=False
                            c.delete('enemy')
                            hcolor='wheat2'
                            ey=460
                            cenemy()
                            epsafe=False
                            epsafe2=False
                            epsafe3=False
                            root.after(30,epgravity)
                    else:
                        if ey<650:
                            ey1=ey1+gforce
                            echeck2=False
                            root.after(30,egravity)
                        else:
                            ey1=0
                            ejnum=0
                            egcheck=False
                            c.delete('enemy')
                            hcolor='wheat2'
                            ey=650
                            cenemy()
                            epsafe=False
                            epsafe2=False
                            epsafe3=False
                else:
                    if ey<460:
                        ey1=ey1+gforce
                        root.after(30,egravity)
                        echeck=True
                        echeck2=False
                    else:
                        ey1=0
                        ejnum=0
                        egcheck=False
                        c.delete('enemy')
                        hcolor='wheat2'
                        ey=460
                        cenemy()
                        epsafe=False
                        epsafe2=False
                        epsafe3=False
                        root.after(30,epgravity)
             else:
                if ey<650:
                    ey1=ey1+gforce
                    root.after(30,egravity)
                    echeck=False
                    echeck2=False
                else:
                    ey1=0
                    ejnum=0
                    egcheck=False
                    c.delete('enemy')
                    hcolor='wheat2'
                    ey=650
                    cenemy()
                    epsafe=False
                    epsafe2=False
                    epsafe3=False
        else:
            if ex>145 and ex<455:
                if ey<260:
                    ey1=ey1+gforce
                    root.after(30,egravity)
                    echeck2=True
                else:
                    ey1=0
                    ejnum=0
                    egcheck=False
                    c.delete('enemy')
                    hcolor='wheat2'
                    ey=260
                    cenemy()
                    epsafe=False
                    epsafe2=False
                    epsafe3=False
                    root.after(30,epgravity2)
            else:
                if ey<260:
                    ey1=ey1+gforce
                    root.after(30,egravity)
                    echeck2=True
                else:
                    ey1=0
                    ejnum=0
                    egcheck=False
                    c.delete('enemy')
                    hcolor='wheat2'
                    ey=260
                    cenemy()
                    epsafe=False
                    epsafe2=False
                    epsafe3=False
                    root.after(30,epgravity3)
    else:
            if ex>495 and ex<805: ##platform x value check
                if ey>460: ##platform y check
                    if echeck==True:
                        if ey<460:
                            ey1=ey1+gforce
                            root.after(30,egravity)
                            echeck=True
                            echeck2=False
                        else:
                            ey1=0
                            ejnum=0
                            egcheck=False
                            c.delete('enemy')
                            hcolor='wheat2'
                            ey=460
                            cenemy()
                            epsafe=False
                            epsafe2=False
                            epsafe3=False
                            root.after(30,epgravity)
                    else:
                        if ey<650:
                            ey1=ey1+gforce
                            root.after(30,egravity)
                            echeck2=False
                        else:
                            ey1=0
                            ejnum=0
                            egcheck=False
                            c.delete('enemy')
                            hcolor='wheat2'
                            ey=650
                            cenemy()
                            epsafe=False
                            epsafe2=False
                            epsafe3=False
                else:
                    if ey<460:
                        ey1=ey1+gforce
                        root.after(30,egravity)
                        echeck=True
                        echeck2=False
                    else:
                        ey1=0
                        ejnum=0
                        egcheck=False
                        c.delete('enemy')
                        hcolor='wheat2'
                        ey=460
                        cenemy()
                        epsafe=False
                        epsafe2=False
                        epsafe3=False
                        root.after(30,epgravity)
            else:
                if ey<650:
                    ey1=ey1+gforce
                    root.after(30,egravity)
                    echeck=False
                    echeck2=False
                else:
                    ey1=0
                    ejnum=0
                    egcheck=False
                    c.delete('enemy')
                    hcolor='wheat2'
                    ey=650
                    cenemy()
                    epsafe=False
                    epsafe2=False
                    epsafe3=False
def epgravity():
    global ex
    global ey1
    global epsafe
    global ejnum
    if ex>495 and ex<805 and ey==460:
        root.after(100,epgravity)
    elif ey==460:
        epsafe=True
        ejnum=1
        root.after(60,egravity)
def epgravity2():
    global ex
    global ey1
    global epsafe2
    global ejnum
    if ex>145 and ex<455 and ey==260:
        root.after(100,epgravity2)
    elif ey==260:
        epsafe2=True
        ejnum=1
        root.after(0,egravity)
def epgravity3():
    global ex
    global ey1
    global epsafe3
    global ejnum
    if ex>845 and ex<1155 and ey==260:
        root.after(50,epgravity3)
    elif ey==260:
        ejnum=1
        epsafe3=True
        root.after(0,egravity)
def shooter(event):
    global shooting
    if shooting==False:
        shooting=True
        shoot()
def shoot():
    global x
    global y
    global bcheck
    global bx1
    global by1
    global bx2
    global by2
    global bx3
    global by3
    global bx4
    global by4
    global bx5
    global by5
    global bx6
    global by6
    global bx7
    global by7
    global bx8
    global by8
    global bspd
    global lagcheck
    global shot
    global btag
    global every2
    global every22
    global every222
    global bcheck2
    global bcheck3
    global bcheck4
    global bcheck5
    global bcheck6
    global bcheck7
    global bcheck8
    global bt1
    global bt2
    global bt3
    global bt4
    global bt5
    global bt6
    global bt7
    global bt8
    global shooting
    global end
    global byc1
    global bxc1
    global byc2
    global bxc2
    global byc3
    global bxc3
    global byc4
    global bxc4
    global byc5
    global bxc5
    global byc6
    global bxc6
    global byc7
    global bxc7
    global byc8
    global bxc8
    global pause
    global bulletcolor
    global shootspd
    global gmode
    global gamem
    global pf2
    if pause==False:
        if end==False:
            if shooting==True:
                if gamem==1:
                    tx = root.winfo_pointerx() - root.winfo_rootx()
                    ty = root.winfo_pointery() - root.winfo_rooty()
                    tx1=x-tx
                    ty1=y+18-ty
                    btag=btag+1
                    every222=every222+1
                    if every222%2==0:
                        every22=every22+1
                        if every22%2==0:
                            every2=every2+1
                            if every2 %2==0:
                                bt1=btag
                                try:
                                    ang=math.atan(ty1/tx1)
                                    by1=(math.sin(ang))*bspd
                                    bx1=(math.cos(ang))*bspd
                                except:
                                    if ty1>0:
                                        by1=-50
                                        bx1=0
                                    else:
                                        by1=50
                                        bx1=0
                                if tx1>0:
                                    bx1=-bx1
                                    by1=-by1
                                root.after(10,bullet1)
                                bcheck=0
                                bxc1=x
                                byc1=y+18
                                c.create_line(x,y+15,x+.45*bx1,y+15+.45*by1,width=3,fill=bulletcolor,tags='bullet'+str(bt1))
                            else:
                                bt2=btag
                                try:
                                    ang=math.atan(ty1/tx1)
                                    by2=(math.sin(ang))*bspd
                                    bx2=(math.cos(ang))*bspd
                                except:
                                    if ty1>0:
                                        by2=-50
                                        bx2=0
                                    else:
                                        by2=50
                                        bx2=0
                                if tx1>0:
                                        bx2=-bx2
                                        by2=-by2
                                c.create_line(x,y+15,x+.45*bx2,y+15+.45*by2,width=3,fill=bulletcolor,tags='bullet'+str(bt2))
                                root.after(10,bullet2)
                                bxc2=x
                                byc2=y+18
                                bcheck2=0
                        else:
                            if every2 %2==0:
                                bt3=btag
                                try:
                                    ang=math.atan(ty1/tx1)
                                    by3=(math.sin(ang))*bspd
                                    bx3=(math.cos(ang))*bspd
                                except:
                                    if ty1>0:
                                        by3=-50
                                        bx3=0
                                    else:
                                        by3=50
                                        bx3=0
                                if tx1>0:
                                    bx3=-bx3
                                    by3=-by3
                                root.after(10,bullet3)
                                bxc3=x
                                byc3=y+18
                                bcheck3=0
                                c.create_line(x,y+15,x+.45*bx3,y+15+.45*by3,width=3,fill=bulletcolor,tags='bullet'+str(bt3))
                            else:
                                bt4=btag
                                try:
                                    ang=math.atan(ty1/tx1)
                                    by4=(math.sin(ang))*bspd
                                    bx4=(math.cos(ang))*bspd
                                except:
                                    if ty1>0:
                                        by4=-50
                                        bx4=0
                                    else:
                                        by4=50
                                        bx4=0
                                if tx1>0:
                                        bx4=-bx4
                                        by4=-by4
                                c.create_line(x,y+15,x+.45*bx4,y+15+.45*by4,width=3,fill=bulletcolor,tags='bullet'+str(bt4))
                                root.after(10,bullet4)
                                bxc4=x
                                byc4=y+18
                                bcheck4=0
                    else:
                        if every22%2==0:
                            if every2 %2==0:
                                bt5=btag
                                try:
                                    ang=math.atan(ty1/tx1)
                                    by5=(math.sin(ang))*bspd
                                    bx5=(math.cos(ang))*bspd
                                except:
                                    if ty1>0:
                                        by5=-50
                                        bx5=0
                                    else:
                                        by5=50
                                        bx5=0
                                if tx1>0:
                                        bx5=-bx5
                                        by5=-by5
                                c.create_line(x,y+15,x+.45*bx5,y+15+.45*by5,width=3,fill=bulletcolor,tags='bullet'+str(bt5))
                                root.after(10,bullet5)
                                bxc5=x
                                byc5=y+18
                                bcheck5=0
                            else:
                                bt6=btag
                                try:
                                    ang=math.atan(ty1/tx1)
                                    by6=(math.sin(ang))*bspd
                                    bx6=(math.cos(ang))*bspd
                                except:
                                    if ty1>0:
                                        by6=-60
                                        bx6=0
                                    else:
                                        by6=60
                                        bx6=0
                                if tx1>0:
                                        bx6=-bx6
                                        by6=-by6
                                c.create_line(x,y+16,x+.46*bx6,y+16+.46*by6,width=3,fill=bulletcolor,tags='bullet'+str(bt6))
                                root.after(10,bullet6)
                                bxc6=x
                                byc6=y+18
                                bcheck6=0
                        else:
                            if every2 %2 == 0:
                                bt7=btag
                                try:
                                    ang=math.atan(ty1/tx1)
                                    by7=(math.sin(ang))*bspd
                                    bx7=(math.cos(ang))*bspd
                                except:
                                    if ty1>0:
                                        by7=-70
                                        bx7=0
                                    else:
                                        by7=70
                                        bx7=0
                                if tx1>0:
                                        bx7=-bx7
                                        by7=-by7
                                c.create_line(x,y+17,x+.47*bx7,y+17+.47*by7,width=3,fill=bulletcolor,tags='bullet'+str(bt7))
                                root.after(10,bullet7)
                                bxc7=x
                                byc7=y+18
                                bcheck7=0
                            else:
                                bt8=btag
                                try:
                                    ang=math.atan(ty1/tx1)
                                    by8=(math.sin(ang))*bspd
                                    bx8=(math.cos(ang))*bspd
                                except:
                                    if ty1>0:
                                        by8=-80
                                        bx8=0
                                    else:
                                        by8=80
                                        bx8=0
                                if tx1>0:
                                        bx8=-bx8
                                        by8=-by8
                                c.create_line(x,y+18,x+.48*bx8,y+18+.48*by8,width=3,fill=bulletcolor,tags='bullet'+str(bt8))
                                root.after(10,bullet8)
                                bxc8=x
                                byc8=y+18
                                bcheck8=0
                else:
                    bcheck=0
                    bt1=1
                    bxc1=x
                    byc1=y+15
                    by1=0
                    if pf2>0:
                        c.create_line(x,y+15,x+10,y+15,width=3,fill=bulletcolor,tags='bullet'+str(bt1))
                        bx1=18
                    else:
                        bx1=-18
                        c.create_line(x,y+15,x-10,y+15,width=3,fill=bulletcolor,tags='bullet'+str(bt1))
                    root.after(0,bullet1)
                if gmode==1:
                    root.after(shootspd,shoot)
def cenemy():
    global ex
    global ey
    global pf3
    lifebar()
    c.create_oval(ex-10,ey-10,ex+10,ey+10,fill=hcolor,tags='enemy')
    c.create_line(ex,ey+10,ex,ey+25,width=3,tags='enemy')
    c.create_line(ex,ey+25,ex-5,ey+40,width=2,tags='enemy')
    c.create_line(ex,ey+25,ex+5,ey+40,width=2,tags='enemy')
    if pf3>0:
        c.create_line(ex+6,ey-1,ex+3,ey-1,width=2,fill='blue',tags=('enemy','efaces'))
        c.create_line(ex+3,ey+6,ex+7,ey+6,width=3,tags=('enemy','efaces'))
        armp=10
        c.create_line(ex,ey+15,ex+20,ey+15,width=3,tags=('egun','enemy'))
        c.create_line(ex+armp,ey+19,ex+17,ey+18,width=3,tags=('egun','enemy'))
        c.create_line(ex,ey+15,ex+armp,ey+18,width=3,tags=('egun','enemy'))
    else:
        c.create_line(ex-6,ey-1,ex-3,ey-1,width=2,fill='blue',tags=('enemy','efaces'))
        c.create_line(ex-3,ey+6,ex-7,ey+6,width=3,tags=('enemy','efaces'))
        armp=-10
        c.create_line(ex,ey+15,ex-20,ey+15,width=3,tags=('egun','enemy'))
        c.create_line(ex+armp,ey+19,ex-17,ey+18,width=3,tags=('egun','enemy'))
        c.create_line(ex,ey+15,ex+armp,ey+18,width=3,tags=('egun','enemy'))
def emover():
    global ex1
    global ex
    global ey
    global x
    global y
    global end
    global elife1
    global gamem
    ex1=-ex1
    ejump()
    if end==False and elife1>0:
        if y<0:
            egravity()
        if end ==False and gamem==1:
            root.after(5000,emover)
def eupdate():
    global x
    global y
    global every10
    global ex
    global ey
    global elife1
    global score
    global end
    global pause
    global eshootspd
    global ex1
    global ey1
    if gamem==1:
        if end==False:
            if pause==False:
                if elife1>0:
    #shoot every so many updates:
                    if gamem==1:
                        every10=every10+1
                        if every10%eshootspd==0:
                            eshoot()
                        tx1=ex-x
                        ty1=ey-y
                        try:
                            ang=math.atan(ty1/tx1)
                            by1=(math.sin(ang))
                            bx1=(math.cos(ang))
                        except:
                             if ty1>0:
                                by1=-.99
                             else:
                                 by1=.99
                             bx1=0
                        if tx1>0:
                                bx1=-bx1
                                by1=-by1
                        try:
                            c.delete('egun')
                        except:
                            None
                        ey=ey+ey1
                        ex=ex+ex1
                        c.move('enemy',ex1,ey1)
                        c.create_line(ex,ey+15,ex+25*bx1,ey+15+25*by1,width=3,tags=('enemy','egun'))
                        root.after(30,eupdate)
                    if ex<0:
                        ex=1300
                        try:
                            c.delete('enemy')
                        except:
                            None
                        cenemy()
                    if ex>1300:
                        ex=0
                        try:
                            c.delete('enemy')
                        except:
                            None
                        cenemy()
                else:
                    score=score+1
                    try:
                            c.delete('enemy')
                    except:
                            None
    else:
         if elife1>0:
            ey=ey+ey1
            ex=ex+ex1
            c.move('enemy',ex1,ey1)
            if ex<0:
                ex=1300
                try:
                    c.delete('enemy')
                except:
                    None
                cenemy()
            if ex>1300:
                ex=0
                try:
                    c.delete('enemy')
                except:
                    None
                cenemy()
            root.after(20,eupdate)
         else:
                    score=score+1
                    try:
                            c.delete('enemy')
                    except:
                            None
def eshooter(event):
    global eshooting
    if eshooting==False:
        eshooting=True
        eshoot()
def eunshoot(event):
    global eshooting
    eshooting=False
def eshoot():
    global ex
    global ey
    global x
    global y
    global bxe
    global bye
    global ebx
    global eby
    global ebcheck
    global ebulletcolor
    global gamem
    global pf3
    global eshooting
    global shootspd
    if gamem==1:
        tx1=ex-x
        ty1=ey-y
        try:
            ang=math.atan(ty1/tx1)
            bye=(math.sin(ang))*20
            bxe=(math.cos(ang))*20
        except:
             if ty1>0:
                bye=-.99
             else:
                 bye=.99
                 bxe=0
        if tx1>0:
                    bxe=-bxe
                    bye=-bye
        ebx=ex
        eby=ey+18
        c.create_line(ex,ey+18,ex+.48*bxe,ey+18+.48*bye,width=3,fill=ebulletcolor,tags='ebullet')
        ebcheck=0
        ebullet1()
    else:
        if eshooting==True:
            bye=0
            ebcheck=0
            ebx=ex
            eby=ey+15
            if pf3>0:
                c.create_line(ex,ey+15,ex+10,ey+15,width=3,fill=bulletcolor,tags='ebullet')
                bxe=18
            else:
                bxe=-18
                c.create_line(ex,ey+15,ex-10,ey+15,width=3,fill=bulletcolor,tags='ebullet')
            ebullet1()
            root.after(shootspd,eshoot)
        
def ejump():
    global ey1
    global egcheck
    global ejcount
    global ejcheck
    global ejnum
    global ey
    global epsafe
    global epsafe2
    global epsafe3
    ey=ey-1
    if ejnum<ejcount:
        ey1=-15
        ejnum=ejnum+1
        if egcheck==False and epsafe==False and epsafe2==False and epsafe3==False:
            root.after(30,egravity)
            egcheck=True
def ejumpt(event):
    global ey1
    global egcheck
    global ejcount
    global ejcheck
    global ejnum
    global ey
    global epsafe
    global epsafe2
    global epsafe3
    ey=ey-1
    if ejnum<ejcount:
        ey1=-15
        ejnum=ejnum+1
        if egcheck==False and epsafe==False and epsafe2==False and epsafe3==False:
            root.after(30,egravity)
            egcheck=True
def ebullet1():
    global x
    global y
    global blength
    global bxe
    global bye
    global ebx
    global eby
    global ebcheck
    ebx=ebx+bxe
    eby=eby+bye
    if ebx+10>x and ebx-10<x and eby+10>y and eby-40<y:
        damage()
        c.delete('ebullet')
    else:
        c.move('ebullet',bxe,bye)
        if ebcheck<blength:
            ebcheck=ebcheck+1
            root.after(10,ebullet1)
        else:
            c.delete('ebullet')
            ebcheck=0
def damage():
    global life
    global edamage
    life=life-edamage
    lifebar()
def edamage1():
    global bdamage
    global elife1
    elife1=elife1-bdamage
    lifebar()
    if elife1<1:
        c.delete('enemy')
        root.after(60,einitial)
def unshoot(event):
    global shooting
    shooting=False
def bullet1():
    global bcheck
    global bx1
    global by1
    global shot
    global bt1
    global byc1
    global bxc1
    global ex
    global ey
    global exs
    global eys
    global blength
    bxc1=bxc1+bx1
    byc1=byc1+by1
    if bxc1+exs>ex and bxc1-exs<ex and byc1+teys>ey and byc1-beys<ey:
        edamage1()
        c.delete('bullet'+str(+bt1))
    else:
        c.move('bullet'+str(bt1),bx1,by1)
        if bcheck<blength:
            bcheck=bcheck+1
            root.after(10,bullet1)
        else:
            c.delete('bullet'+str(bt1))
            bcheck=0
def bullet2():
    global bcheck2
    global bx2
    global by2
    global shot
    global bt2
    global bxc2
    global byc2
    global ex
    global ey
    global exs
    global eys
    global blength
    bxc2=bxc2+bx2
    byc2=byc2+by2
    if bxc2+exs>ex and bxc2-exs<ex and byc2+teys>ey and byc2-beys<ey:
        edamage1()
        c.delete('bullet'+str(+bt2))
    else:
        c.move('bullet'+str(+bt2),bx2,by2)
        if bcheck2<blength:
            bcheck2=bcheck2+1
            root.after(10,bullet2)
        else:
            c.delete('bullet'+str(bt2))
            bcheck2=0
def bullet3():
    global bcheck3
    global bx3
    global by3
    global shot
    global bt3
    global bxc3
    global byc3
    global ex
    global ey
    global exs
    global eys
    global blength
    bxc3=bxc3+bx3
    byc3=byc3+by3
    if bxc3+exs>ex and bxc3-exs<ex and byc3+teys>ey and byc3-beys<ey:
        edamage1()
        c.delete('bullet'+str(+bt3))
    else:
        c.move('bullet'+str(+bt3),bx3,by3)
        if bcheck3<blength:
            bcheck3=bcheck3+1
            root.after(10,bullet3)
        else:
            c.delete('bullet'+str(bt3))
            bcheck3=0
def bullet4():
    global bcheck4
    global bx4
    global by4
    global shot
    global bt3
    global bxc4
    global byc4
    global ex
    global ey
    global exs
    global eys
    global blength
    bxc4=bxc4+bx4
    byc4=byc4+by4
    if bxc4+exs>ex and bxc4-exs<ex and byc4+teys>ey and byc4-beys<ey:
        edamage1()
        c.delete('bullet'+str(+bt4))
    else:
        c.move('bullet'+str(+bt4),bx4,by4)
        if bcheck4<blength:
            bcheck4=bcheck4+1
            root.after(10,bullet4)
        else:
            c.delete('bullet'+str(bt4))
            bcheck4=0
def bullet5():
    global bcheck5
    global bx5
    global by5
    global shot
    global bt5
    global bxc5
    global byc5
    global ex
    global ey
    global exs
    global eys
    global blength
    bxc5=bxc5+bx5
    byc5=byc5+by5
    if bxc5+exs>ex and bxc5-exs<ex and byc5+teys>ey and byc5-beys<ey:
        edamage1()
        c.delete('bullet'+str(+bt5))
    else:
        c.move('bullet'+str(+bt5),bx5,by5)
        if bcheck5<blength:
            bcheck5=bcheck5+1
            root.after(10,bullet5)
        else:
            c.delete('bullet'+str(bt5))
            bcheck5=0
def bullet6():
    global bcheck6
    global bx6
    global by6
    global shot
    global bt6
    global bxc6
    global byc6
    global ex
    global ey
    global exs
    global eys
    global blength
    bxc6=bxc6+bx6
    byc6=byc6+by6
    if bxc6+exs>ex and bxc6-exs<ex and byc6+teys>ey and byc6-beys<ey:
        edamage1()
        c.delete('bullet'+str(+bt6))
    else:
        c.move('bullet'+str(+bt6),bx6,by6)
        if bcheck6<blength:
            bcheck6=bcheck6+1
            root.after(10,bullet6)
        else:
            c.delete('bullet'+str(bt6))
            bcheck6=0
def bullet7():
    global bcheck7
    global bx7
    global by7
    global shot
    global bt7
    global bxc7
    global byc7
    global ex
    global ey
    global exs
    global eys
    global blength
    bxc7=bxc7+bx7
    byc7=byc7+by7
    if bxc7+exs>ex and bxc7-exs<ex and byc7+teys>ey and byc7-beys<ey:
        edamage1()
        c.delete('bullet'+str(+bt7))
    else:
        c.move('bullet'+str(+bt7),bx7,by7)
        if bcheck7<blength:
            bcheck7=bcheck7+1
            root.after(10,bullet7)
        else:
            c.delete('bullet'+str(bt7))
            bcheck7=0
def bullet8():
    global bcheck8
    global bx8
    global by8
    global shot
    global bt8
    global bxc8
    global byc8
    global ex
    global ey
    global exs
    global eys
    global blength
    bxc8=bxc8+bx8
    byc8=byc8+by8
    if bxc8+exs>ex and bxc8-exs<ex and byc8+teys>ey and byc8-beys<ey:
        edamage1()
        c.delete('bullet'+str(+bt8))
    else:
        c.move('bullet'+str(+bt8),bx8,by8)
        if bcheck8<blength:
            bcheck8=bcheck8+1
            root.after(10,bullet8)
        else:
            c.delete('bullet'+str(bt8))
            bcheck8=0
def up1(event):
    global y1
    global gcheck
    global jcheck
    global jcount
    global jnum
    global y
    global psafe
    global psafe2
    global psafe3
    y=y-1
    if jcheck==False:
     if jnum<jcount:
        y1=-15
        jnum=jnum+1
        if gcheck==False and psafe==False and psafe2==False and psafe3==False:
            root.after(30,gravity)
        gcheck=True
        jcheck=True
def up2(event):
    global jcheck
    jcheck=False
def left1(event):
    global x1
    global spd
    global checkL
    global checkR
    global gamem
    global pf2
    if gamem==2 and checkR==False:
        pf2=-1
        try:
            c.delete('gun')
            c.delete('faces')
        except:
            None
        c.create_line(x-6,y-1,x-3,y-1,width=2,fill='blue',tags=('player','faces'))
        c.create_line(x-3,y+6,x-7,y+6,width=3,tags=('player','faces'))
        armp=-10
        c.create_line(x,y+15,x-20,y+15,width=3,tags=('gun','player'))
        c.create_line(x+armp,y+19,x-17,y+18,width=3,tags=('gun','player'))
        c.create_line(x,y+15,x+armp,y+18,width=3,tags=('gun','player'))
    checkL=True
    if checkR==True:
        x1=0
    else:
        x1=-spd
def left2(event):
    global x1
    global spd
    global checkL
    global checkR
    global pf2
    checkL=False
    if checkR==False:
        x1=0
    else:
        pf2=1
        x1=spd
        try:
            c.delete('gun')
            c.delete('faces')
        except:
            None
        c.create_line(x+6,y-1,x+3,y-1,width=2,fill='blue',tags=('player','faces'))
        c.create_line(x+3,y+6,x+7,y+6,width=3,tags=('player','faces'))
        armp=10
        c.create_line(x,y+15,x+20,y+15,width=3,tags=('gun','player'))
        c.create_line(x+armp,y+19,x+17,y+18,width=3,tags=('gun','player'))
        c.create_line(x,y+15,x+armp,y+18,width=3,tags=('gun','player'))
def right1(event):
    global x1
    global spd
    global checkR
    global checkL
    global pf2
    if gamem==2:
        pf2=1
        try:
            c.delete('gun')
            c.delete('faces')
        except:
            None
        c.create_line(x+6,y-1,x+3,y-1,width=2,fill='blue',tags=('player','faces'))
        c.create_line(x+3,y+6,x+7,y+6,width=3,tags=('player','faces'))
        armp=10
        c.create_line(x,y+15,x+20,y+15,width=3,tags=('gun','player'))
        c.create_line(x+armp,y+19,x+17,y+18,width=3,tags=('gun','player'))
        c.create_line(x,y+15,x+armp,y+18,width=3,tags=('gun','player'))
    checkR=True
    if checkL==True:
        x1=0
    else:
        x1=spd
def right2(event):
    global x1
    global spd
    global checkR
    global checkL
    global pf2
    checkR=False
    if checkL==False:
        x1=0
    else:
        pf2=-1
        x1=-spd
        try:
            c.delete('gun')
            c.delete('faces')
        except:
            None
        c.create_line(x-6,y-1,x-3,y-1,width=2,fill='blue',tags=('player','faces'))
        c.create_line(x-3,y+6,x-7,y+6,width=3,tags=('player','faces'))
        armp=-10
        c.create_line(x,y+15,x-20,y+15,width=3,tags=('gun','player'))
        c.create_line(x+armp,y+19,x-17,y+18,width=3,tags=('gun','player'))
        c.create_line(x,y+15,x+armp,y+18,width=3,tags=('gun','player'))
def eleft1(event):
    global ex1
    global spd
    global echeckL
    global echeckR
    global pf3
    pf3=-1
    try:
            c.delete('egun')
            c.delete('efaces')
    except:
            None
    c.create_line(ex-6,ey-1,ex-3,ey-1,width=2,fill='blue',tags=('enemy','efaces'))
    c.create_line(ex-3,ey+6,ex-7,ey+6,width=3,tags=('enemy','efaces'))
    armp=-10
    c.create_line(ex,ey+15,ex-20,ey+15,width=3,tags=('egun','enemy'))
    c.create_line(ex+armp,ey+19,ex-17,ey+18,width=3,tags=('egun','enemy'))
    c.create_line(ex,ey+15,ex+armp,ey+18,width=3,tags=('egun','enemy'))
    echeckL=True
    if echeckR==True:
        ex1=0
    else:
        ex1=-spd
def eleft2(event):
    global ex1
    global spd
    global echeckL
    global echeckR
    echeckL=False
    if echeckR==False:
        ex1=0
    else:
        ex1=spd
        pf3=1
        try:
                c.delete('egun')
                c.delete('efaces')
        except:
                None
        c.create_line(ex+6,ey-1,ex+3,ey-1,width=2,fill='blue',tags=('enemy','efaces'))
        c.create_line(ex+3,ey+6,ex+7,ey+6,width=3,tags=('enemy','efaces'))
        armp=10
        c.create_line(ex,ey+15,ex+20,ey+15,width=3,tags=('egun','enemy'))
        c.create_line(ex+armp,ey+19,ex+17,ey+18,width=3,tags=('egun','enemy'))
        c.create_line(ex,ey+15,ex+armp,ey+18,width=3,tags=('egun','enemy'))
def eright1(event):
    global ex1
    global spd
    global echeckR
    global echeckL
    global pf3
    pf3=1
    try:
            c.delete('egun')
            c.delete('efaces')
    except:
            None
    c.create_line(ex+6,ey-1,ex+3,ey-1,width=2,fill='blue',tags=('enemy','efaces'))
    c.create_line(ex+3,ey+6,ex+7,ey+6,width=3,tags=('enemy','efaces'))
    armp=10
    c.create_line(ex,ey+15,ex+20,ey+15,width=3,tags=('egun','enemy'))
    c.create_line(ex+armp,ey+19,ex+17,ey+18,width=3,tags=('egun','enemy'))
    c.create_line(ex,ey+15,ex+armp,ey+18,width=3,tags=('egun','enemy'))
    echeckR=True
    if echeckL==True:
        ex1=0
    else:
        ex1=spd
def eright2(event):
    global ex1
    global spd
    global echeckR
    global echeckL
    echeckR=False
    if echeckL==False:
        ex1=0
    else:
        ex1=-spd
        pf3=-1
        try:
                c.delete('egun')
                c.delete('efaces')
        except:
                None
        c.create_line(ex-6,ey-1,ex-3,ey-1,width=2,fill='blue',tags=('enemy','efaces'))
        c.create_line(ex-3,ey+6,ex-7,ey+6,width=3,tags=('enemy','efaces'))
        armp=-10
        c.create_line(ex,ey+15,ex-20,ey+15,width=3,tags=('egun','enemy'))
        c.create_line(ex+armp,ey+19,ex-17,ey+18,width=3,tags=('egun','enemy'))
        c.create_line(ex,ey+15,ex+armp,ey+18,width=3,tags=('egun','enemy'))
def gamemode1():
    global gamem
    gamem=1
    gamemode()
def gamemode2():
    global gamem
    gamem=2
    gamemode()
def gamemode():
    global gamem
    if gamem==2:
        global shootspd
        global blength
        global bdamage
        global edamage
        shootspd=200
        blength=40
        bdamage=20
        edamage=bdamage
        c.config(cursor='arrow')
        root.bind('<MouseWheel>',none)
        root.bind('<ButtonPress-1>',none)
        root.bind('<ButtonRelease-1>',none)
        root.bind('<Motion>',none)
        root.bind('<KeyPress-w>',none)
        root.bind('<KeyRelease-w>',none)
        root.bind('<KeyPress-a>',none)
        root.bind('<KeyRelease-a>',none)
        root.bind('<KeyPress-d>',none)
        root.bind('<KeyRelease-d>',none)
        root.bind('<KeyPress-W>',none)
        root.bind('<KeyRelease-W>',none)
        root.bind('<KeyPress-A>',none)
        root.bind('<KeyRelease-A>',none)
        root.bind('<KeyPress-D>',none)
        root.bind('<KeyRelease-D>',none)
        root.bind('<e>',ejumpt)
        root.bind('<KeyPress-f>',eright1)
        root.bind('<KeyRelease-f>',eright2)
        root.bind('<KeyPress-s>',eleft1)
        root.bind('<KeyRelease-s>',eleft2)
        root.bind('<KeyPress-.>',shooter)
        root.bind('<KeyRelease-.>',unshoot)
        root.bind('<KeyPress-2>',eshooter)
        root.bind('<KeyRelease-2>',eunshoot)
    if gamem==1:
        edamage=10
        c.config(cursor='none')
        root.bind('<KeyPress-m>',none)
        root.bind('<KeyRelease-m>',none)
        root.bind('<KeyPress-2>',none)
        root.bind('<KeyRelease-2>',none)
        root.bind('<e>',none)
        root.bind('<KeyPress-f>',none)
        root.bind('<KeyRelease-f>',none)
        root.bind('<KeyPress-s>',none)
        root.bind('<KeyRelease-s>',none)
        root.bind('<KeyPress-Up>',up1)
        root.bind('<KeyRelease-Up>',up2)
        root.bind('<KeyPress-Left>',left1)
        root.bind('<KeyRelease-Left>',left2)
        root.bind('<KeyPress-Right>',right1)
        root.bind('<KeyRelease-Right>',right2)
        root.bind('<KeyPress-w>',up1)
        root.bind('<KeyRelease-w>',up2)
        root.bind('<KeyPress-a>',left1)
        root.bind('<KeyRelease-a>',left2)
        root.bind('<KeyPress-d>',right1)
        root.bind('<KeyRelease-d>',right2)
        root.bind('<KeyPress-W>',up1)
        root.bind('<KeyRelease-W>',up2)
        root.bind('<KeyPress-A>',left1)
        root.bind('<KeyRelease-A>',left2)
        root.bind('<KeyPress-D>',right1)
        root.bind('<KeyRelease-D>',right2)
        root.bind('<ButtonPress-1>',shooter)
        root.bind('<ButtonRelease-1>',unshoot)
        root.bind('<Motion>',aim)
        root.bind('<MouseWheel>',wselect)
def none(event):
    None
def aim(event):
##    global bx1
##    global by1
##    try:
##        print(bx1,by1)
##    except:
##        None
    global pause
    if pause==False:
        cx,cy=event.x,event.y
        try:
            c.delete('crosshair')
        except:
            None
        c.create_line(cx,cy-5,cx,cy+5,tags='crosshair')
        c.create_line(cx-5,cy,cx+5,cy,tags='crosshair')
def pausecmd():
    global pause
    global pframe
    global menu
    global pausebtn
    hgt=(root.winfo_height())
    wdt=(root.winfo_width())
    pause=True
    pausebtn.destroy()
    menu=Menu(root,bg='black',fg='green',activebackground='black',activeforeground='white')
    root.config(menu=menu)
    menu.add_command(label='Resume',command=resume)
    gamemode=Menu(menu,bg='black',fg='green',activebackground='black',activeforeground='white')
    menu.add_cascade(label='Gamemode',menu=gamemode)
    gamemode.add_command(label='1 Player',command=gamemode1)
    gamemode.add_command(label='2 Player',command=gamemode2)
    c.config(cursor='arrow')
def resume():
    global pframe
    global pause
    global x
    global y
    global menu
    global pausebtn
    pausebtn=Button(root,bg=cback,activeforeground='green',activebackground='black',text='Pause',command=pausecmd)
    pausebtn.place(x=650,y=10)
    pause=False
    menu.destroy()
    c.config(cursor='none')
    initialize()
    einitial()
#enemy test bindings
##def eright(event):
##    global ex1
##    ex1=10
##def eright1(event):
##    global ex1
##    ex1=0
##def eleft(event):
##    global ex1
##    ex1=-10
##def eleft1(event):
##    global ex1
##    ex1=0
def sniper(event):
    global bulletcolor
    global blength
    global bdamage
    global gmode
    bulletcolor='black'
    blength=60
    bdamage=25
    gmode=2
def regulargun(event):
    global shootspd
    global bulletcolor
    global blength
    global bdamage
    global bspd
    global gmode
    shootspd=100
    bulletcolor='black'
    blength=25
    bdamage=5
    gmode=1
wsel=0
def wselect(event):
    global wsel
    if event.delta>0:
        wsel=wsel+1
    if event.delta<0:
        wsel=wsel-1
    if wsel>2:
        wsel=1
    if wsel<1:
        wsel=2
    if wsel==1:
        regulargun(event)
    if wsel==2:
        sniper(event)
c.create_text(800,20,fill='black',font=('bold 20'),text=scores,tags='scoret')
pausebtn=Button(root,bg=cback,activeforeground='green',activebackground='black',text='Pause',command=pausecmd)
pausebtn.place(x=650,y=10)
root.bind('<KeyPress-Up>',up1)
root.bind('<KeyRelease-Up>',up2)
root.bind('<KeyPress-Left>',left1)
root.bind('<KeyRelease-Left>',left2)
root.bind('<KeyPress-Right>',right1)
root.bind('<KeyRelease-Right>',right2)
root.bind('<KeyPress-w>',up1)
root.bind('<KeyRelease-w>',up2)
root.bind('<KeyPress-a>',left1)
root.bind('<KeyRelease-a>',left2)
root.bind('<KeyPress-d>',right1)
root.bind('<KeyRelease-d>',right2)
root.bind('<KeyPress-W>',up1)
root.bind('<KeyRelease-W>',up2)
root.bind('<KeyPress-A>',left1)
root.bind('<KeyRelease-A>',left2)
root.bind('<KeyPress-D>',right1)
root.bind('<KeyRelease-D>',right2)
root.bind('<ButtonPress-1>',shooter)
root.bind('<ButtonRelease-1>',unshoot)
root.bind('<Motion>',aim)
root.bind('<MouseWheel>',wselect)
einitial()
initialize()
root.mainloop()
