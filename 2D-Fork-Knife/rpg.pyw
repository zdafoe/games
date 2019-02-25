from pygame import*
from time import sleep,time
import tkinter as tk
import math
import multiprocessing as mp
from socket import socket, AF_INET, SOCK_DGRAM,getaddrinfo,SOL_SOCKET, SO_BROADCAST,SOCK_STREAM,SHUT_RDWR
from threading import Thread

def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def newgameping(launcher):
    hostip=get_ip()
    broadcastsocket=socket(AF_INET, SOCK_DGRAM)
    broadcastsocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    hostlist=hostip.split('.')
    try:
        while launcher.newgame:
            broadcastdata=launcher.gamename.get()+':'+launcher.mapsize.get() +','+launcher.speedentry.get()+':'+str(launcher.players).replace('[','').replace(']','').replace(':',';')+':'+str(hostip)
            broadcastdata=broadcastdata.encode('utf-8')
            for x in range(256):
                hostlist[3]=str(x)
                broadcastsocket.sendto(broadcastdata,('.'.join(hostlist),5063))
            sleep(1)
    except:
        broadcastsocket.shutdown(SHUT_RDWR)
    broadcastsocket.shutdown(SHUT_RDWR)
def getnewgameping(launcher):
    hostip=get_ip()
    locatesoc=socket(AF_INET, SOCK_DGRAM )
    locatesoc.bind((hostip,5063))
    sendaddresslist=[]
    try:
        while launcher.joining:
            if not launcher.refreshqueue.empty():
                    while not launcher.refreshqueue.empty():
                        launcher.refreshqueue.get()
                    sendaddresslist=[]
                    launcher.ipqueue.put(sendaddresslist)
                    refreshed=True

            else:
                data,addr=locatesoc.recvfrom(1024)
                refreshed=False
            if launcher.joining and not refreshed:
                if data!=b'11111111101':
                    data=data.decode('utf-8')
                    sentip=data.split(':')[-1]
                    players=data.split(':')[-2]
                    mapsizespeed=(data.split(':')[-3]).split(',')
                    gamename=data.split(':')
                    del gamename[-1]
                    del gamename[-1]
                    del gamename[-1]
                    gamename=''.join(gamename).replace('{','').replace('}','')
                    isinlist=False
                    for nameip in sendaddresslist:
                        if nameip[0]==sentip:
                            if nameip[1]!=gamename:
                                sendaddresslist[sendaddresslist.index(nameip)][1]=gamename
                                launcher.ipqueue.put(sendaddresslist)
                            if nameip[2]!=players:
                                sendaddresslist[sendaddresslist.index(nameip)][2]=players
                                launcher.ipqueue.put(sendaddresslist)
                            if nameip[3]!=mapsizespeed:
                                sendaddresslist[sendaddresslist.index(nameip)][3]=mapsizespeed
                            isinlist=True
                    if not isinlist:
                        sendaddresslist.append([sentip,gamename,players,mapsizespeed])
                        launcher.ipqueue.put(sendaddresslist)
    except:
        locatesoc.shutdown(SHUT_RDWR)
        locatesoc.close()
    locatesoc.shutdown(SHUT_RDWR)
    locatesoc.close()
def joinping(launcher):
    while launcher.joining:
        try:
            joinsoc=socket(AF_INET, SOCK_DGRAM )
            data=(launcher.name.get().replace(',','.')).encode('utf-8')
            joinsoc.sendto(data,(launcher.player.gameip,5064))
        except:
            pass
        sleep(1)
    joinsoc.shutdown(SHUT_RDWR)
def getjoinping(launcher):
    hostip=get_ip()
    getjoinsoc=socket(AF_INET, SOCK_DGRAM )
    getjoinsoc.bind((hostip,5064))
    sendaddresslist=[]
    try:
        while launcher.newgame:
            if not launcher.refreshqueue.empty():
                    while not launcher.refreshqueue.empty():
                        launcher.refreshqueue.get()
                    sendaddresslist=[]
                    launcher.ipqueue.put(sendaddresslist)
                    name=b'11111111101'
            else:
                name,address=getjoinsoc.recvfrom(1024)
            if launcher.newgame:
                if name!=b'11111111101':
                    name=name.decode('utf-8')
                    sentip=address[0]
                    isinlist=False
                    for nameip in sendaddresslist:
                        if nameip[0]==sentip:
                            if nameip[1]!=name:
                                sendaddresslist[sendaddresslist.index(nameip)][1]=name
                                launcher.ipqueue.put(sendaddresslist)
                            isinlist=True
                    if not isinlist:
                        sendaddresslist.append([sentip,name])
                        launcher.ipqueue.put(sendaddresslist)
    except:
        getjoinsoc.shutdown(SHUT_RDWR)
        getjoinsoc.close()
    getjoinsoc.shutdown(SHUT_RDWR)
    getjoinsoc.close()

def serversend(player):
    #port 5065
    serverSendSoc=socket(AF_INET, SOCK_DGRAM)
    firstiteration=True
    xy=str(player.y)+','+str(player.x)
    player.bulletlist1=[]
    for coord in player.bulletlist:
        if '(' in str(coord):
            player.bulletlist1.append('`'.join((str(coord[0]),str(coord[1]))))
    bullets=','.join(player.bulletlist1)
    currenthealthratio=player.health/player.maxhealth
     #     [0][0]             [0][1]           [1]             [2]            [3]                    [4]                 [5][0]            [5][1]                     [6]
    serverdata=player.myip+','+player.finalname+':'+xy+':'+str(player.angle)+':'+bullets+':'+str(currenthealthratio)+':'+player.hitname+','+str(player.hitdamage)+':'+str(player.mysprite)
    datalist=[serverdata,]
    transferGameDataQueueget=[]
    
    while player.isplaying.empty():
        try:
            while not player.sendGameDataQueue.empty():
                serverdata=[player.sendGameDataQueue.get(),]
            if not firstiteration:
                while not player.transferGameDataQueue.empty():
                    transferGameDataQueueget=player.transferGameDataQueue.get()
                datalist=serverdata+transferGameDataQueueget

                data='/'.join(datalist)
                data=str(time())+'/'+data
                data=data.encode('utf-8')
            else:
                firstiteration=False
                data=b'11111111101'
            player.gameDataQueue.put(transferGameDataQueueget)
            for ip in player.finaliplist:
                serverSendSoc.sendto(data,(ip,5065))
            sleep(.005)
        except Exception as exx:
            print(exx)
    serverSendSoc.shutdown(SHUT_RDWR)
def serverrecv(player):
    #port 5165
    serverrecvsoc=socket(AF_INET, SOCK_DGRAM)
    serverrecvsoc.bind((get_ip(),5165))
    addresslist=[]
    datalist=[]
    previousrecvtime=0
    while player.isplaying.empty():
        #receive single string frome one playerwith that players data
        data,address=serverrecvsoc.recvfrom(2024)
        if data!=b'11111111101':
            data=data.decode('utf-8')
            time,data=data.split('/')

            #make list of addresses and data to organize the data
            if address[0] in addresslist:
                index=int(addresslist.index(address[0])/2)
                previousrecvtime=addresslist[int(index*2)+1]
                if float(time)>previousrecvtime:
                    previousrecvtime=float(time)
                    datalist[index]=data
            else:
                addresslist.append(address[0])
                addresslist.append(float(time))
                datalist.append(data)
            player.transferGameDataQueue.put(datalist)
    serverrecvsoc.shutdown(SHUT_RDWR)
    serverrecvsoc.close() 

def clientsend(player):
    #port 5165
    clientsendsoc=socket(AF_INET, SOCK_DGRAM)
    while player.isplaying.empty():
        data=player.sendGameDataQueue.get()
        data=str(time())+'/'+data
        data=data.encode('utf-8')
        clientsendsoc.sendto(data,(player.gameip,5165))
    clientsendsoc.shutdown(SHUT_RDWR)
def clientrecv(player):
    #port 5065
    hostip=get_ip()
    clientrecvsoc=socket(AF_INET, SOCK_DGRAM)
    clientrecvsoc.bind((hostip,5065))
    while player.isplaying.empty():
        data,address=clientrecvsoc.recvfrom(2000)
        if player.isInitialClientRecv:
            player.startQueue.put(1)
            previousrecvtime=0
        if data!=b'11111111101':
            data=data.decode('utf-8')
            data=data.split('/')
            if float(data[0])>previousrecvtime:
                previousrecvtime=float(data[0])
                del data[0]
                player.gameDataQueue.put(data)
    clientrecvsoc.shutdown(SHUT_RDWR)
    clientrecvsoc.close()
#class for handling most variables in mainloop and player functions 
class Player():
    def __init__(self):
        self.isalive=True

        self.maxhealth=200
        self.health=self.maxhealth
        self.hitname=' '
        self.invulnerable=False
        self.mysprite=0
        self.lastspritechangetime=0
        self.prevzoom=1
        #make queues and get local ip
        self.myip=get_ip()
        self.isplaying=mp.Queue()
        self.sendGameDataQueue=mp.Queue()
        self.servergoqueue=mp.Queue()

        self.musicplaying=False
        #direction list initializatiom
        self.directionlist=[False,False,False,False]
        #set background color, grid color, and wall color and blend transparents
        self.bgcolor=(30,100,30)
        self.gridcolor=(0,0,0)
        self.wallcolor=(92,64,51)
        self.bulletcolor=[]
        for rgb in self.bgcolor:
            self.bulletcolor.append(rgb-30)
        #x,y vars/speed vars initialization55
        self.x=0
        self.y=0
        self.previousFrameX=0
        self.previousFrameY=0
        self.yspeed=0
        self.xspeed=0
        #player speed, acceleration, friction and fps vars
        self.acceleration=4
        self.friction=2
        self.angle=0
        #map size/grid vars
        self.gridlength=300

        #wall vars
        self.wallphysicsdistance=180
        self.EdgeWallLoadDistance=2000
        self.EdgeWallwidth=1000

       
        #gun vars
        self.shotrange=500
        self.shootspeed=1/2
        self.bulletlifespan=.04
        self.bulletthickness=3
        self.hitdamage=40
        self.bulletcolor=(0,0,255,90)
        self.hitlist=' '
        self.alreadyhitlist=[]
        
        #gun initialization
        self.shooting=False
        self.canshoot=True
        self.shoottime=0
        self.bulletlist=[]
        self.yratio=-1
        self.xratio=0
        self.invYratio=0
        self.invXratio=-1
        self.gundistance=28
        self.issemiauto=False
        self.lastshottime=0
        #set grid compensation
        
        self.lbcompensation=700/(self.gridlength)
        self.gridShift=int(300/(self.gridlength))

        #initialize control hotkey
        self.control=False
        #initialize fullscreenon var
        self.fullscreenon=False
        #initialize lastcalltime
        self.lastcalltime=time()
        self.anglechange=0
        self.prevangle=0
        #set initial width and height
        self.width=1000
        self.height=700
        self.gameDataList=[]
        
    def init2(self):
        self.d=display.set_mode((self.width,self.height),RESIZABLE)
        self.maxspeed=self.setspeed
        #set title player.sprite
        display.set_caption("Zech's Fork-Knife")
        self.sprite=image.load('sprites/pistol.png')
        self.spidersprite=image.load('sprites/spidersprite.png')
        self.sniper=image.load('sprites/sniper.png')
        self.playerspriteslist=[self.sprite,self.spidersprite,self.sniper]
        self.finalsprite=self.sprite
        font.init()
        self.namefont = font.SysFont("comicsansms", 20)
        display.update()
        mixer.pre_init(44100, 16, 2, 1024)
        mixer.init()
        self.lasershot=mixer.Sound('sprites/Laser1.ogg')
        self.laser2=mixer.Sound('sprites/Laser2.ogg')
        mixer.music.set_volume(.35)
        mixer.music.load('sprites/Meg.ogg')
        mixer.music.play(-1)
        self.music()
    def music(self):
        if self.musicplaying:
            mixer.music.pause()
            self.musicplaying=False
        else:
            self.musicplaying=True
            mixer.music.unpause()
            
    def zoom(self,Map,zoom):
        zoomdif=zoom/self.prevzoom
        self.y,self.x=self.y/zoom,self.x/zoomdif
        self.gridlength=self.gridlength/zoomdif
        self.maxspeed=self.maxspeed/zoomdif
        self.lbcompensation=700/(self.gridlength)
        self.gridShift=int(400/(self.gridlength))
        self.shotrange=self.shotrange/zoomdif
        self.playerspriteslist=[transform.scale(self.sprite,(int(self.sprite.get_rect().width/zoom),int(self.sprite.get_rect().height/zoom)))\
        ,transform.scale(self.spidersprite,(int(self.spidersprite.get_rect().width/zoom),int(self.spidersprite.get_rect().height/zoom)))\
        ,transform.scale(self.sniper,(int(self.sniper.get_rect().width/zoom),int(self.sniper.get_rect().height/zoom)))]        
        Map.zoom(zoom)
        self.prevzoom=zoom
    def totalspeed(self):
        return (math.sqrt((self.xspeed**2)+(self.yspeed**2)))
    def setpos(self,x,y):
        self.x=x
        self.y=y
    def move(self,xmove,ymove):
        self.y+=int(xmove)
        self.x+=int(ymove)
    def pos(self):
        return (self.x,self.y)
    def getspeed(self):
        return (self.xspeed,self.yspeed)
    def timepassed(self):
        self.now=time()
        return (self.now-self.lastcalltime)
    def fullscreen(self):
        if not self.fullscreenon:
            display.set_mode((self.width,self.height),FULLSCREEN)
            self.fullscreenon=True
        else:
            display.set_mode((self.width,self.height),RESIZABLE)
            self.fullscreenon=False
    def spriteXY(self):
        return (int(self.width/2),int(self.height/2))
    def die(self,Map):
        self.health=self.maxhealth
        self.y,self.x=0,0
        self.mysprite=0
        self.changesprite(self.mysprite,Map)
    def changesprite(self,spritenum,Map):
        if spritenum==1:
            self.zoom(Map,.75)
            self.bulletcolor=(255,255,255)
            self.bulletthickness=10
            self.hitdamage=30
            self.maxspeed=self.setspeed*3
            self.bulletlifespan=.04
            self.shootspeed=1/10
            self.shotrange=200
        elif spritenum==0:
            self.zoom(Map,1)
            self.bulletcolor=(0,0,255)
            self.bulletthickness=3
            self.gundistance=23
            self.bulletlifespan=.04
            self.maxspeed=self.setspeed
            self.shootspeed=1/2
            self.hitdamage=40
            self.shotrange=450
        elif spritenum==2:
            self.zoom(Map,3)
            self.bulletcolor=(255,0,0)
            self.bulletthickness=3
            self.bulletlifespan=.2
            self.gundistance=12
            self.maxspeed=self.setspeed/3
            self.shotrange=500
            self.shootspeed=3
            self.hitdamage=100
#class for loading maps
class MapClass():
    def __init__(self):  
        #load in map objects
        self.block_original=image.load('sprites/block.png')
        self.wall_original=image.load('sprites/wall.png')
        self.horwall_original=transform.rotate(self.wall_original,90)

        self.roof_original=image.load('sprites/roof.png').convert_alpha()
        self.tree_original=image.load('sprites/tree.png').convert_alpha()

        self.pistoltile_original=image.load('sprites/PistolTile.png')
        self.spidertile_original=image.load('sprites/spiderspritetile.png')
        self.snipertile_original=image.load('sprites/snipertile.png')
        
        #create transparent copies for top layer objects
        self.rooft_original=self.roof_original.copy()
        self.treet_original=self.tree_original.copy()

        alpha=120
        self.treet_original.fill((255, 255, 255, alpha), None, BLEND_RGBA_MULT)
        self.rooft_original.fill((255, 255, 255, alpha), None, BLEND_RGBA_MULT)

        #create copys of the in map obects to actually be used
        self.block=self.block_original.copy()
        self.wall=self.wall_original.copy()
        self.horwall=self.horwall_original.copy()
        self.roof=self.roof_original.copy()
        self.tree=self.tree_original.copy()
        self.pistoltile=self.pistoltile_original.copy()
        self.spidertile=self.spidertile_original.copy()
        self.snipertile=self.snipertile_original.copy()
        self.rooft=self.rooft_original.copy()
        self.treet=self.treet_original.copy()
        
        
        
        
    def setmap(self,zoom):
        self.obstaclelist=[]
        self.toplayerlist=[]
        self.playertilelist=[]
        #walls 
        mapsize=3000
        for x in range (-int(mapsize/500),int(mapsize/500)+1):
            x=x*500
            self.obstaclelist.append((self.wall,x/zoom,mapsize/zoom))
            self.obstaclelist.append((self.wall,x/zoom,-mapsize/zoom))
        for x in range (-int(mapsize/500),int(mapsize/500)+1):
            x=x*500
            self.obstaclelist.append((self.horwall,-mapsize/zoom,x/zoom))
            self.obstaclelist.append((self.horwall,mapsize/zoom,x/zoom))

        #for player tiles syntax is (tile image, x,y,spritenumber)
        self.playertilelist.append((self.pistoltile,-50/zoom,200/zoom,0))
        self.playertilelist.append((self.spidertile,-50/zoom,-200/zoom,1))
        self.playertilelist.append((self.pistoltile,50/zoom,-200/zoom,0))
        self.playertilelist.append((self.spidertile,50/zoom,200/zoom,1))
        #sniper tile
        self.playertilelist.append((self.snipertile,-1000/zoom,-2000/zoom,2))

        self.toplayerlist.append((self.tree,-1000/zoom,-2000/zoom,self.treet))
        self.toplayerlist.append((self.tree,-1000/zoom,-2150/zoom,self.treet))
        self.toplayerlist.append((self.tree,-1150/zoom,-2000/zoom,self.treet))
        self.toplayerlist.append((self.tree,-1150/zoom,-1850/zoom,self.treet))
        self.toplayerlist.append((self.tree,-850/zoom,-2150/zoom,self.treet))
        self.toplayerlist.append((self.tree,-850/zoom,-1850/zoom,self.treet))
        self.toplayerlist.append((self.tree,-1400/zoom,-2100/zoom,self.treet))
        self.toplayerlist.append((self.tree,-700/zoom,-1950/zoom,self.treet))
        self.toplayerlist.append((self.tree,-1200/zoom,-2200/zoom,self.treet))
        self.toplayerlist.append((self.tree,-1000/zoom,-1750/zoom,self.treet))
        self.toplayerlist.append((self.tree,-1350/zoom,-1850/zoom,self.treet))
        self.toplayerlist.append((self.tree,-650/zoom,-1700/zoom,self.treet))
        #spawn area
        self.toplayerlist.append((self.roof,0,0,self.rooft))
        self.obstaclelist.append((self.wall,0,-100/zoom))
        self.obstaclelist.append((self.wall,0,100/zoom))
        self.obstaclelist.append((self.horwall,400/zoom,0))
        self.obstaclelist.append((self.horwall,-400/zoom,0)) 
        self.toplayerlist.append((self.tree,220/zoom,-425/zoom,self.treet))
        self.toplayerlist.append((self.tree,220/zoom,425/zoom,self.treet))
        self.toplayerlist.append((self.tree,-220/zoom,-425/zoom,self.treet))
        self.toplayerlist.append((self.tree,-220/zoom,425/zoom,self.treet))

    def zoom(self,zoom):
        #scale sprites to new zoom
        self.block=transform.scale(self.block_original,(int(self.block_original.get_rect().width/zoom),int(self.block_original.get_rect().height/zoom)))
        self.wall=transform.scale(self.wall_original,(int(self.wall_original.get_rect().width/zoom),int(self.wall_original.get_rect().height/zoom)))
        self.horwall=transform.scale(self.horwall_original,(int(self.horwall_original.get_rect().width/zoom),int(self.horwall_original.get_rect().height/zoom)))
        self.roof=transform.scale(self.roof_original,(int(self.roof_original.get_rect().width/zoom),int(self.roof_original.get_rect().height/zoom)))
        self.tree=transform.scale(self.tree_original,(int(self.tree_original.get_rect().width/zoom),int(self.tree_original.get_rect().height/zoom)))
        self.pistoltile=transform.scale(self.pistoltile_original,(int(self.pistoltile_original.get_rect().width/zoom),int(self.pistoltile_original.get_rect().height/zoom)))
        self.spidertile=transform.scale(self.spidertile_original,(int(self.spidertile_original.get_rect().width/zoom),int(self.spidertile_original.get_rect().height/zoom)))
        self.rooft=transform.scale(self.rooft_original,(int(self.rooft_original.get_rect().width/zoom),int(self.rooft_original.get_rect().height/zoom)))
        self.treet=transform.scale(self.treet_original,(int(self.treet_original.get_rect().width/zoom),int(self.treet_original.get_rect().height/zoom)))
        self.snipertile=transform.scale(self.snipertile_original,(int(self.snipertile_original.get_rect().width/zoom),int(self.snipertile_original.get_rect().height/zoom)))
        
        #reset map
        self.setmap(zoom)
#main game loop
def mainloop(player,Map):
    try:
        wall=[0,0,0,0]
        bc=0
        while True:
            events=event.get()
            #event handling
            for e in events:
                
                if e.type==QUIT:
                    player.isalive=False
                    quit()
                    player.isplaying.put(1)
                    hostip=get_ip()
                    killsoc=socket(AF_INET, SOCK_DGRAM)
                    killsoc.sendto(b'11111111101',(hostip,5065))
                    killsoc.sendto(b'11111111101',(hostip,5165))
                    player.gameDataQueue.put(1)
                    
                    try:
                        player.transferGameDataQueue.put(1)
                    except:
                        pass
                    break
                if e.type==KEYDOWN:
                    if player.isalive:
                        if e.key==ord('w'):
                            player.yspeed-=player.acceleration
                            player.directionlist[0]=True
                        elif e.key==ord('s'):
                            player.yspeed+=player.acceleration
                            player.directionlist[1]=True
                        elif e.key==ord('a'):
                            player.xspeed-=player.acceleration
                            player.directionlist[2]=True
                        elif e.key==ord('d'):
                            player.xspeed+=player.acceleration
                            player.directionlist[3]=True
                        elif e.key==ord('f'):
                            if player.control:
                                player.fullscreen()
                        elif e.key==ord('m'):
                            player.music()
                        elif e.key==306:
                            player.control=True
                elif e.type==KEYUP:
                    if e.key==ord('w'):
                        player.directionlist[0]=False
                    elif e.key==ord('s'):
                        player.directionlist[1]=False
                    elif e.key==ord('a'):
                        player.directionlist[2]=False
                    elif e.key==ord('d'):
                        player.directionlist[3]=False
                    elif e.key==306:
                            player.control=False
                elif e.type==16 and not player.fullscreenon:
                        player.width,player.height = e.size
                        display.set_mode((player.width,player.height),RESIZABLE)
                elif e.type==MOUSEBUTTONDOWN:
                    if e.button==1:
                        player.shooting=True
                elif e.type==MOUSEBUTTONUP:
                    if e.button==1:
                        player.shooting=False
                        if player.issemiauto:
                            player.canshoot=True
            if player.isalive:

                #acceleration code
                if player.directionlist[0]:
                    if abs(player.yspeed)<player.maxspeed:
                        player.yspeed-=player.acceleration
                if player.directionlist[1]:
                    if abs(player.yspeed)<player.maxspeed:
                        player.yspeed+=player.acceleration
                if player.directionlist[2]:
                    if abs(player.xspeed)<player.maxspeed:
                        player.xspeed-=player.acceleration
                if player.directionlist[3]:
                    if abs(player.xspeed)<player.maxspeed:
                        player.xspeed+=player.acceleration

                #max speed control
                if player.yspeed>0:
                    player.yspeed-=player.friction
                    if player.yspeed<0:
                        player.yspeed=0
                elif player.yspeed<0:
                    player.yspeed+=player.friction
                    if player.yspeed>0:
                        player.yspeed=0
                if player.xspeed>0:
                    player.xspeed-=player.friction
                    if player.xspeed<0:
                        player.xspeed=0
                elif player.xspeed<0:
                    player.xspeed+=player.friction
                    if player.xspeed>0:
                        player.xspeed=0
                #get the time since last iteration and regulate fps
                timepassed=player.timepassed()
                player.lastcalltime=time()
                if timepassed<player.fpslimit:
                    sleep(player.fpslimit-timepassed)

                #move the player
                player.move((player.xspeed/12)*(timepassed*60),(player.yspeed/12)*(timepassed*60))
                #make the background
                try:
                    player.d.fill(player.bgcolor)
                except:
                    pass
                
                
                px,py=player.pos()
                if 0:
                    #bottom wall
                    if player.x>(player.gridlength*player.gridnumber)*player.prevzoom-player.EdgeWallLoadDistance:
                        if px>player.gridlength*(player.gridnumber-player.lbcompensation)*player.prevzoom-player.wallphysicsdistance:
                            player.setpos((player.gridlength*(player.gridnumber-player.lbcompensation))*player.prevzoom-player.wallphysicsdistance,py)
                        wall[0]=True
                    else:
                        wall[0]=False
                    #top wall
                    if player.x<(-player.gridlength*player.gridnumber)+player.EdgeWallLoadDistance:
                        if px<-player.gridlength*player.gridnumber+player.wallphysicsdistance:
                            player.setpos(-player.gridlength*player.gridnumber+player.wallphysicsdistance,py)
                        wall[1]=True
                    else:
                        wall[1]=False
                    px,py=player.pos()

                    #left wall
                    if player.y<(-player.gridlength*player.gridnumber)+player.EdgeWallLoadDistance:
                        if py<-player.gridlength*player.gridnumber+player.wallphysicsdistance:
                            player.setpos(px,-player.gridlength*player.gridnumber+player.wallphysicsdistance)
                        wall[2]=True
                    else:
                        wall[2]=False
                    #right wall
                    if player.y>(player.gridlength*player.gridnumber)*player.prevzoom-player.EdgeWallLoadDistance:
                        if py>player.gridlength*(player.gridnumber-player.lbcompensation)*player.prevzoom-player.wallphysicsdistance:
                            player.setpos(px,player.gridlength*(player.gridnumber-player.lbcompensation)*player.prevzoom-player.wallphysicsdistance)
                        wall[3]=True
                    else:
                        wall[3]=False
                
                #get queue with other player data
                if not player.gameDataQueue.empty():
                    while not player.gameDataQueue.empty():
                        player.gameDataList=player.gameDataQueue.get()
                    for data in player.gameDataList:
                        #delete the local computers data from the list
                        if data.split(':')[0].split(',')[1]==player.finalname and data.split(':')[0].split(',')[0]==player.myip:
                            del player.gameDataList[player.gameDataList.index(data)]

                        #get take hit data from other players and subtract from health
                        hitdata=data.split(':')[5].split(';')
                        for hit in hitdata:
                            hit1=hit.split(',')
                            if hit!=' ':
                                    if hit1[1]==(player.myip+player.finalname):
                                        if not hit in player.alreadyhitlist:
                                            player.alreadyhitlist.append(hit)
                                            if not player.invulnerable:
                                                player.health-=int(hit1[2])
                                            if player.health<1:
                                                player.die(Map)
                                    for t in player.alreadyhitlist:
                                        index=player.alreadyhitlist.index(t)
                                        t=t.split(',')
                                        if float(t[0])<time()-10:
                                            del player.alreadyhitlist[index]

                #shooting code/ sprite rotation
                mx,my=mouse.get_pos()
                spriteX,spriteY=player.spriteXY()
                try:
                    newangle=math.atan((spriteY-my)/(spriteX-mx))
                    if player.prevangle!=newangle:
                        player.yratio=(math.sin(newangle))
                        player.xratio=(math.cos(newangle))
                        if mx<spriteX:
                            player.yratio=-player.yratio
                            player.xratio=-player.xratio
                            player.angle=(-newangle*180)/math.pi+90
                            player.finalsprite=transform.rotate(player.playerspriteslist[player.mysprite],player.angle)
                        else:
                            player.angle=(-newangle*180)/math.pi-90
                            player.finalsprite=transform.rotate(player.playerspriteslist[player.mysprite],player.angle)
                except:
                    if my>spriteY:
                        player.yratio=1
                        player.xratio=0
                        player.angle=180
                        player.finalsprite=transform.rotate(player.playerspriteslist[player.mysprite],player.angle)
                    else:
                        player.yratio=-1
                        player.xratio=0
                        player.angle=0
                        player.finalsprite=transform.rotate(player.playerspriteslist[player.mysprite],player.angle)


                #in map objects collision code
                obstaclelistindex=0
                obstacleplacelist=[]
                for obstacle in Map.obstaclelist:
                    
                    HalfWidth=obstacle[0].get_rect().width / 2
                    HalfHeight=obstacle[0].get_rect().height / 2
                    if obstacle[1]>py-(player.width/2)-(HalfWidth) and obstacle[1]<py+(player.width/2)+(HalfWidth):
                        if obstacle[2]>px-(player.height/2)-(HalfHeight) and obstacle[2]<px+(player.height/2)+(HalfHeight):
                            
                            obstacleplacelist.append(obstaclelistindex)
                            #collision detection

                            #if player is within x range of obstacle
                            if player.mysprite==2:
                                spritehalfwidth=player.playerspriteslist[player.mysprite].get_rect().width/4
                            else:
                                spritehalfwidth=player.playerspriteslist[player.mysprite].get_rect().width/2
                            if player.y-obstacle[1]<HalfWidth+spritehalfwidth and player.y-obstacle[1]>-HalfWidth-spritehalfwidth:
                                if player.x>=obstacle[2]+HalfHeight and player.x<obstacle[2]+HalfHeight+spritehalfwidth:
                                    player.x=obstacle[2]+HalfHeight+spritehalfwidth

                                elif player.x<=obstacle[2]-HalfHeight and player.x>obstacle[2]-HalfHeight-spritehalfwidth:
                                    player.x=obstacle[2]-HalfHeight-spritehalfwidth
                                        
                            #if player is within y range of obstacle
                            if player.x-obstacle[2]<HalfHeight+spritehalfwidth and player.x-obstacle[2]>-HalfHeight-spritehalfwidth:
                                if player.y>=obstacle[1] and player.y<obstacle[1]+HalfWidth+spritehalfwidth:
                                    player.y=obstacle[1]+HalfWidth+spritehalfwidth

                            
                                elif player.y<=obstacle[1] and player.y>obstacle[1]-HalfWidth-spritehalfwidth:
                                    player.y=obstacle[1]-HalfWidth-spritehalfwidth


                    obstaclelistindex+=1
                px,py=player.pos()
                #set which gridlines to draw
                verticalgridstart=int(((-player.width)/player.gridlength)+(py/player.gridlength))
                verticlegridstop=int(((player.width)/player.gridlength)+(py/player.gridlength))
                horizontalgridstart=int(((-player.height)/player.gridlength)+(px/player.gridlength))
                horizontalgridstop=int(((player.height)/player.gridlength)+(px/player.gridlength))

                #draw grid
                for x in range(verticalgridstart+player.gridShift,verticlegridstop+player.gridShift):
                    draw.line(player.d,player.gridcolor,(x*player.gridlength-py,0),(x*player.gridlength-py,player.height))
                for x in range(horizontalgridstart+player.gridShift,horizontalgridstop+player.gridShift):  
                    draw.line(player.d,player.gridcolor,(0,x*player.gridlength-px),(player.width,x*player.gridlength-px))
                
                #draw walls
                if 0:
                    if wall[0]:
                        draw.line(player.d,player.wallcolor,(0,(player.gridlength*player.gridnumber)*player.prevzoom-px+(player.height-700)/2),(player.width,(player.gridlength*player.gridnumber)*player.prevzoom-px+(player.height-700)/2),player.EdgeWallwidth)
                    if wall[1]:
                        draw.line(player.d,player.wallcolor,(0,((-player.gridlength*player.gridnumber)-px+(player.height-700)/2)),(player.width,(-player.gridlength*player.gridnumber)-px+(player.height-700)/2),player.EdgeWallwidth)
                    if wall[2]:
                        draw.line(player.d,player.wallcolor,((-player.gridlength*player.gridnumber)-py+(player.width-700)/2,0),((-player.gridlength*player.gridnumber)-py+(player.width-700)/2,player.height),player.EdgeWallwidth)
                    if wall[3]:
                        draw.line(player.d,player.wallcolor,((player.gridlength*player.gridnumber)*player.prevzoom-py+(player.width-700)/2,0),((player.gridlength*player.gridnumber)*player.prevzoom-py+(player.width-700)/2,player.height),player.EdgeWallwidth)
                
                #draw in map objects
                for x in obstacleplacelist:
                    obstacle=Map.obstaclelist[x]
                    HalfWidth=obstacle[0].get_rect().width / 2
                    HalfHeight=obstacle[0].get_rect().height / 2
                    blockxy=((obstacle[1]-HalfWidth)-py+(player.width/2),(obstacle[2]-HalfHeight)-px+(player.height/2))
                    player.d.blit(obstacle[0],(blockxy))


                #draw player tiles
                for obstacle in Map.playertilelist:
                    HalfWidth=obstacle[0].get_rect().width / 2
                    HalfHeight=obstacle[0].get_rect().height / 2
                    if obstacle[1]>py-(player.width/2)-(HalfWidth) and obstacle[1]<py+(player.width/2)+(HalfWidth):
                        if obstacle[2]>px-(player.height/2)-(HalfHeight) and obstacle[2]<px+(player.height/2)+(HalfHeight):
                            blockxy=((obstacle[1]-HalfWidth)-py+(player.width/2),(obstacle[2]-HalfHeight)-px+(player.height/2))
                            player.d.blit(obstacle[0],(blockxy))
                            if player.y-obstacle[1]<HalfWidth and player.y-obstacle[1]>-HalfWidth and player.x-obstacle[2]<HalfHeight and player.x-obstacle[2]>-HalfHeight:
                                if player.mysprite!=obstacle[3]:
                                    player.mysprite=obstacle[3]
                                    player.changesprite(obstacle[3],Map)

                if player.shooting:
                    if player.canshoot:
                        if time()-player.lastshottime>player.shootspeed or player.issemiauto:
                            player.lastshottime=time()
                            bc+=1
                            player.canshoot=False
                            #switch which inverse is negative to change which size the bullets come from
                            player.invYratio=-player.xratio
                            player.invXratio=player.yratio
                            if player.mysprite==1:
                                player.lasershot.play(maxtime=200)
                                start=(int(player.width/2),int(player.height/2))
                                
                            elif player.mysprite==2:
                                player.lasershot.play(maxtime=350)
                                start=(int(player.width/2)+int(player.invXratio-player.invXratio*player.gundistance),int(player.height/2)+int(player.invYratio-player.invYratio*player.gundistance))
                            else:
                                player.lasershot.play()
                                start=(int(player.width/2)+int(player.invXratio-player.invXratio*player.gundistance),int(player.height/2)+int(player.invYratio-player.invYratio*player.gundistance))
                            
                            end=[start[0]+int(player.xratio*player.shotrange),start[1]+int(player.yratio*player.shotrange)]
                            #bullet collision with in map obstacles
                            shortestend=player.shotrange
                            obsticle_players=[Map.obstaclelist,player.gameDataList]
                            is_obj_or_player=0
                            for ob_play in obsticle_players:
                                is_obj_or_player+=1
                                for obstacle in ob_play:
                                    if is_obj_or_player==1:
                                        HalfWidth=obstacle[0].get_rect().width / 2
                                        HalfHeight=obstacle[0].get_rect().height / 2
                                    else:
                                        obstacle=obstacle.split(':')
                                        Pwidths=obstacle[7].split(',')
                                        if int(Player[6])==2:
                                            HalfWidth=(float(Pwidths[2])/2)*(float(Player[8])/player.prevzoom)
                                            HalfHeight=(float(Pwidths[3])/2)*(float(Player[8])/player.prevzoom)
                                        else:
                                            HalfWidth=float(Pwidths[2])*(float(Player[8])/player.prevzoom)
                                            HalfHeight=float(Pwidths[3])*(float(Player[8])/player.prevzoom)
                                        obstacle1=obstacle
                                        #obstacle=[True,int(float(obstacle[0])*(float(Player[8])/player.prevzoom)),int(float(obstacle[1])*(float(Player[8])/player.prevzoom))]
                                        obstacle=['placeholder',float(obstacle[1].split(',')[0])*(float(Player[8])/player.prevzoom),float(obstacle[1].split(',')[1])*(float(Player[8])/player.prevzoom)]
                                    if obstacle[1]>py-(player.width/2)-(HalfWidth) and obstacle[1]<py+(player.width/2)+(HalfWidth):
                                        if obstacle[2]>px-(player.height/2)-(HalfHeight) and obstacle[2]<px+(player.height/2)+(HalfHeight):
                                            
                                            for point in range(player.shotrange):
                                                xpoint=start[0]+point*player.xratio
                                                ypoint=start[1]+point*player.yratio
                                                if xpoint>=obstacle[1]-(HalfWidth+player.y)+(player.width/2) and xpoint<=obstacle[1]+ (HalfWidth-player.y)+(player.width/2):
                                                    if ypoint>=obstacle[2]- (HalfHeight+player.x)+(player.height/2) and ypoint<=obstacle[2]+(HalfHeight-player.x)+(player.height/2):
                                                        if math.sqrt((xpoint-start[0])**2+(ypoint-start[1])**2)<shortestend:
                                                            end=(xpoint,ypoint)
                                                            shortestend=math.sqrt((xpoint-start[0])**2+(ypoint-start[1])**2)
                                                            if is_obj_or_player==2:
                                                                player.hitname=''.join(obstacle1[0].split(','))
                                                            else:
                                                                player.hitname=' '
                                                        break
                            player.bulletlist.append(start)
                            player.bulletlist.append(tuple(end))
                            player.bulletlist.append(time())

                    
                player.shoottime+=timepassed
                if player.shoottime>player.shootspeed:
                    player.canshoot=True
                    player.shoottime=0
                if len(player.bulletlist)>0:
                    if time()-player.bulletlist[2]>player.bulletlifespan:
                            player.bulletlist.pop(0)
                            player.bulletlist.pop(0)
                            player.bulletlist.pop(0)
                    for iteration in range(int(len(player.bulletlist)/3)):
                        iteration=iteration*3
                        draw.line(player.d,player.bulletcolor,player.bulletlist[iteration],player.bulletlist[iteration+1],player.bulletthickness)
                
                #draw other player's bullets
                for Player in player.gameDataList:
                    Player=Player.split(':')
                    Pwidths=Player[7].split(',') 
                    Pwidths=(float(Pwidths[0])*(float(Player[8])/player.prevzoom),float(Pwidths[1])*(float(Player[8])/player.prevzoom))
                    Playerxy=Player[1].split(',')
                    Playerxy=(float(Playerxy[0])*(float(Player[8])/player.prevzoom),float(Playerxy[1])*(float(Player[8])/player.prevzoom))
                    otherplayersbulletlist=Player[3]
                    otherplayersbulletlist=otherplayersbulletlist.split(',')
                    Playerbulletthickness=int(otherplayersbulletlist[-1].split('`')[0])
                    Playerbulletcolor=otherplayersbulletlist[-1].split('`')[1:4]
                    for x in range(len(Playerbulletcolor)):
                        Playerbulletcolor[x]=int(Playerbulletcolor[x])
                    if len(otherplayersbulletlist)>1:
                        for x in range(len(otherplayersbulletlist)):
                            otherplayersbulletlist[x]=otherplayersbulletlist[x].split('`')
                        for iteration in range(int(len(otherplayersbulletlist)/2)):
                            if len(otherplayersbulletlist[iteration])==2:
                                iteration=iteration*2                             #-(player.width-float(Pwidths[0])/2)
                                start=(float(otherplayersbulletlist[iteration][0])*(float(Player[8])/player.prevzoom)+(player.width-float(Pwidths[0]))/2+Playerxy[0]-py,\
                                float(otherplayersbulletlist[iteration][1])*(float(Player[8])/player.prevzoom)+(player.height-float(Pwidths[1]))/2+Playerxy[1]-px)
                                
                                
                                end=(float(otherplayersbulletlist[iteration+1][0])*(float(Player[8])/player.prevzoom)+(player.width-float(Pwidths[0]))/2+Playerxy[0]-py,float(otherplayersbulletlist[iteration+1][1])*(float(Player[8])/player.prevzoom)+(player.height-float(Pwidths[1]))/2+Playerxy[1]-px)
                                draw.line(player.d,Playerbulletcolor,start,end,Playerbulletthickness)

                #draw other players
                for Player in player.gameDataList:
                    #index=player.gameDataList.index(player)
                    Player=Player.split(':')
                    obstacle=Player[1].split(',')
                    obstacle=[True,int(float(obstacle[0])*(float(Player[8])/player.prevzoom)),int(float(obstacle[1])*(float(Player[8])/player.prevzoom))]

                    #rotate sprite
                    otherplayersprite=transform.rotate(player.playerspriteslist[int(Player[6])],float(Player[2]))
                    HalfWidth=otherplayersprite.get_rect().width / 2
                    HalfHeight=otherplayersprite.get_rect().height / 2
                    # if other player is onscreen--:
                    if obstacle[1]>py-(player.width/2)-(HalfWidth) and obstacle[1]<py+(player.width/2)+(HalfWidth):
                        if obstacle[2]>px-(player.height/2)-(HalfHeight) and obstacle[2]<px+(player.height/2)+(HalfHeight):
                            #set actual xy values for player and nametag
                            Playerhealth=float(Player[4])
                            playerxy=((obstacle[1]-HalfWidth)-py+(player.width/2),(obstacle[2]-HalfHeight)-px+(player.height/2))
                            text=player.namefont.render(Player[0].split(',')[1],True,(0,0,0))
                            textxy=((obstacle[1]-text.get_rect().width/2)-py+(player.width/2),(obstacle[2]-text.get_rect().height/2)-px+(player.height/2)-40)
                            yajust=17
                            #draw health bar
                            draw.line(player.d,(int(255-255*Playerhealth),int(255*Playerhealth),0),(textxy[0]+text.get_rect().width/2-58,textxy[1]+yajust),(textxy[0]+text.get_rect().width/2-58+116*(Playerhealth),textxy[1]+yajust),22)
                            #draw health bar outline
                            draw.line(player.d,(0,0,0),(textxy[0]+text.get_rect().width/2-60,textxy[1]-11+yajust),(textxy[0]+text.get_rect().width/2+60,textxy[1]-11+yajust),5)
                            draw.line(player.d,(0,0,0),(textxy[0]+text.get_rect().width/2-60,textxy[1]+11+yajust),(textxy[0]+text.get_rect().width/2+60,textxy[1]+11+yajust),5)
                            draw.line(player.d,(0,0,0),(textxy[0]+text.get_rect().width/2+60,textxy[1]+13+yajust),(textxy[0]+text.get_rect().width/2+60,textxy[1]-13+yajust),5)
                            draw.line(player.d,(0,0,0),(textxy[0]+text.get_rect().width/2-60,textxy[1]-13+yajust),(textxy[0]+text.get_rect().width/2-60,textxy[1]+13+yajust),5)

                            #use blit to render the nametag and player
                            player.d.blit(text,textxy)
                            player.d.blit(otherplayersprite,(playerxy))

                #format playerxy values for sending           
                xy=str(player.y)+','+str(player.x)

                #format bullets data for sending
                player.bulletlist1=[]
                for coord in player.bulletlist:
                    if '(' in str(coord):
                        player.bulletlist1.append('`'.join((str(coord[0]),str(coord[1]))))
                bulletcolor1=(str(player.bulletcolor[0]),str(player.bulletcolor[1]),str(player.bulletcolor[2]))
                player.bulletlist1.append(str(player.bulletthickness)+'`'+'`'.join(bulletcolor1))
                bullets=','.join(player.bulletlist1)
                
                #format current health data for sending
                currenthealthratio=player.health/player.maxhealth

                #format list of players that have been hit for sending and delete old ones
                player.hitlist=player.hitlist.split(';')
                if player.hitname!=' ':
                    player.hitlist.append(str(time())+','+player.hitname+','+str(player.hitdamage))
                for t in player.hitlist:
                    index=player.hitlist.index(t)
                    t=t.split(',')
                    try: 
                        float(t[0])
                        if float(t[0])<time()-5:
                            #print('deleted: ',index)
                            del player.hitlist[index]
                    except:
                        pass
                player.hitlist=';'.join(player.hitlist)

                #send local data to the process that sends it to the server using a queue 
                #     [0][0]             [0][1]           [1]             [2]            [3]                    [4]                 [5]                  [6]                      [7][0]                [7][1]                           [7][2]                                         [7][3]                                   [8]
                data=player.myip+','+player.finalname+':'+xy+':'+str(player.angle)+':'+bullets+':'+str(currenthealthratio)+':'+player.hitlist+':'+str(player.mysprite)+':'+str(player.width)+','+str(player.height)+','+str(player.finalsprite.get_rect().width / 2)+','+str(player.finalsprite.get_rect().height / 2)+':'+str(player.prevzoom)
                player.hitname=' '
                player.sendGameDataQueue.put(data)
                    
                    
                #draw local sprite
                
                player.d.blit(player.finalsprite,(spriteX-(player.finalsprite.get_rect().width / 2),spriteY-(player.finalsprite.get_rect().height / 2)))
                
                #draw top layer
                for obstacle in Map.toplayerlist:
                    HalfWidth=obstacle[0].get_rect().width / 2
                    HalfHeight=obstacle[0].get_rect().height / 2
                    if obstacle[1]>py-(player.width/2)-(HalfWidth) and obstacle[1]<py+(player.width/2)+(HalfWidth):
                        if obstacle[2]>px-(player.height/2)-(HalfHeight) and obstacle[2]<px+(player.height/2)+(HalfHeight):
                            blockxy=((obstacle[1]-HalfWidth)-py+(player.width/2),(obstacle[2]-HalfHeight)-px+(player.height/2))
                            if player.y-obstacle[1]<HalfWidth+spritehalfwidth and player.y-obstacle[1]>-HalfWidth-spritehalfwidth and player.x-obstacle[2]<HalfHeight+spritehalfwidth and player.x-obstacle[2]>-HalfHeight-25:
                                player.d.blit(obstacle[3],(blockxy))
                            else:
                                player.d.blit(obstacle[0],(blockxy))
                
                #draw ui
                text=player.namefont.render(str((int(player.y*player.prevzoom),int(player.x*player.prevzoom))),True,(0,0,0))
                player.d.blit(text,(10,10))
                
                boxwidth=100
                boxheight=30
                boxthickness=2
                draw.line(player.d,(int(255-255*currenthealthratio),int(255*currenthealthratio),0) \
                ,(player.width/2-boxwidth+2,int(player.height-(boxheight/2+5))) \
                ,((int(player.width/2-boxwidth+2)+(((boxwidth*2)-2)*currenthealthratio)),int(player.height-(boxheight/2+5))),18)

                draw.line(player.d,(0,0,0),(player.width/2-boxwidth,player.height-boxheight),(player.width/2+boxwidth,player.height-boxheight),boxthickness)
                draw.line(player.d,(0,0,0),(player.width/2-boxwidth,player.height-10),(player.width/2+boxwidth,player.height-10),boxthickness)
                draw.line(player.d,(0,0,0),(player.width/2-boxwidth,player.height-10),(player.width/2-boxwidth,player.height-boxheight),boxthickness)
                draw.line(player.d,(0,0,0),(player.width/2+boxwidth,player.height-10),(player.width/2+boxwidth,player.height-boxheight),boxthickness)

                #update display
                display.update()
    except Exception as error:
        print('\n','----',error,'----','\n')
        player.isplaying.put(1)
        hostip=get_ip()
        killsoc=socket(AF_INET, SOCK_DGRAM)
        killsoc.sendto(b'11111111101',(hostip,5065))
        killsoc.sendto(b'11111111101',(hostip,5165))
        player.gameDataQueue.put(1)
        try:
            player.transferGameDataQueue.put(1)
        except:
            pass
#class for starting the game using tkinter to make the gui
class launcher():
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Zech's Fork-Knife Launcher")
        self.root.config(width=500,height=500,bg='black')

        self.scrollbar=tk.Scrollbar(self.root)
        self.scrollbar.place(relx=.975,relheight=1)

        self.listboxyplacement=.2
        self.iplist=tk.Listbox(self.root,yscrollcommand=self.yscroll,font=('bold 15'),bg='black',fg='green',highlightbackground='black',highlightcolor='green',selectbackground='black')
        self.iplist.place(x=0,rely=self.listboxyplacement,relwidth=.5,relheight=.25)

        self.playerlist=tk.Listbox(self.root,font=('bold 15'),yscrollcommand=self.yscroll,bg='black',fg='green',highlightbackground='black',highlightcolor='green',selectbackground='black')
        self.playerlist.place(relx=.5,rely=self.listboxyplacement,relwidth=.475,relheight=.25)

        self.gameslabel=tk.Label(self.root,text='Games',bg='black',fg='green',font=('bold 12'))
        self.playerslabel=tk.Label(self.root,text='Players in Lobby',bg='black',fg='green',font=('bold 12'))
        self.gameslabel.place(x=0,rely=self.listboxyplacement-.05,relwidth=.5,relheight=.05)
        self.playerslabel.place(relx=.5,rely=self.listboxyplacement-.05,relwidth=.45,relheight=.05)

        self.vcmd = (self.root.register(self.callback))
        self.fpsentry=tk.Entry(self.root,bg='black',validate='all',validatecommand=(self.vcmd,'%P'),fg='green',insertbackground='green')
        self.fpsentry.place(relx=.2,rely=.5,relwidth=.2,relheight=.05)
        self.fpslabel=tk.Label(self.root,text='Set FPS:',font='bold 12',bg='black',fg='green')
        self.fpslabel.place(x=0,rely=.5,relwidth=.2,relheight=.05)
        self.fpsentry.insert('0','60')

        self.scrollbar.config(command=self.yview)
        
        self.refreshbutton=tk.Button(self.root,text='Refresh',command=self.refresh,font='bold 25',bg='black',fg='green')
        self.refreshbutton.place(x=0,rely=.75,relwidth=.975,relheight=.1)
        self.startbutton=tk.Button(self.root,text='Join',command=self.Joingame,font='bold 50',bg='black',fg='green')
        self.startbutton.place(x=0,rely=.85,relwidth=.975,relheight=.15)

        self.mapsizecmd = (self.root.register(self.mapsizecallback))
        self.namecmd = (self.root.register(self.namecallback))

        self.nameyplacement=.07
        self.namelabel=tk.Label(self.root,text='Name:',font='bold 15',bg='black',fg='green')
        self.namelabel.place(x=0,rely=self.nameyplacement,relwidth=.2,relheight=.05)
        self.name=tk.Entry(self.root,bg='black',validate='all',validatecommand=(self.namecmd,'%P'),fg='green',insertbackground='green')
        self.name.place(relx=.2,rely=self.nameyplacement+.01,relwidth=.775,relheight=.04)

        self.mode=tk.IntVar()
        self.mode.set(1)
        self.creategame=tk.Radiobutton(self.root,text='Create Game',indicatoron=0,command=self.changemode,variable=self.mode,value=2,bg='black',fg='green',selectcolor='black',activebackground='black',activeforeground='white')
        self.creategame.place(relx=.5,y=0,relwidth=.45,relheight=.05)
        self.joingame=tk.Radiobutton(self.root,text='Join Game',variable=self.mode,value=1,indicatoron=0,command=self.changemode,bg='black',fg='green',selectcolor='black',activebackground='black',activeforeground='white')
        self.joingame.place(x=0,y=0,relwidth=.5,relheight=.05)
        self.joined=False
        self.prevjoinip=''
        self.ipqueueget=[]
        self.players=[]
        self.joining=True
        self.newgame=False
        self.refreshqueue=mp.Queue()
        self.startgetnewgameping()
        self.ipqueue=mp.Queue()
        self.updatelist()
        self.killsoc=socket(AF_INET, SOCK_DGRAM )
        self.root.protocol("WM_DELETE_WINDOW",self.onExit)
        self.root.mainloop()
    def onExit(self):
        self.newgame=False
        self.joining=False
        hostip=get_ip()
        self.killsoc.sendto(b'11111111101',(hostip,5063))
        self.killsoc.sendto(b'11111111101',(hostip,5064))
        self.root.destroy()
    def refresh(self):
        self.refreshqueue.put(1)
        hostip=get_ip()
        self.playerlist.delete('0',tk.END)
        self.killsoc.sendto(b'11111111101',(hostip,5063))
        self.killsoc.sendto(b'11111111101',(hostip,5064))
        if self.mode.get()==1:
            self.iplist.delete('0',tk.END)
    def startjoinping(self):
        joinPingThread=Thread(target=joinping,args=(self,))
        joinPingThread.start()
    def startgetjoinping(self):
        getJoinPingThread=Thread(target=getjoinping,args=(self,))
        getJoinPingThread.start()
    def startnewgameping(self):
        newGamePingThread=Thread(target=newgameping,args=(self,))
        newGamePingThread.start()
    def startgetnewgameping(self):
        getPingThread=Thread(target=getnewgameping,args=(self,))
        getPingThread.start()
    def yscroll(self,*args):
        if self.mode.get()==1 and not self.joined:
            self.iplist.yview_moveto(args[0])
        else:
            self.playerlist.yview_moveto(args[0])
        self.scrollbar.set(*args)
    def yview(self,*args):
        if self.mode.get()==1 and not self.joined:
            self.iplist.yview(*args)
        else:
            self.playerlist.yview(*args)
    def updatelist(self):
        if not self.ipqueue.empty():
            while not self.ipqueue.empty():
                self.ipqueueget=self.ipqueue.get()
            if self.mode.get()==1:
                #insert gamelist into listbox for joining player
                if not self.joined:
                    self.iplist.delete('0',tk.END)
                    for x in self.ipqueueget:
                        self.iplist.insert(tk.END,x[0:2])
            else:
                #insert players that have joined
                self.playerlist.delete('0',tk.END)


                #final ip list for server
                self.finaliplist=[]
                for ip in self.ipqueueget:
                    self.finaliplist.append(ip[0])

                for x in self.ipqueueget:
                    self.ipqueueget[self.ipqueueget.index(x)]=' -- '.join(x)
        try:
            if self.mode.get()==1 and str(self.iplist.curselection())!='()' and not self.joined:
                #start pinging the game server
                #insert playerlist into listbox
                self.playerlist.delete('0',tk.END)
                for name in (self.ipqueueget[self.iplist.curselection()[0]][2]).split(','):
                    self.playerlist.insert(tk.END,name)
        except:
            pass
            if self.joined:
                self.playerlist.delete('0',tk.END)
                for sub in self.ipqueueget:
                    if sub[0]==self.player.gameip:
                        ipindex=self.ipqueueget.index(sub)
                for name in self.ipqueueget[ipindex][2].split(','):
                    self.playerlist.insert(tk.END,name)
                self.mapsizeget=self.ipqueueget[ipindex][3][0]
                self.speedget=self.ipqueueget[ipindex][3][1]
        if self.mode.get()==2:
            self.playerlist.delete('0',tk.END)
            myname=self.name.get()+' -- '+str(get_ip())
            self.players=[myname,]
            self.players+=self.ipqueueget
            x=0
            for name in self.players:
                if x ==0:
                    self.playerlist.insert(tk.END,'You: '+name)
                else:
                    self.playerlist.insert(tk.END,name)
                x=1
        self.root.after(1000,self.updatelist)
    def changemode(self):
        self.playerlist.delete('0',tk.END)
        self.ipqueueget=()
        if self.mode.get()==1:
            try:
                self.iplist.destroy()
            except:
                pass
            try:

                self.gameslabel.destroy()
                self.playerslabel.destroy()
                self.mapsize.destroy()
                self.gamename.destroy()
                self.mapsizelabel.destroy()
                self.gamenamelabel.destroy()
                self.speedlabel.destroy()
                self.speedentry.destroy()
            except:
                pass
            if self.newgame:
                self.startgetnewgameping()
                hostip=get_ip()
                self.newgame=False
                self.joining=True
                self.killsoc.sendto(b'11111111101',(hostip,5064))
            self.startbutton.destroy()
            self.startbutton=tk.Button(self.root,text='Join',command=self.Joingame,font='bold 50',bg='black',fg='green')
            self.startbutton.place(x=0,rely=.85,relwidth=.975,relheight=.15)
            self.iplist=tk.Listbox(self.root,yscrollcommand=self.yscroll,font=('bold 15'),bg='black',fg='green',highlightbackground='black',highlightcolor='green',selectbackground='black')
            self.iplist.place(x=0,rely=self.listboxyplacement,relwidth=.5,relheight=.25)
            self.gameslabel=tk.Label(self.root,text='Games',bg='black',fg='green',font=('bold 12'))
            self.playerslabel=tk.Label(self.root,text='Players in Lobby',bg='black',fg='green',font=('bold 12'))
            self.gameslabel.place(x=0,rely=self.listboxyplacement-.05,relwidth=.5,relheight=.05)
            self.playerslabel.place(relx=.5,rely=self.listboxyplacement-.05,relwidth=.45,relheight=.05)
            self.playerlist.place(relx=.5,rely=self.listboxyplacement,relwidth=.475,relheight=.25)
        else:
            try:
                self.iplist.destroy()
                self.playerlist.place(relx=0,rely=self.listboxyplacement,relwidth=.975,relheight=.25)
            except:
                pass
            try:
                self.mapsize.destroy()
                self.gamename.destroy()
                self.mapsizelabel.destroy()
                self.gamenamelabel.destroy()
                self.speedlabel.destroy()
                self.speedentry.destroy()
            except:
                pass
            self.startbutton.destroy()
            
            
            self.speedentry=tk.Entry(self.root,bg='black',validate='all',validatecommand=(self.vcmd,'%P'),fg='green',insertbackground='green')
            self.speedentry.place(relx=.75,rely=.5,relwidth=.2,relheight=.05)
            self.speedentry.insert('0','70')
            self.speedlabel=tk.Label(self.root,text='Movement Speed:',font='bold 12',bg='black',fg='green')
            self.speedlabel.place(relx=.45,rely=.5,relwidth=.3,relheight=.05)
            self.startbutton=tk.Button(self.root,text='Start',command=self.opengame,font='bold 50',bg='black',fg='green')
            self.startbutton.place(x=0,rely=.85,relwidth=.975,relheight=.15)
            self.playerslabel=tk.Label(self.root,text='Players in Lobby',bg='black',fg='green',font=('bold 15'))
            self.playerslabel.place(relx=0,rely=self.listboxyplacement-.05,relwidth=.95,relheight=.05)
            self.mapsizelabel=tk.Label(self.root,text='Map Size:',font='bold 12',bg='black',fg='green')
            self.mapsizelabel.place(x=0,rely=.69,relwidth=.2,relheight=.05)
            self.gamenamelabel=tk.Label(self.root,text='Game Name:',font='bold 12',bg='black',fg='green')
            self.gamenamelabel.place(x=0,rely=.6,relwidth=.2,relheight=.05)
            self.mapsize=tk.Entry(self.root,validate='all',validatecommand=(self.mapsizecmd,'%P'),bg='black',fg='green',insertbackground='green')
            self.gamename=tk.Entry(self.root,bg='black',fg='green',insertbackground='green')
            self.mapsize.place(relx=.2,rely=.69,relwidth=.1,relheight=.05)
            self.gamename.place(relx=.2,rely=.6,relwidth=.775,relheight=.05)
            self.mapsize.insert('0','10')
            if not self.newgame:
                self.joining=False
                self.newgame=True
                hostip=get_ip()
                self.killsoc.sendto(b'11111111101',(hostip,5063))
                self.startnewgameping()
                self.startgetjoinping()

    def callback(self, P):
        if str.isdigit(P) or P == "":
            try:
                if int(P)<201:
                    return True
                else:
                    return False
            except:
                return True
        else:
            return False
    def mapsizecallback(self, P):
        if str.isdigit(P) or P == "":
            try:
                if int(P)<21:
                    return True
                else:
                    return False
            except:
                return True
        else:
            return False
    def namecallback(self,P):
        if ':' in P or ','in P or "/"in P or ';'in P or '`'in P:
            return False
        else:
            if len(P)<20:
                return True
            else:
                return False
    def Joingame(self):
        try:
            self.joined=True
            nothing=self.ipqueueget[self.iplist.curselection()[0]][0]
            self.player=Player()
            self.player.gameip=self.ipqueueget[self.iplist.curselection()[0]][0]
            self.player.Fps=int(self.fpsentry.get())
            if self.player.Fps<30:
                self.player.Fps=30
            self.startjoinping()
            self.creategame.destroy()
            self.joingame.destroy()
            self.iplist.destroy()
            self.startbutton.destroy()
            self.refreshbutton.destroy()
            self.fpsentry.destroy()
            self.fpslabel.destroy()
            tk.Label(self.root,text='Waiting For Host To Start Game...',bg='black',fg='green',font=('bold 25')).place(x=0,y=0,relwidth=.975,relheight=.09)
            self.nameyplacement+=.02
            self.namelabel.place(x=0,rely=self.nameyplacement,relwidth=.2,relheight=.05)
            self.name.place(relx=.2,rely=self.nameyplacement+.01,relwidth=.775,relheight=.04)
            self.playerlist.place(relx=0,rely=self.listboxyplacement,relwidth=.975,relheight=1-self.listboxyplacement)
            self.playerslabel=tk.Label(self.root,text='Players in Lobby',bg='black',fg='green',font=('bold 15'))
            self.playerslabel.place(relx=0,rely=self.listboxyplacement-.05,relwidth=.95,relheight=.05)
            
            self.player.isInitialClientRecv=True
            self.player.startQueue=mp.Queue()
            self.player.gameDataQueue=mp.Queue()
            self.player.server=False
            self.startcheck()
            clientRecvProcess=mp.Process(target=clientrecv,args=(self.player,))
            clientRecvProcess.start()
        except Exception as exx:
            print('Exception in join method of launcher: ',exx)
    def startcheck(self):
        if self.player.startQueue.empty():
            self.root.after(300,self.startcheck)
        else:
            self.player.isInitialClientRecv=False
            self.opengame()
    def opengame(self):
        self.joining=False
        self.newgame=False
        hostip=get_ip()
        self.killsoc.sendto(b'11111111101',(hostip,5063))
        self.killsoc.sendto(b'11111111101',(hostip,5064))
        display.init()
        #set game variables
        if self.mode.get()==2:
            self.player=Player()
            self.player.server=True
            #eventually put map data in the setmap args for transfering maps
            
            self.player.gameDataQueue=mp.Queue()
            self.player.transferGameDataQueue=mp.Queue()
            fps=int(self.fpsentry.get())
            if fps<30:
                fps=30
            self.player.finalname=self.name.get()
            if self.player.finalname.replace(' ','')=='':
                self.player.finalname='Player'
            mapsize=int(self.mapsize.get())
            movementspeed=int(self.speedentry.get())
            self.root.destroy()
            try:
                self.player.finaliplist=self.finaliplist
            except:
                self.player.finaliplist=[get_ip(),]
            serverSendProcess=mp.Process(target=serversend,args=(self.player,))
            serverSendProcess.start()
            serverReceiveProcess=mp.Process(target=serverrecv,args=(self.player,))
            serverReceiveProcess.start()
        else:
            self.player.server=False
            self.player.finalname=self.name.get()
            if self.player.finalname.replace(' ','')=='':
                self.player.finalname='Player'
            fps=self.player.Fps
            mapsize=int(self.mapsizeget)
            movementspeed=int(self.speedget)
            self.root.destroy()
            clientSendProcess=mp.Process(target=clientsend,args=(self.player,))
            clientSendProcess.start()
        self.player.fpslimit=1/fps
        self.player.gridnumber=mapsize
        self.player.setspeed=movementspeed
        self.player.init2()

        self.Map=MapClass()
        self.Map.setmap(1)
        mouse.set_cursor(*cursors.broken_x)
       
        mainloop(self.player,self.Map)

if __name__ == "__main__":
    mp.freeze_support()
    launch=launcher()