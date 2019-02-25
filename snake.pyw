from tkinter import*
from random import*
import time
import os
import os.path
from PIL import Image,ImageTk
from io import BytesIO
import base64
root=Tk()
c=Canvas(master=root,bg='black',width=1200,height=680)
c.pack()
c.create_text(600,600,text='Press Enter To Start',fill='blue',font=('bold 85'))
root.title('snake')
appleamount=10
win=1
applenum=1
t=1
pt=1
s=10
xx=15
pxx=15
hx=[]
hy=[]
phx=[]
phy=[]
ax,ay,ax2,ay2,ax3,ay3,ax4,ay4=0,0,0,0,0,0,0,0
pp=0
pp2=0
speed=80
gmodecc=1
solid=True
hx.append(1)
hy.append(1)
phx.append(1)
phy.append(1)
gmode=1
gmodecc=1
vert=False
dright=True
high=False
screencheck=True
selfbodyon=True
shead='classic'
burgerstring=(b'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')
picstring=b'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'
im = Image.open(BytesIO(base64.b64decode(picstring)))
uhead=ImageTk.PhotoImage(image=im)
im=im.rotate(90)
lhead=ImageTk.PhotoImage(image=im)
im=im.rotate(90)
dhead=ImageTk.PhotoImage(image=im)
im=im.rotate(90)
rhead=ImageTk.PhotoImage(image=im)
ico=PhotoImage(data=picstring)
im = Image.open(BytesIO(base64.b64decode(burgerstring)))
im2=im
im=im.resize((50,50))
uburger=ImageTk.PhotoImage(image=im)
im=im.rotate(90)
lburger=ImageTk.PhotoImage(image=im)
im=im.rotate(90)
dburger=ImageTk.PhotoImage(image=im)
im=im.rotate(90)
rburger=ImageTk.PhotoImage(image=im)
im=im2.resize((25,30))
ubs=ImageTk.PhotoImage(image=im)
im=im.rotate(90)
lbs=ImageTk.PhotoImage(image=im)
im=im.rotate(90)
dbs=ImageTk.PhotoImage(image=im)
im=im.rotate(90)
rbs=ImageTk.PhotoImage(image=im)
root.tk.call('wm', 'iconphoto', root._w, ico)
fillc='green'
outc='red'
shape='square'
poutc='blue'
pfillc='red'
wordvar=0
wordc=True
def word():
      c.create_text(600,100,text='Snake',font=('bold 100'),fill='blue')
##    global wordvar
##    global wordc
##    if wordc==True:
##        #c.delete('word')
##        if wordvar==0:
##            c.create_text(600,100,text='Snake',font=('bold 100'),fill='purple')
##        elif wordvar==1:
##            c.create_text(600,100,text='Snake',font=('bold 100'),fill='blue')
##        elif wordvar==2:
##            c.create_text(600,100,text='Snake',font=('bold 100'),fill='green')
##        elif wordvar==3:
##            c.create_text(600,100,text='Snake',font=('bold 100'),fill='yellow')
##        elif wordvar==4:
##            c.create_text(600,100,text='Snake',font=('bold 100'),fill='orange')
##        elif wordvar==5:
##            c.create_text(600,100,text='Snake',font=('bold 100'),fill='red')
##        else:
##            wordvar=-1
##        wordvar+=1
##        if wordvar==0:
##            word()
##        else:
##            #None
##            root.after(1000,word)
word()
def csave():
    global saveb
    f=open('snake.save1','w')
    f.write('--~`0,--~`0,--~`0,--~`0,--~`0,square~`-1,110~`-2,False~`-3,classic~`-4,1~`-5,2~`-6')
    try:
        saveb.destroy()
    except:
        None
if os.path.isfile('snake.save1'):
      None
else:
    csave()
stc1=4
stc2=3
stc3=2
stc4=1
stc8=16
startv=False
sim=uhead
psim=uhead
def startscreen():
    global xx
    global pxx
    global x
    global y
    global px
    global py
    global x1
    global y1
    global px1
    global py1
    global pvert
    global vert
    global pddown
    global pdright
    global ddown
    global dright
    global safe
    global startv
    global stc1
    global stc2
    global stc3
    global stc4
    global stc8
    global shape
    global shead
    global gmode
    global uhead
    global dhead
    global rhead
    global lhead
    global sim
    global psim
    if startv==False:
        gmode=2
        pxx=25
        xx=25
        safe=True
        if stc8%16==0:
            if stc1%4==0:
                if shead=='face':
                    psim,sim=rhead,lhead
                else:
                    psim,sim=rburger,lburger
                shape='square'
                pvert=False
                vert=False
                ddown=False
                pddown=False
                dright=False
                pdright=True
                x=660
                y=200
                y1=0
                x1=-20
                px=500
                py=520
                px1=20
                py1=0
            if stc2%4==0:
                if shead=='face':
                    psim,sim=uhead,dhead
                else:
                    psim,sim=uburger,dburger
                shape='diamond'
                pvert=True
                vert=True
                ddown=True
                pddown=False
                dright=False
                pdright=False
                x,y,px,py=340,200,820,520
                y1=20
                x1=0
                px1=0
                py1=-20
            if stc3%4==0:
                if shead=='face':
                    psim,sim=lhead,rhead
                else:
                    psim,sim=lburger,rburger
                shape='triangle'
                pvert=False
                vert=False
                ddown=False
                pddown=False
                dright=True
                pdright=False
                x,y,px,py=340, 520, 820, 200
                y1=0
                x1=20
                px1=-20
                py1=0
            if stc4%4==0:
                if shead=='face':
                    psim,sim=dhead,uhead
                else:
                    psim,sim=dburger,uburger
                shape='circle'
                pvert=True
                vert=True
                ddown=False
                pddown=True
                dright=False
                pdright=False
                x,y,px,py=660, 520, 500, 200,
                y1=-20
                x1=0
                px1=0
                py1=20
            stc1+=1
            stc2+=1
            stc3+=1
            stc4+=1
        stc8+=1
        gamecall()
        pgamecall()
        root.after(40,startscreen)
root.after(0,startscreen)
def c1():
    global pp
    global t
    global x
    global y
    global s
    global hx
    global hy
    global xx
    global vert
    global pic
    global sp
    global im
    global shape
    global fillc
    global outc
    global sim
    global ddown
    global dright
    global shead
    global ubs
    global lbs
    global dbs
    global rbs
    hx.append(x)
    hy.append(y)
    if xx==len(hx):
     del hx[0]
     del hy[0]
    try:
        c.delete('head')
    except:
        None
    h=15
    try:
        c.delete(sp)
    except:
        None
    if shape=='circle':
        c.create_oval(x-s,y-s,x+s,y+s,outline=outc,fill=fillc,tags='l'+str(t))
    elif shape=='diamond':
        c.create_polygon(x-s,y,x,y+s,x+s,y,x,y-s,x-s,y,outline=outc,fill=fillc,tags='l'+str(t))
    elif shape=='square':
        c.create_rectangle(x-s,y-s,x+s,y+s,outline=outc,fill=fillc,tags='l'+str(t))
    elif shape=='triangle':
        if vert==True:
            if ddown==True:
                c.create_polygon(x-s,y-5,x,y+s+5,x+s,y-5,x-s,y-5,outline=outc,fill=fillc,tags='l'+str(t))
            else:
                c.create_polygon(x-s,y+5,x,y-s-5,x+s,y+5,x-s,y+5,outline=outc,fill=fillc,tags='l'+str(t))
        else:
            if dright==True:
                c.create_polygon(x-5,y-s,x+s+5,y,x-5,y+s,x-5,y-s,outline=outc,fill=fillc,tags='l'+str(t))
            else:
                c.create_polygon(x+5,y-s,x-s-5,y,x+5,y+s,x+5,y-s,outline=outc,fill=fillc,tags='l'+str(t))
    elif shape=='burger':
        if vert==True:
            if ddown==True:
                c.create_image(x,y, image=dbs,tags='l'+str(t))
            else:
                c.create_image(x,y, image=ubs,tags='l'+str(t))
        else:
            if dright==True:
                c.create_image(x,y, image=rbs,tags='l'+str(t))
            else:
                c.create_image(x,y, image=lbs,tags='l'+str(t))
    if shead=='face' or shead=='burger':
        sp=c.create_image(x,y, image=sim)
    elif shead=='classic':
        c.create_polygon(x-h,y-h,x+h,y-h,x+h,y+h,x-h,y+h,x-h,y-h,outline='green',fill='black',tags='head')
        if vert==True:
            c.create_oval(x-12,y-5,x-4,y+5,fill='blue',tags='head')
            c.create_oval(x+12,y+5,x+4,y-5,fill='blue',tags='head')
        else:
            c.create_oval(x+5,y-12,x-5,y-4,fill='blue',tags='head')
            c.create_oval(x+5,y+12,x-5,y+4,fill='blue',tags='head')
def pc1():
    global pp2
    global pt
    global px
    global py
    global s
    global phx
    global phy
    global pxx
    global pvert
    global pic
    global psp
    global shape
    global pfillc
    global poutc
    global psim
    global pddown
    global pdright
    global shead
    global ubs
    global lbs
    global dbs
    global rbs
    phx.append(px)
    phy.append(py)
    if pxx==len(phx):
     del phx[0]
     del phy[0]
    try:
        c.delete('phead')
    except:
        None
    h=15
    try:
        c.delete(psp)
    except:
        None
    if shape=='circle':
        c.create_oval(px-s,py-s,px+s,py+s,outline=poutc,fill=pfillc,tags='pl'+str(pt))
    elif shape=='diamond':
        c.create_polygon(px-s,py,px,py+s,px+s,py,px,py-s,px-s,py,outline=poutc,fill=pfillc,tags='pl'+str(pt))
    elif shape=='square':
        c.create_rectangle(px-s,py-s,px+s,py+s,outline=poutc,fill=pfillc,tags='pl'+str(pt))
    elif shape=='triangle':
        if pvert==True:
            if pddown==True:
                c.create_polygon(px-s,py-5,px,py+s+5,px+s,py-5,px-s,py-5,outline=poutc,fill=pfillc,tags='pl'+str(pt))
            else:
                c.create_polygon(px-s,py+5,px,py-s-5,px+s,py+5,px-s,py+5,outline=poutc,fill=pfillc,tags='pl'+str(pt))
        else:
            if pdright==True:
                c.create_polygon(px-5,py-s,px+s+5,py,px-5,py+s,px-5,py-s,outline=poutc,fill=pfillc,tags='pl'+str(pt))
            else:
                c.create_polygon(px+5,py-s,px-s-5,py,px+5,py+s,px+5,py-s,outline=poutc,fill=pfillc,tags='pl'+str(pt))
    elif shape=='burger':
        if pvert==True:
            if pddown==True:
                c.create_image(px,py, image=dbs,tags='pl'+str(pt))
            else:
                c.create_image(px,py, image=ubs,tags='pl'+str(pt))
        else:
            if pdright==True:
                c.create_image(px,py, image=rbs,tags='pl'+str(pt))
            else:
                c.create_image(px,py, image=lbs,tags='pl'+str(pt))
    if shead=='face' or shead=='burger':
        psp=c.create_image(px,py, image=psim)
    elif shead=='classic':
        c.create_polygon(px-h,py-h,px+h,py-h,px+h,py+h,px-h,py+h,px-h,py-h,outline=poutc,fill='black',tags='phead')
        if pvert==True:
            c.create_oval(px-12,py-5,px-4,py+5,fill='blue',tags='phead')
            c.create_oval(px+12,py+5,px+4,py-5,fill='blue',tags='phead')
        else:
            c.create_oval(px+5,py-12,px-5,py-4,fill='blue',tags='phead')
            c.create_oval(px+5,py+12,px-5,py+4,fill='blue',tags='phead')
def start(event):
    global gm
    global x
    global y
    global x1
    global y1
    global xx
    global pxx
    global px
    global py
    global px1
    global py1
    global pxx
    global safe
    global hs
    global hx
    global hy
    global phx
    global phy
    global high
    global score1
    global highnum
    global hsc
    global hsc1
    global hsc2
    global hsc3
    global hsc4
    global hsc5
    global pic
    global im
    global saveb
    global sim
    global psim
    global psp
    global dright
    global vert
    global pvert
    global pdright
    global pddown
    global pscore
    global gmode
    global gmodec
    global startv
    global gmodecc
    global shape
    global speed
    global solid
    global shead
    global scount
    global applenum
    global appleamount
    global screencheck
    global gmodecc
    global wordc
    global rhead
    global score
    wordc=False
    gmode=1
    if gmodecc==2:
        gmode=2
    screencheck=False
    pvert=False
    pdright=True
    pddown=False
    dright=True
    vert=False
    startv=True
    try:
        saveb.destroy()
    except:
        None
    try:
        hsc.destroy()
        hsc1.destroy()
        hsc2.destroy()
        hsc3.destroy()
        hsc4.destroy()
        hsc5.destroy()
    except:
        None
    try:
        hsc1.destroy()
    except:
        None
    if gmode==1:
        if high==True:
            f=open('snake.save1')
            fl=f.read()
            fl=fl.split(',')
            for xn in range(len(fl)):
                fl[xn]=fl[xn].split('~`')
            hss=hs.get()
            hss=hss.replace(' ','_')
            fl[4]=[hss,str(score1)]
            fl.sort(key=lambda x: int(x[1]),reverse=True)        
            for xn in range(11):
                fl[xn]=str(fl[xn]).replace(',','~`')
            fl=str(fl).replace("'",'').replace('"','').replace('[','').replace(']','').replace(' ','')
            f.close()
            f=open('snake.save1','w')
            f.write(fl)
            hs.destroy()
            f.close()
            high=False
    try:
        score.destroy()
    except:
        None
    try:
        pscore.destroy()
    except:
        None
    pxx=15
    xx=15
    if gmode==1:
        score=Label(master=root,bg='black',fg='white',text='Score: '+str(xx),font=(40))
        score.place(x=20,y=20)
    else:
        score=Label(master=root,bg='black',fg='white',text='P1 Score: '+str(xx),font=(40))
        score.place(x=20,y=20)
        pscore=Label(master=root,bg='black',fg='white',text='P2 Score: '+str(pxx),font=(40))
        pscore.place(x=1000,y=20)
    safe=True
    x1=20
    y1=0
    x=300
    y=300
    px1=20
    py1=0
    px=300
    py=200
    hx=[]
    hy=[]
    phx=[]
    phy=[]
    if gmode==2:
        y=460
    root.bind('<Right>',nt)
    root.bind('<Up>',up)
    root.bind('<Down>',down)
    root.bind('<Left>',nt)
    root.bind('<d>',nt)
    root.bind('<w>',pup)
    root.bind('<s>',pdown)
    root.bind('<a>',nt)
    c.delete('all')
    try:
     gm.destroy()
    except:
        None
    root.bind('<Return>',nt)
    loadpref()
    if shead=='face':
        sim=rhead
        psim=rhead
    else:
        sim=rburger
        psim=rburger
    apple()
    gmodec=1
    if applenum>1:
        apple2()
    if applenum>2:
        apple3()
    if applenum>3:
        apple4()
    if gmode==2:
        pgame()
        gmodec=0
    game()
def nt(event):
    x=1
def end():
    global startv
    global pp
    global t
    global x
    global y
    global s
    global hx
    global hy
    global phx
    global phy
    global xx
    global ax
    global ay
    global ax2
    global ay2
    global gm
    global ax
    global ax2
    global ax3
    global ax4
    global ay
    global ay2
    global ay3
    global ay4
    global score
    global score1
    global safe
    global high
    global hs
    global highnum
    global hsc
    global hsc1
    global hsc2
    global hsc3
    global hsc4
    global hsc5
    global fl
    global gm
    global gmode
    global stc1
    global stc2
    global stc3
    global stc4
    global stc8
    global screencheck
    root.bind('<Right>',nt)
    root.bind('<Up>',nt)
    root.bind('<Down>',nt)
    root.bind('<Left>',nt)
    root.bind('<d>',nt)
    root.bind('<w>',nt)
    root.bind('<s>',nt)
    root.bind('<a>',nt)
    ax,ay,ax2,ay2,ax3,ay3,ax4,ay4=0,0,0,0,0,0,0,0
    startv=False
    try:
        gm.destroy()
    except:
        None
    try:
        score.destroy()
    except:
        None
    try:
        pscore.destroy()
    except:
        None
    safe=False
    if gmodecc==2:
        gmode=2
    if gmode==1:
        score2=xx
        score1=xx
        try:
            f=open('snake.save1')
            fl=f.read()
            fl=str(fl).replace('(','').replace(')','').replace(',',' ').replace('~`',' ').replace('[','').replace(']','')
            fl=fl.split()
            if int(fl[9])<score2:
                hs=Entry(master=root,bg='grey')
                hs.place(x=480,y=120,width=200,height=20)
                hs.insert(0,'New highscore enter your name')
                high=True
                highnum=4
            f.close()
        except:
            hsc1=Label(master=c,text='High Scores Unavailable',font=('bold 40'),fg='green',bg='black')
            hsc1.place(relx=.25,rely=.5)
    t=1
    pt=1
    s=10
    x=300
    y=300
    x1=20
    y1=0
    xx=15
    hx=[]
    hy=[]
    phx=[]
    phy=[]
    pp=0
    pp2=0
    score=xx
    stc1=4
    stc2=3
    stc3=2
    stc4=1
    stc8=16
    c.delete('all')
    root.bind('<Return>',start)
    root.after(10,clearall)
    if screencheck==False:
        root.after(200,startscreen)
    screencheck=True
def clearall():
    global c
    global im1
    global fl
    global hsc
    global hsc1
    global hsc2
    global hsc3
    global hsc4
    global hsc5
    global win
    global gmode
    global gmodec
    global gmodecc
    if gmodecc==1:
        gmode=1
    c.delete("all")
    
    if gmode==1:
        gm=c.create_text(600,60,text='Game Over- Press Enter To Restart',fill='green',font=('bold 50'),tags='resartt')
        try:
            hsc=c.create_text(250,136,text='High Scores:',font=('bold 25'),fill='green')
            hsc1=c.create_text(250,204,text=str(fl[0])+':  '+str(fl[1]),font=('bold 20'),fill='green')
            hsc2=c.create_text(250,272,text=str(fl[2])+':  '+str(fl[3]),font=('bold 20'),fill='green')
            hsc3=c.create_text(250,340,text=str(fl[4])+':  '+str(fl[5]),font=('bold 20'),fill='green')
            hsc4=c.create_text(250,408,text=str(fl[6])+':  '+str(fl[7]),font=('bold 20'),fill='green')
            hsc5=c.create_text(250,476,text=str(fl[8])+':  '+str(fl[9]),font=('bold 20'),fill='green')
        except:
            None
    else:
        if gmodec==0:
            gm=c.create_text(600,60,text='player '+str(win)+' wins!',fill='green',font=('bold 50'))
        elif gmodec==1:
            gm=c.create_text(600,60,text='Two Player Snake Press Enter To Start',fill='green',font=('bold 50'))
        elif gmodec==2:
            gm=c.create_text(600,60,text='One Player Snake Press Enter To Start',fill='green',font=('bold 50'))
    if gmodec==2:
        try:
            c.delete('resartt')
        except:
            None
        gm=c.create_text(600,60,text='One Player Snake Press Enter To Start',fill='green',font=('bold 50'))
def game():
    global phx
    global phy
    global pp
    global xx
    global x
    global y
    global x1
    global y1
    global t
    global ax
    global ay
    global ax2
    global ay2
    global ax3
    global ay3
    global ax4
    global ay4
    global hx
    global hy
    global safe
    global speed
    global solid
    global gmode
    global win
    global score
    global appleamount
    global applenum
    global selfbodyon
    pp+=1
    if safe==True:
        if x==ax and y==ay:
            xx=xx+appleamount
            c.delete('ap')
            try:
                score.destroy()
            except:
                None
            if gmode==1:
                score=Label(master=root,bg='black',fg='white',text='Score: '+str(xx),font=(40))
                score.place(x=20,y=20)
            else:
                score=Label(master=root,bg='black',fg='white',text='P1 Score: '+str(xx),font=(40))
                score.place(x=20,y=20)
            apple()
        if applenum>1:
            if x==ax2 and y==ay2:
                xx=xx+appleamount
                c.delete('ap2')
                try:
                    score.destroy()
                except:
                    None
                if gmode==1:
                    score=Label(master=root,bg='black',fg='white',text='Score: '+str(xx),font=(40))
                    score.place(x=20,y=20)
                else:
                    score=Label(master=root,bg='black',fg='white',text='P1 Score: '+str(xx),font=(40))
                    score.place(x=20,y=20)
                apple2()
        if applenum>2:
            if x==ax3 and y==ay3:
                xx=xx+appleamount
                c.delete('ap3')
                try:
                    score.destroy()
                except:
                    None
                if gmode==1:
                    score=Label(master=root,bg='black',fg='white',text='Score: '+str(xx),font=(40))
                    score.place(x=20,y=20)
                else:
                    score=Label(master=root,bg='black',fg='white',text='P1 Score: '+str(xx),font=(40))
                    score.place(x=20,y=20)
                apple3()
        if applenum>3:
            if x==ax4 and y==ay4:
                xx=xx+appleamount
                c.delete('ap4')
                try:
                    score.destroy()
                except:
                    None
                if gmode==1:
                    score=Label(master=root,bg='black',fg='white',text='Score: '+str(xx),font=(40))
                    score.place(x=20,y=20)
                else:
                    score=Label(master=root,bg='black',fg='white',text='P1 Score: '+str(xx),font=(40))
                    score.place(x=20,y=20)
                apple4()
        if y>0 and y<680 and x>0 and x<1200:
         if pp>=4:
          if gmode==2:  
              for num in range(0,len(phx)):
               if phx[num]==x and phy[num]==y:
                win=2
                end()  
          for num in range(0,len(hx)):
            if selfbodyon==True:
                 if hx[num]==x and hy[num]==y:
                  win=2
                  end() 
          else:
            c1()
            x=x+x1
            y=y+y1
            t=t+1
            c.delete('l'+str(t-xx))
            root.after(speed,game)
         else:
            c1()
            x=x+x1
            y=y+y1
            t=t+1
            c.delete('l'+str(t-xx))
            root.after(speed,game)
        else:
            if solid==True:
                win=2
                end()
            else:
                if y==0:
                    y=660
                elif y==680:
                    y=20
                elif x==0:
                    x=1180
                elif x==1200:
                    x=20
                game()
def gamecall():
    global phx
    global phy
    global pp
    global xx
    global x
    global y
    global x1
    global y1
    global t
    global ax
    global ay
    global ax2
    global ay2
    global ax3
    global ay3
    global ax4
    global ay4
    global hx
    global hy
    global solid
    global score
    global appleamount
    global applenum
    global selfbodyon
    pp+=1
    if x==ax and y==ay:
        xx=xx+appleamount
        c.delete('ap')
        try:
            score.destroy()
        except:
            None
        if gmode==1:
            score=Label(master=root,bg='black',fg='white',text='Score: '+str(xx),font=(40))
            score.place(x=20,y=20)
        else:
            score=Label(master=root,bg='black',fg='white',text='P1 Score: '+str(xx),font=(40))
            score.place(x=20,y=20)
        apple()
    if applenum>1:
        if x==ax2 and y==ay2:
            xx=xx+appleamount
            c.delete('ap2')
            try:
                score.destroy()
            except:
                None
            if gmode==1:
                score=Label(master=root,bg='black',fg='white',text='Score: '+str(xx),font=(40))
                score.place(x=20,y=20)
            else:
                score=Label(master=root,bg='black',fg='white',text='P1 Score: '+str(xx),font=(40))
                score.place(x=20,y=20)
            apple2()
    if applenum>2:
        if x==ax3 and y==ay3:
            xx=xx+appleamount
            c.delete('ap3')
            try:
                score.destroy()
            except:
                None
            if gmode==1:
                score=Label(master=root,bg='black',fg='white',text='Score: '+str(xx),font=(40))
                score.place(x=20,y=20)
            else:
                score=Label(master=root,bg='black',fg='white',text='P1 Score: '+str(xx),font=(40))
                score.place(x=20,y=20)
            apple3()
    if applenum>3:
        if x==ax4 and y==ay4:
            xx=xx+appleamount
            c.delete('ap4')
            try:
                score.destroy()
            except:
                None
            if gmode==1:
                score=Label(master=root,bg='black',fg='white',text='Score: '+str(xx),font=(40))
                score.place(x=20,y=20)
            else:
                score=Label(master=root,bg='black',fg='white',text='P1 Score: '+str(xx),font=(40))
                score.place(x=20,y=20)
            apple4()
    if y>0 and y<680 and x>0 and x<1200:
     if pp>=4:
      for num in range(0,len(hx)):
        if selfbodyon==True:
             if hx[num]==x and hy[num]==y:
              end()
      else:
        c1()
        x=x+x1
        y=y+y1
        t=t+1
        c.delete('l'+str(t-xx))
     else:
        c1()
        x=x+x1
        y=y+y1
        t=t+1
        c.delete('l'+str(t-xx))
    else:
        if solid==True:
            win=2
            end()
        else:
            if y==0:
                y=660
            elif y==680:
                y=20
            elif x==0:
                x=1180
            elif x==1200:
                x=20
def pgame():
    global hx
    global hy
    global pp2
    global pxx
    global px
    global py
    global px1
    global py1
    global pt
    global ax
    global ay
    global ax2
    global ay2
    global ax3
    global ay3
    global ax4
    global ay4
    global phx
    global phy
    global safe
    global speed
    global solid
    global gmode
    global win
    global pscore
    global appleamount
    global applenum
    global gmode
    global selfbodyon
    pp2+=1
    if gmode==2:
        if safe==True:
            if px==ax and py==ay:
                pxx=pxx+appleamount
                c.delete('ap')
                try:
                    pscore.destroy()
                except:
                    None
                pscore=Label(master=root,bg='black',fg='white',text='P2 Score: '+str(pxx),font=(40))
                pscore.place(x=1000,y=20)
                apple()
            if applenum>1:
                if px==ax2 and py==ay2:
                    pxx=pxx+appleamount
                    c.delete('ap2')
                    try:
                        pscore.destroy()
                    except:
                        None
                    pscore=Label(master=root,bg='black',fg='white',text='P2 Score: '+str(pxx),font=(40))
                    pscore.place(x=1000,y=20)
                    apple2()
            if applenum>2:
                if px==ax3 and py==ay3:
                    pxx=pxx+appleamount
                    c.delete('ap3')
                    try:
                        pscore.destroy()
                    except:
                        None
                    pscore=Label(master=root,bg='black',fg='white',text='P2 Score: '+str(pxx),font=(40))
                    pscore.place(x=1000,y=20)
                    apple3()
            if applenum>3:
                if px==ax4 and py==ay4:
                    pxx=pxx+appleamount
                    c.delete('ap4')
                    try:
                        pscore.destroy()
                    except:
                        None
                    pscore=Label(master=root,bg='black',fg='white',text='P2 Score: '+str(pxx),font=(40))
                    pscore.place(x=1000,y=20)
                    apple4()
            if py>0 and py<680 and px>0 and px<1200:
             if pp2>=pxx:  
              for num in range(0,len(hx)):
                   if hx[num]==px and hy[num]==py:
                    win=1
                    end()  
              for num in range(0,len(phx)):
                if selfbodyon==True:  
                     if phx[num]==px and phy[num]==py:
                      win=1
                      end() 
              else:
                pc1()
                px=px+px1
                py=py+py1
                pt=pt+1
                c.delete('pl'+str(pt-pxx))
                root.after(speed,pgame)
             else:
                pc1()
                px=px+px1
                py=py+py1
                pt=pt+1
                c.delete('pl'+str(pt-pxx))
                root.after(speed,pgame)
            else:
                if solid==True:
                    win=1
                    end()
                else:
                    if py==0:
                        py=660
                    elif py==680:
                        py=20
                    elif px==0:
                        px=1180
                    elif px==1200:
                        px=20
                    pgame()
def pgamecall():
    global pp2
    global pxx
    global px
    global py
    global px1
    global py1
    global pt
    global ax
    global ay
    global ax2
    global ay2
    global ax3
    global ay3
    global ax4
    global ay4
    global phx
    global phy
    global solid
    global pscore
    global appleamount
    global applenum
    global gmode
    global selfbodyon
    pp2+=1
    if gmode==2:
        if px==ax and py==ay:
            pxx=pxx+appleamount
            c.delete('ap')
            try:
                pscore.destroy()
            except:
                None
            pscore=Label(master=root,bg='black',fg='white',text='Score: '+str(pxx),font=(40))
            pscore.place(x=1000,y=20)
            apple()
        if applenum>1:
            if px==ax2 and py==ay2:
                pxx=pxx+appleamount
                c.delete('ap2')
                try:
                    pscore.destroy()
                except:
                    None
                pscore=Label(master=root,bg='black',fg='white',text='P2 Score: '+str(pxx),font=(40))
                pscore.place(x=1000,y=20)
                apple2()
        if applenum>2:
            if px==ax3 and py==ay3:
                pxx=pxx+appleamount
                c.delete('ap3')
                try:
                    pscore.destroy()
                except:
                    None
                pscore=Label(master=root,bg='black',fg='white',text='P2 Score: '+str(pxx),font=(40))
                pscore.place(x=1000,y=20)
                apple3()
        if applenum>3:
            if px==ax4 and py==ay4:
                pxx=pxx+appleamount
                c.delete('ap4')
                try:
                    pscore.destroy()
                except:
                    None
                pscore=Label(master=root,bg='black',fg='white',text='P2 Score: '+str(pxx),font=(40))
                pscore.place(x=1000,y=20)
                apple4()
        if py>0 and py<680 and px>0 and px<1200:
         if pp2>=pxx:
          for num in range(0,len(hx)):
                   if hx[num]==px and hy[num]==py:
                    win=1
                    end()  
          for num in range(0,len(phx)):
                if selfbodyon==True:
                     if phx[num]==px and phy[num]==py:
                      win=1
                      end() 
          else:
            pc1()
            px=px+px1
            py=py+py1
            pt=pt+1
            c.delete('pl'+str(pt-pxx))
         else:
            pc1()
            px=px+px1
            py=py+py1
            pt=pt+1
            c.delete('pl'+str(pt-pxx))
        else:
            if solid==True:
                win=1
                end()
            else:
                if py==0:
                    py=660
                elif py==680:
                    py=20
                elif px==0:
                    px=1180
                elif px==1200:
                    px=20
def apple():
    global ax
    global ay
    global s
    global startv
    if startv==True:
        ax=randint(2,58)
        ay=randint(2,32)
        ax=ax*20
        ay=ay*20
        c.create_oval(ax,ay,ax+s,ay-15,outline='green',fill='green',tags='ap')
        c.create_line(ax,ay,ax,ay-18,width=3,fill='brown',tags='ap')
        c.create_oval(ax,ay-10,ax-s,ay-18,outline='green',fill='green',tags='ap')
        c.create_oval(ax-s,ay-s,ax+s,ay+s,outline='red',fill='red',tags='ap')        
def apple2():
    global ax2
    global ay2
    global startv
    if startv==True:
        ax2=randint(2,58)
        ay2=randint(2,32)
        ax2=ax2*20
        ay2=ay2*20
        c.create_oval(ax2,ay2,ax2+s,ay2-15,outline='green',fill='green',tags='ap2')
        c.create_line(ax2,ay2,ax2,ay2-18,width=3,fill='brown',tags='ap2')
        c.create_oval(ax2,ay2-10,ax2-s,ay2-18,outline='green',fill='green',tags='ap2')
        c.create_oval(ax2-s,ay2-s,ax2+s,ay2+s,outline='red',fill='red',tags='ap2')
def apple3():
    global ax3
    global ay3
    global startv
    if startv==True:
        ax3=randint(2,58)
        ay3=randint(2,32)
        ax3=ax3*20
        ay3=ay3*20
        c.create_oval(ax3,ay3,ax3+s,ay3-15,outline='green',fill='green',tags='ap3')
        c.create_line(ax3,ay3,ax3,ay3-18,width=3,fill='brown',tags='ap3')
        c.create_oval(ax3,ay3-10,ax3-s,ay3-18,outline='green',fill='green',tags='ap3')
        c.create_oval(ax3-s,ay3-s,ax3+s,ay3+s,outline='red',fill='red',tags='ap3')
def apple4():
    global ax4
    global ay4
    global startv
    if startv==True:
        ax4=randint(2,58)
        ay4=randint(2,32)
        ax4=ax4*20
        ay4=ay4*20
        c.create_oval(ax4,ay4,ax4+s,ay4-15,outline='green',fill='green',tags='ap4')
        c.create_line(ax4,ay4,ax4,ay4-18,width=3,fill='brown',tags='ap4')
        c.create_oval(ax4,ay4-10,ax4-s,ay4-18,outline='green',fill='green',tags='ap4')
        c.create_oval(ax4-s,ay4-s,ax4+s,ay4+s,outline='red',fill='red',tags='ap4')
def up(event):
    global x1
    global y1
    global vert
    global pic
    global im
    global sim
    global ddown
    global psim
    global uhead
    global shead
    global uburger
    vert=True
    ddown=False
    x1=0
    y1=-20
    if shead=='face':
        sim=uhead
    else:
        sim=uburger
    gamecall()
    root.bind('<Up>',nt)
    root.bind('<Down>',nt)
    root.bind('<Left>',left)
    root.bind('<Right>',right)
def down(event):
    global x1
    global y1
    global vert
    global pic
    global im
    global sim
    global ddown
    global dhead
    global shead
    global dburger
    x1=0
    y1=20
    if shead=='face':
        sim=dhead
    else:
        sim=dburger
    vert=True
    ddown=True
    gamecall()
    root.bind('<Down>',nt)
    root.bind('<Up>',nt)
    root.bind('<Left>',left)
    root.bind('<Right>',right)
def left(event):
    global x1
    global y1
    global vert
    global im
    global pic
    global sim
    global dright
    global lhead
    global shead
    global lburger
    x1=-20
    y1=0
    if shead=='face':
        sim=lhead
    else:
        sim=lburger
    vert=False
    dright=False
    root.bind('<Left>',nt)
    root.bind('<Up>',up)
    root.bind('<Down>',down)
    root.bind('<Right>',nt)
    gamecall()
def right(event):
    global x1
    global y1
    global vert
    global dright
    global im
    global pic
    global sim
    global rhead
    global shead
    global rburger
    x1=20
    y1=0
    if shead=='face':
        sim= rhead
    else:
        sim=rburger
    vert=False
    dright=True
    gamecall()
    root.bind('<Right>',nt)
    root.bind('<Up>',up)
    root.bind('<Down>',down)
    root.bind('<Left>',nt)
def pup(event):
    global px1
    global py1
    global pvert
    global pic
    global pim
    global psim
    global pddown
    global uhead
    global shead
    global uburger
    pvert=True
    pddown=False
    px1=0
    py1=-20
    if shead=='face':
        psim=uhead
    else:
        psim=uburger
    pgamecall()
    root.bind('<w>',nt)
    root.bind('<s>',nt)
    root.bind('<a>',pleft)
    root.bind('<d>',pright)
def pdown(event):
    global px1
    global py1
    global pvert
    global pic
    global pim
    global psim
    global pddown
    global dhead
    global shead
    global dburger
    px1=0
    py1=20
    if shead=='face':
        psim=dhead
    else:
        psim=dburger
    pvert=True
    pddown=True
    pgamecall()
    root.bind('<s>',nt)
    root.bind('<w>',nt)
    root.bind('<a>',pleft)
    root.bind('<d>',pright)
def pleft(event):
    global px1
    global py1
    global pvert
    global pim
    global pic
    global psim
    global pdright
    global lhead
    global lburger
    global shead
    px1=-20
    py1=0
    if shead=='face':
        psim=lhead
    else:
        psim=lburger
    pvert=False
    pdright=False
    root.bind('<a>',nt)
    root.bind('<w>',pup)
    root.bind('<s>',pdown)
    root.bind('<d>',nt)
    pgamecall()
def pright(event):
    global px1
    global py1
    global pvert
    global pdright
    global pim
    global pic
    global psim
    global rhead
    global rburger
    global shead
    px1=20
    py1=0
    if shead=='face':
        psim=rhead
    else:
        psim=rburger
    pvert=False
    pdright=True
    pgamecall()
    root.bind('<d>',nt)
    root.bind('<w>',pup)
    root.bind('<s>',pdown)
    root.bind('<a>',nt)
def csnake():
    global shape
    shape='circle'
    savepref(1)
def dsnake():
    global shape
    shape='diamond'
    savepref(1)
def rsnake():
    global shape
    shape='square'
    savepref(1)
def tsnake():
    global shape
    shape='triangle'
    savepref(1)
def bsnake():
    global shape
    shape='burger'
    savepref(1)
def sspeed():
    global speed
    speed=110
    savepref(2)
def nspeed():
    global speed
    speed=80
def fspeed():
    global speed
    speed=60
    savepref(2)
def xfspeed():
    global speed
    speed=40
    savepref(2)
def xxfspeed():
    global speed
    speed=20
    savepref(2)
def swon():
    global solid
    solid=True
    savepref(3)
def swoff():
    global solid
    solid=False
    savepref(3)
def face():
    global shead
    global sim
    global psim
    global dhead
    global rhead
    global lhead
    global uhead
    global vert
    global ddown
    global dright
    global pvert
    global pddown
    global pdright
    shead='face'
    if vert==True:
      if ddown==True:
            sim=dhead
      else:
            sim=uhead
    else:
      if dright==True:
          sim=rhead
      else:
          sim=lhead
    if pvert==True:
      if pddown==True:
            psim=dhead
      else:
            psim=uhead
    else:
      if pdright==True:
          psim=rhead
      else:
          psim=lhead  
    savepref(4)
def classich():
    global shead
    shead='classic'
    savepref(4)
def burgerh():
    global shead
    global uburger
    global lburger
    global dburger
    global rburger
    global vert
    global ddown
    global dright
    global pvert
    global pddown
    global pdright
    global sim
    global psim
    if vert==True:
      if ddown==True:
            sim=dburger
      else:
            sim=uburger
    else:
      if dright==True:
          sim=rburger
      else:
          sim=lburger
    if pvert==True:
      if pddown==True:
            psim=dburger
      else:
            psim=uburger
    else:
      if pdright==True:
          psim=rburger
      else:
          psim=lburger
    shead='burger'
    savepref(4)
scount=0
def loadpref():
    global shape
    global speed
    global solid
    global shead
    global scount
    global applenum
    global appleamount
    f=open('snake.save1')
    f=f.read()
    f=f.split(',')
    for xn in range(5,11):
        f[xn]=str(f[xn]).replace('~`','').replace('-6','').replace('-1','').replace('-2','').replace('-3','').replace('-4','').replace('-5','').replace('[','').replace(']','').replace('"','').replace("'",'').replace(' ','')
    shape=f[5]
    speed=int(f[6])
    solid=f[7]=='True'
    shead=f[8]
    applenum=int(f[9])
    appleamount=int(f[10])
def savepref(snum):
    global shape
    global speed
    global solid
    global shead
    global scount
    global applenum
    global appleamount
    f=open('snake.save1')
    f=f.read()
    f=f.split(',')
    for xn in range(4):
        f[xn]=f[xn].split('~`')
    if snum==1:
        f[5]=[shape,-1]
    if snum==2:
        f[6]=[speed,-2]
    if snum==3:
        f[7]=[solid,-3]
    if snum==4:
        f[8]=[shead,-4]
    if snum==5:
        f[9]=[applenum,-5]
    if snum==6:
        f[10]=[appleamount,-6]
    for xn in range(11,len(f)-1):
        try:
            f.pop(xn)
        except:
            None
    for x in range(len(f)):
        try:
            f(x).strip()
        except:
            None
    for xn in range(11):
        f[xn]=str(f[xn]).replace(',','~`')
    f=str(f).replace('[','').replace(']','').replace('"','').replace("'",'').replace(' ','')
    w=open('snake.save1','w')
    w.write(f)
def players1():
    global gmode
    global gmodec
    #gmodecc for startscreen so it can run the two snakes without messing with prefs
    global gmodecc
    gmodecc=1
    gmodec=2
    gmode=1
    end()
    root.bind('<w>',nt)
    root.bind('<s>',nt)
    root.bind('<a>',nt)
    root.bind('<d>',nt)
def players2():
    global gmode
    global gmodec
    global gmodecc
    global hs
    try:
        hs.destroy()
    except:
        None
    gmodecc=2
    gmodec=1
    end()
    gmode=2
    root.bind('<w>',pup)
    root.bind('<s>',pdown)
    root.bind('<a>',nt)
    root.bind('<d>',nt)
def applec1():
    global applenum
    global c
    if applenum>1:
        c.delete('ap2')
    if applenum>2:
        c.delete('ap3')
    if applenum>3:
        c.delete('ap4')
    applenum=1
    savepref(5)
def applec2():
    global applenum
    global c
    if applenum==1:
        apple2()
    if applenum==3:
        c.delete('ap3')
        c.delete('ap4')
    if applenum==4:
        c.delte('ap4')
        c.delete('ap3')
    applenum=2
    savepref(5)
def applec3():
    global applenum
    if applenum==1:
        apple3()
        apple2()
    if applenum==2:
        apple3()
    if applenum==4:
        c.delete('ap4')
    applenum=3
    savepref(5)
def applec4():
    global applenum
    if applenum==3:
        apple4()
    if applenum==2:
        apple3()
        apple4()
    if applenum==1:
        apple2()
        apple3()
        apple4()
    applenum=4
    savepref(5)
def apm1():
    global appleamount
    appleamount=1
    savepref(6)
def apm2():
    global appleamount
    appleamount=2
    savepref(6)
def apm4():
    global appleamount
    appleamount=4
    savepref(6)
def apm8():
    global appleamount
    appleamount=8
    savepref(6)
def apm16():
    global appleamount
    appleamount=16
    savepref(6)
def apm100():
    global appleamount
    appleamount=100
    savepref(6)
def bodyon():
      global selfbodyon
      selfbodyon=True
def bodyoff():
      global selfbodyon
      selfbodyon=False
loadpref()
root.bind('<Return>',start)
menu=Menu(root,bg='black',fg='green',activebackground='black',activeforeground='white')
root.config(menu=menu)
menu.config(bg='black',fg='green',activebackground='black',activeforeground='white')
settings=Menu(menu,bg='black',fg='green',activebackground='black',activeforeground='white')
menu.add_cascade(label='Body',menu=settings)
headm=Menu(menu,bg='black',fg='green',activebackground='black',activeforeground='white')
menu.add_cascade(label='Head',menu=headm)
speedm=Menu(menu,bg='black',fg='green',activebackground='black',activeforeground='white')
menu.add_cascade(label='Speed',menu=speedm)
solidwalls=Menu(menu,bg='black',fg='green',activebackground='black',activeforeground='white')
menu.add_cascade(label='Solid Walls',menu=solidwalls)
players=Menu(menu,bg='black',fg='green',activebackground='black',activeforeground='white')
menu.add_cascade(label='Game Mode',menu=players)
applem=Menu(menu,bg='black',fg='green',activebackground='black',activeforeground='white')
menu.add_cascade(label='Apples',menu=applem)
apamt=Menu(menu,bg='black',fg='green',activebackground='black',activeforeground='white')
menu.add_cascade(label='Points Per Apple',menu=apamt)
bodym=Menu(menu,bg='black',fg='green',activebackground='black',activeforeground='white')
menu.add_cascade(label='Self Body Collision',menu=bodym)
bodym.add_command(label='On',command=bodyon)
bodym.add_command(label='Off',command=bodyoff)
apamt.add_command(label='1',command=apm1)
apamt.add_command(label='2',command=apm2)
apamt.add_command(label='4',command=apm4)
apamt.add_command(label='8',command=apm8)
apamt.add_command(label='16',command=apm16)
apamt.add_command(label='100',command=apm100)
applem.add_command(label='1 Apple',command=applec1)
applem.add_command(label='2 Apples',command=applec2)
applem.add_command(label='3 Apples',command=applec3)
applem.add_command(label='4 Apples',command=applec4)
players.add_command(label='Single Player',command=players1)
players.add_command(label='Two Player',command=players2)
headm.add_command(label='Classic',command=classich)
headm.add_command(label='Face',command=face)
headm.add_command(label='Burger',command=burgerh)
solidwalls.add_command(label='On',command=swon)
solidwalls.add_command(label='Off',command=swoff)
speedm.add_command(label='Slow',command=sspeed)
speedm.add_command(label='Normal',command=nspeed)
speedm.add_command(label='Fast',command=fspeed)
speedm.add_command(label='Extra Fast',command=xfspeed)
speedm.add_command(label='Extra Extra Fast',command=xxfspeed)
settings.add_command(label="Circles",command=csnake)
settings.add_command(label="Diamonds",command=dsnake)
settings.add_command(label='Squares',command=rsnake)
settings.add_command(label='Triangles',command=tsnake)
settings.add_command(label='Burgers',command=bsnake)
root.mainloop()
