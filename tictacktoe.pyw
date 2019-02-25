from tkinter import*
from time import sleep
if __name__ == "__main__":
    new=True
    root=Tk()
    root.title('Tic Tack Toe')
    burgerstring=(b'R0lGODlhZQBRAPcAAEUXEUsaE0oeFlMdFU4jGkwiF1glGlkzHm4jFGcoF3IlFnUpF3MsHHorGXwyHFgsJFs1Jl88MWUsInMvIWwxJWc3LXc2KGk9M3g9MVZBHnxBHl1SIVxIJWZHKGVaJ2hENX1ENXZFNWlcMXZYNXVSK3dlLnpsO3VpNn1yOG9lLnlWT3lwQI84H4g0HZI6H4Q8K4c6JJQ9I5s8Ios/MKg9JLA/JYhFK5RELJZGKYxEMY5LNoVHM5dINIxWOphYOJJTKadJKLVDJrpHKKdUK7VaKaxMNLdONKhXObhVO4ZlK4N1LYp6L4t0LYdmO5hoOI5/MIh6OZV7Npl1LqZpO7hnOKd7ObZ4O6VrLolCH8JGKMRKKstPKM1SKsdVLtBTKNNbKcRSNcpTMcxdPMdZONJbMtBeOcNNMNtrKtx1K8ZmOdNhNtdqOcV4Pd1yNNd1PMFiLeFvJuR1JeZ6JuV7LON4KOV9NJZbSYhUQa1bQpJpQYl6RZd4QotqSapnR6d8Q7Z6RrNoSbJ2ZMteQc1pRNZtQtNnQch4R9J7Rtd3Rdt8W8ltUI6COZKDM5OFO5iKOZ6TOKWZN6mfOKOWOLSHOKygPrChPtmNO86LOOmELOiCLPGUKPKZLumJNu6UOe6WOPGaNPGbO/GXMPSjPfaqO/itOfeqNvqzO+umO9qkOJqCRZuMQpWHSJ6SR4mAQqWLRbWJRaKTRKiYSa+QUayiR7KmTLyjVbmxXbWPbbmubcqESdeESMuLUtiHU9GaUuiLROqVROuZUtGkTe2lSPOkQ/SpSPm2RPWxTPi3SeylVfKsVvq9U/W3V+63V9uLZ92cdNWXaeGcaeKTeNWybvS4ZOSmevO9eOmvbfnEXfnAVd3Dc/nFZPrJbPvGavrNdPrOevfNf/nRfeHCd762irmopcebj9KwmOaok+61j9S3r+q7p/jLg/nTg/bUifvZl/HNid7ZuNfGr/LTsfvjtM3Gl9rRyPTVyeza0Pzoxfnn2P3w2OjmzfXq5f315fv18v/69AAAACH5BAEAAP8ALAAAAABlAFEAAAj+AP8JHEiwoMGDCBHWq2eu3sB95hou7JewosWLGDMe3MfQXDpCZRJ5GUnSizlgwNqUHEmm2blz/DTKnEnzX7900cis3Fnyy5w6br54OXNmpM84SKeBGlbN3b17//zVnCrT3j57irJk0cmzK8s1dZCKHYtJk9mzmoYpayeVqluC9uDdusECida7YbZsCcPV68g2dOiMHQwK7dlhxUwdY/uWKjm6LljQsHu3cpYxYUpquatlC8k2g0MbPjvKlGnF8hrL7EcPHQsgSMxY1gpGkOeRt70I0pp3Z2jCaJeeHm6KW1vVFdHRZQFmtlYzmUuG4b3lrpe+JMP+RvrrMPHvx9b+5UO+MRALFi6az8bMc/rsNSq9fJkPenscOYXNkvr+Xds1eceR99h5LBThXBZhiCGGIAvutdtsZcAxhy9wyGEfUnJwEgpapfF32jUgXtNNTMj1AwiB58l24IoIjlTIGheOJQcm+RnWoYemYBPiNdqQ+FY/fcBAYAxGsMhiX4TEeF+No32C43D+hehNgDX1o8gYBMpQpJEHalESHBdi8slohu1HXDGJQbnjNe28ZU4WSLAgg3pcHlgGSWRcKMeGZKJlpmnKhLiNMqdFuSNUVDWHBGV1OqeFTrcl+ZscnfRp43CBrqnNpmuCmNpU6bjXaJd3loTIpHxaqkkof5rS6av+IXazzjo+zpTIIKMeuAV2I0kq4yaqkqbmjt10A+s14MzK2Ez9qDEGb6KGUUghoh7IK0m+isWkpaKclmmsya4DjrGdejPrOojKFA8hmwlBBhm8lVTGiqXyVJ9YlQZrVimmFSMoOOGeuw65IG7TTcDsUHmROWsUIsi18s7Gl1d5DqbvWadxU3DAAs/qDY/hsiNwrRil4waeJamhxkpllLHZGH55cS9SY16syWnbgKgNxx333DHJFzlz8khnwLHGUEitvBPE8pEEplhy2GxWxrH6bPXPMzlzyGdPiwWHG4QQEjMZ8CFyRmj52mwmsSJffTXQTyVEzSGEqNFG17+1cfT+0mvgPRgdUmvSbb878uz2ueDEtM888/xzzzrsAC1QPIcc4obfobVxrRoVXpi2voN/WPXhPrODCyNPMNLOuekK1M8789hCCS+HIMKJkmeYHccaMMYYtc2hiy4l6R3X0kgjrLAizcgF9dNILJFEv4shleviyxxKbmch1Knqyy9xa8pK/KyxMMIIJNFnc+54Bb0TTi2OVBL9CRuY4IQhiCDii3bZY0hpKNuy1DBEMYz+hI944dDDBjzACElELxKUgBz7HtIIRixvVrSIHiPoVz8/IKJ2urhd/wIYLA99ixuG6xg72CELBZaggox4YCRwASCD6CN1jHDEI+THClWYTwn+q4ieCS7wgRDcgQ394wSw0ALAJY4meMLjRs8CJg1Z8OEDADiAHhxhPvM94oHvSIg4lsAIMqIPdU9II/Qi0QQAAIAAH/iAH+JAhDvogAhEONukOgEKUIgwDp7okyhKQchRlIIUyliGMhYJIm6Q6xkqgIAbAVCAAnRgCWnEYSRsscJ1tGOCBNGHLR6BvuhJwhGZVAUUPLABDmRgA7DkQBM+IMlJAiAAD8DABS4Qgjy4ohKyqEQsYqEKVcDiEbBI5iNe4YpXONOZftiDH1KxB2rm4Q60fEAqSHCADjQBFqwwASzrl0lGfHF54WpTQaQhw+hxkRGrWAQKxrlAE6CAlSf+uAUrNvABE4gAliLggC0HmsUToCACCE3oBbDggx2AAAQYEIAbPxCBOFb0Ax1QQibTOItISGIRKYAlGtPIikhkIxsrJNk72hmJRdCTnilAARkZMc9azEoPKHjCEkIKUAgc4KcFEMEqYsGKLpbgAJMkQBNoUcYSlACLH8DkRslIxkegbgQRAIAJHvgIKIw0jQ2MxCzCWJB8vAMXMoQEFDi4AYNStYtK2AArRFYLBqZxCeLcgEbTGD1IoO+d9POACExASlpslBEk+OpdzddRWKSAlgB4QDsp8U6dom4eFEkIP+ChhxUswnwzXWwZGaGEkIqAHd+gxCy+uoS9gnUWsC3+3049QNtSRsKwG81tJkO6CFPSMwNLYGn5bOEOdziiHPi4CCxXYc6vjpam4/RALToaCVgo9rAzNd9nzVfSB+JWtxuNKyxVQYlIOIKVsOwtS2Fxrl0cgheZRQg9NlCC6K3WfKIVLyxT8YQvehS8mZzpTCMBCe7K8LtKyKlu9euBNTIClidohH07qtpY8MIa6tBF5cxREXFEgQVW2MUD7ztTJZAgvZmcBSVGqgQ9QMG1NO1iDCVBxu5GrxUvdW0ak7CAE29gjdF7hBLotwqrvlUVlUvyIeKRkHc8wQkuAEIuJvHAV/yhjEuwQuVoqmAliEDBT2DrSx/BRf8+Yp7pZQT+K9AMYd32gAEI6IAHZlELK/zAFYxohBWswIY/vMIRZESykp2hMJto7RU3AANJ1JALK2QhyVS4wQerQM4niPcEaczrS2Ep4QdSAs0i6MATYBGJDXQAAQhIAKonkISNPlQEQ+hCF4IwBCc84RVpOIQ6qsGLScgiF0pOR0KeUTlDTMEFMCNJIR59CCocAQeyJoIHwPzPSqPAoHpYBU9/zFJHHBUAHUAflF0QAx7wwAUKQIAf/kAFIggBCLMRwroHcYhzQSPJugBGNQrtD1y4onKueIIPXJAGkrhMC13AgQuCcJcjSJUKQigBLJdA1SesEZZzTqv59FAAN47AozGIDHr+YICAG+SKENaYlTUOYYhfnKYY36jhQPRhPlf8IeBLcIIOGgCzzayICH6gQha0IIQmmOCtSSB1qTdAYEiwIhbIZAQUJDpJRxC4ClPAAQ9QnQNzM3xFNKBBEY7gAxwMYQqVI85+lJGuG3YxjT5gQA9QrQAFWIAHePC5EMJOgxrcRQhBYLgFUI3qJKBvAwLuoiNGIAAB0EUCABAAH4CsAcIT/gZjwAGBWoAByzuAQD/Qsi5wNCWBiKN8qGOEIRDAAAtIYAC2HEAOHGB5VLcAPeiZAeEtsAMbMAIWG9hudjsAAAmEnNwBCLkNWoAFLIz9CEfAgw+ooOTK8cIQQJBBC27+fx5bazkYqEBFMGpRi2AMc5jBIOs/6BHPMoIgAASNvAFqvwAWxKAIi4oNilhwAwSQwKv45QRYgCI8cARFEARCYAQuUARiUC8k8UHVVzlD4wVbEAM40AhpZAWTgF9p9AiSIAlExQqQQAkDoQJuZAAVUEuTJAAQwAc6tQB0twA5wAJbohVCsH+0539O0AQ2gAAziCJCsCJmUBKEEIFJNjRcIANOMFKMgAaDcQmQ8IEyVILx50YEEAVphIVJ0HUwCAOR4QKTgQQygCL9V3tch3v8F4QrEh1eoAZu4AZssAaIUIQsZ4At8AKfJQVY2AiXMBhwcAmp9ECuYwc6AHvxNwL+T/Bvu/Bh59F/CvAC5yZyQ5JuZogACnBuBGJyK+IVnoEEO4BqGiAFUsAGXBE2hOAGnJCKnDAMk5BJ4lAQ+3AeFFCFkfUHk6ALr+AE5uYDPcADuqcAC+AAWHADOvAClFiJdEeGRaCGlaFoJTEG0IcHMdAAqMYAUWAFPfEFbcAJnZAM58IOplAMaAQPBVEO52EAtPhGTxAFu3BYTuADTdAEPSCPOwBnyFh7PrB/RLIod5FsggAEMaADhHd7SMAGE3gGnQAsxGAKpWAM3tA23GAaqIBJuFAQ5HAePLADvgh/BNUEjPAK7QhWzpV6TJAE9LgDn1h7E4ABDiUBBsCRA/X+ABWwAzFABG6ABm4wBEBABdgzB7/wC9uykE8SDFGgfgIBD0JyHgZiBDlgiEnVCFFwCFiYSanABHngBHlQTamAgamwCquwBz0AAQ9AUPBXABUQARWQli6ZAAtQBHeTL4O0CZvwOaNhCT0wBXsmDMjwHWxwA/tgEOZ4HukRJzNAUB3ACIdQBU+wB5V3j475mKjGAmlwH3QQNZuQJqdxFpZgCWhBBQiAAegIAIR3BadhDDHQAuhwEDyAIjEgiwFgAIYYABBgCIBgj5AJmQuQBoOAB2ZHBWwwB5kwDMOgCaDAJ6NADMGADMEQDH9AAaGJAbXmA6hmAw11AbY5BaZBBXb+kJoHcZEskJQo8gIIAHluNAAwaHkr6QM80HxYYJuVuAA/YAn9YgzCIAzGwAlzIAeJMQqbwJC+kAs7QIsPQHgEwHr4UzmKcAQxkG4OcAsX8RgwAAMMoAAococYMIsDQHigyZED8AenYBq/kAtHwALn+XlUcAlnQQzKcAzaoDEhcgwMOQykIAwBSosFQJt054PUd6BdoBVGgGp2gBHoIAAUAGfcdx4tAGduFABOOVB/YBqlQAyjYDPcsA1WCiKmQQx+gFTpCAB9UDktgAAvQD3NNgSV43NZQI1BihHjQAABIAEWcB4WgAETEKa2RAETQAEw6UZPOhw10yehwC+iMAn+ebALz7CltxQAAVAAe2pLIZBkgDCd0jeiR5AGdxEEOnAL9KAR9BBJkaWCE4AA5TkBlDgBBNWnpzEKf4oWm7AfPkAA8ReqqwYCOwCrkxQAFqBktWcD/dd1BchhNdEMgEB1t0QBFzp4CDB/qEaeKygM30EKpFAKogAsrXoKWDQAF6Cnk0QBtdcC1FMB24oAR5BktKcA1HiMCuADzABKMlFsIDCWigoAFECJBKCsCDABF4ABFYCOAhAMOMKfpDAJsMqt1YiOyqoAN7ADL9ACgHAIJCcBAoABMzB91HcEOeAC6EZ4PoAMIMKuGpFk0KAO7sAH6BgAFdB5jrkAkYeZ/OH+A/Bnr4S3dTI4CHGCHjFwCDlYcqx5bjGQA0AqC9eQKYWGEdDAC7wADG2zDrdAnhnqmBJ1ADcyHKcQAuFaezwgAwwAA0hwIiwwA8ZoeQjLf7S3mummA8szDaKgCcugTjVxDryAFJmgDgIjDSMwrwhgAQOAgug5SSTwHagArrYkq6i2AH6XBUIQA5jaAsdYe5RoAU7wDNKQct2gDMRgFsfwKTXhD7yAPXGQCcTgjefyDDpgAQSQty9pABZgAcQKAE4wHJfQcWSJsi9QA3hAJzHAuA7wAoAACHiAB88gMN2gDaZxDGahDkObEecANZrQCdPQDXI7K7vQByiiA8xqS87+agqXYKtViKvjGXlIUANBiARFoAM6oAhKpgsYlizgoA0wOhybkAyNgQ/aETXbEwfJoA3ekDPX0Au5QAUAeQR9MLp3AAIGsAOWYAXau6SNeksPoAM7gAEyMAZnQAh9Qwe80AzQYA3VcC7dgLab8AnGYAynsQmY6xb3IBahQAeYsD2YMAzT0CnLAAy3AwdvgAQKJ6chgAEPpQM9cAc93ANArAN3cARUMJliUQfIkMQb3DHDORrFEMKt8xb1UAeCgRShsAmYMBaZIAzTYChBS5+/4As/mQZTQAVOeCGcEMa+IMa/ALoeUyzaMA2340SaUAyfQECaUA3k4TrUADWgUL/+f8MJwpAMMBoo2qAM2JDI12AMSYwM9hnCIfwqm7IpyUCfg+wJnFsWZ1EMoAC3JbzH9fBH2YMfwrAMIvwk/bJI0zANydDKrtzKmNAJgCwHfxoKosxke2wQyds/v5EJvpwJnEAMwkwMwjAMxAAKnIsUVWwfcuBEoVC/wJBcuXwQ8ZDMvBwjmNM/cNAGvtAGZyBCvoDL05wQ+HAO/HPN6Bwa2xw2vAIN9RBf43wR8XAOwJDO2mw0c8g0XtAM6QDP8awu96YLvKALaADI27E3bUgIhaDPXrAGRpsIicDP/vzPU2EP6UANtIMIRqsLSAEHXLEGSsMT17IGzeAM6SDNFD0nzvtwDs7Q0tQgEjHjBRA909HgEe+c0jh9EPiwEDzd0/WA0jl9EAEBADs=')
    ico=PhotoImage(data=burgerstring)
    root.tk.call('wm', 'iconphoto', root._w, ico)
    w = 510 
    h = 550
    ws = root.winfo_screenwidth() 
    hs = root.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    os=0
    xs=0
    serve='h'
    l=Label(root,text='X:  '+str(xs)+'                                               O:  '+str(os),font=('bold 20'),bg='grey',fg='white')
    l.pack()
    c=Canvas(master=root,width=500,height=500)
    c.pack()
    c.create_line(0,0,0,500,width=10,fill='black')
    c.create_line(0,500,500,500,width=5,fill='black')
    c.create_line(0,0,500,0,width=10,fill='black')
    c.create_line(500,0,500,500,width=5,fill='black')
    c.create_line(0,166,500,166,width=5,fill='black')
    c.create_line(0,333,500,333,width=5,fill='black')
    c.create_line(166,0,166,500,width=5,fill='black')
    c.create_line(333,0,333,500,width=5,fill='black')
    hlist=[0,0,0,0,0,0,0,0,0]
    counter=0
    gameend=False
def click(xy):
        x,y=xy.x,xy.y
        if x<166:
            if y<166:
                coord=1
            elif y<333:
                coord=2
            else:
                coord=3
        elif x<333:
            if y<166:
                coord=4
            elif y<333:
                coord=5
            else:
                coord=6
        else:
            if y<166:
                coord=7
            elif y<333:
                coord=8
            else:
                coord=9
        draw(coord)
def draw(bnum):
    global hlist
    global counter
    global gameend
    global l
    global c
    global xs
    global os
    if hlist.count(0)==0:
        gameend=True
    if not gameend:
        if hlist[bnum-1]==0:
            counter+=1
            if counter%2==0: #player 2 circles
                hlist[bnum-1]=2
                wincheck()
                if bnum==1:
                    c.create_oval(20,20,146,146,width=5,outline='red')
                if bnum==2:
                    c.create_oval(20,186,146,312,width=5,outline='red')
                if bnum==3:
                    c.create_oval(20,352,146,478,width=5,outline='red')
                if bnum==4:
                    c.create_oval(186,20,312,146,width=5,outline='red')
                if bnum==5:
                    c.create_oval(186,186,312,312,width=5,outline='red')
                if bnum==6:
                    c.create_oval(186,352,312,478,width=5,outline='red')
                if bnum==7:
                    c.create_oval(352,20,478,146,width=5,outline='red')
                if bnum==8:
                    c.create_oval(352,186,478,312,width=5,outline='red')
                if bnum==9:
                    c.create_oval(352,352,478,478,width=5,outline='red')
                
            else:            #player 1 X's
                hlist[bnum-1]=1
                wincheck()
                if bnum==1:
                    c.create_line(20,20,146,146,width=5,fill='blue')
                    c.create_line(146,20,20,146,width=5,fill='blue')
                if bnum==2:
                    c.create_line(20,186,146,312,width=5,fill='blue')
                    c.create_line(146,186,20,312,width=5,fill='blue')
                if bnum==3:
                    c.create_line(20,352,146,478,width=5,fill='blue')
                    c.create_line(146,352,20,478,width=5,fill='blue')
                if bnum==4:
                    c.create_line(186,20,312,146,width=5,fill='blue')
                    c.create_line(312,20,186,146,width=5,fill='blue')
                if bnum==5:
                    c.create_line(186,186,312,312,width=5,fill='blue')
                    c.create_line(312,186,186,312,width=5,fill='blue')
                if bnum==6:
                    c.create_line(186,352,312,478,width=5,fill='blue')
                    c.create_line(312,352,186,478,width=5,fill='blue')
                if bnum==7:
                    c.create_line(352,20,478,146,width=5,fill='blue')
                    c.create_line(478,20,352,146,width=5,fill='blue')
                if bnum==8:
                    c.create_line(352,186,478,312,width=5,fill='blue')
                    c.create_line(478,186,352,312,width=5,fill='blue')
                if bnum==9:
                    c.create_line(352,352,478,478,width=5,fill='blue')
                    c.create_line(478,352,352,478,width=5,fill='blue')
    else:
        l.destroy()
        l=Label(root,text='X:  '+str(xs)+'                                                O:  '+str(os),font=('bold 20'),bg='grey',fg='white')
        l.pack()
        c.destroy()
        c=Canvas(master=root,width=500,height=500)
        c.pack()
        c.create_line(0,0,0,500,width=10,fill='black')
        c.create_line(0,500,500,500,width=5,fill='black')
        c.create_line(0,0,500,0,width=10,fill='black')
        c.create_line(500,0,500,500,width=5,fill='black')
        c.create_line(0,166,500,166,width=5,fill='black')
        c.create_line(0,333,500,333,width=5,fill='black')
        c.create_line(166,0,166,500,width=5,fill='black')
        c.create_line(333,0,333,500,width=5,fill='black')
        hlist=[0,0,0,0,0,0,0,0,0]
        gameend=False
def wincheck():
    global hlist
    global gameend
    global xs
    global os
    l=hlist
    if l[0]==1 and l[1]==1 and l[2]==1:
        c.create_line(83,0,83,500,width=5,fill='green')
        gameend=True
        xs+=1
    if l[3]==1 and l[4]==1 and l[5]==1:
        c.create_line(249,0,249,500,width=5,fill='green')
        gameend=True
        xs+=1
    if l[6]==1 and l[7]==1 and l[8]==1:
        c.create_line(415,0,415,500,width=5,fill='green')
        gameend=True
        xs+=1
    if l[0]==1 and l[3]==1 and l[6]==1:
        c.create_line(0,83,500,83,width=5,fill='green')
        gameend=True
        xs+=1
    if l[1]==1 and l[4]==1 and l[7]==1:
        c.create_line(0,249,500,249,width=5,fill='green')
        gameend=True
        xs+=1
    if l[2]==1 and l[5]==1 and l[8]==1:
        c.create_line(0,415,500,415,width=5,fill='green')
        gameend=True
        xs+=1
    if l[0]==1 and l[4]==1 and l[8]==1:
        c.create_line(0,0,500,500,width=5,fill='green')
        gameend=True
        xs+=1
    if l[2]==1 and l[4]==1 and l[6]==1:
        c.create_line(500,0,0,500,width=5,fill='green')
        gameend=True
        xs+=1
    if l[0]==2 and l[1]==2 and l[2]==2:
        c.create_line(83,0,83,500,width=5,fill='green')
        gameend=True
        os+=1
    if l[3]==2 and l[4]==2 and l[5]==2:
        c.create_line(249,0,249,500,width=5,fill='green')
        gameend=True
        os+=1
    if l[6]==2 and l[7]==2 and l[8]==2:
        c.create_line(415,0,415,500,width=5,fill='green')
        gameend=True
        os+=1
    if l[0]==2 and l[3]==2 and l[6]==2:
        c.create_line(0,83,500,83,width=5,fill='green')
        gameend=True
        os+=1
    if l[1]==2 and l[4]==2 and l[7]==2:
        c.create_line(0,249,500,249,width=5,fill='green')
        gameend=True
        os+=1
    if l[2]==2 and l[5]==2 and l[8]==2:
        c.create_line(0,415,500,415,width=5,fill='green')
        gameend=True
        os+=1
    if l[0]==2 and l[4]==2 and l[8]==2:
        c.create_line(0,0,500,500,width=5,fill='green')
        gameend=True
        os+=1
    if l[2]==2 and l[4]==2 and l[6]==2:
        c.create_line(500,0,0,500,width=5,fill='green')
        gameend=True
        os+=1
root.bind('<Button-1>',click)
root.mainloop()