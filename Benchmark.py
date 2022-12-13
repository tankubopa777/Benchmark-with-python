from tkinter import *
import time
import os
import psutil
import platform

# from PIL import ImageTk, Image


app = Tk()
app.title("Benchmark by python")

# Picture manage
# imagebg = Image.open("C:\\Users\\tankubopa\\Desktop\\CN210\\bgpic4.jpg")
# backgroundImage = ImageTk.PhotoImage(imagebg)
# lbl = Label(app,image=backgroundImage)
# lbl.place(x=0,y=0)

# Screen manage
app.geometry("1000x700")
app.config(bg="black")
#app.maxsize("450","300")
#app.minsize("450","300")

myLabel1 = Label(text="The Hackerman! Computer Benchmark Program",font="Consolas 16",fg="green",bg="black").place(x=350,y=60)
myLabel2 = Label(text="We will hack your computer...",font="Consolas 16",fg="green",bg="black").place(x=350,y=100)
myLabel2 = Label(text="We know your computer spec",font="Consolas 16",fg="green",bg="black").place(x=350,y=140)

user = platform.uname()
print(f"OS : {user.system}")
print(f"OS : {user.processor}")


print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

memory = psutil.virtual_memory()
total1 = round(memory.total/1024.0/1024.0/1024.0)


disk = psutil.disk_usage('/')
total2 = round(disk.total/1024.0/1024.0/1024.0)


myLabel1 = Label(text=f"Total cores: {psutil.cpu_count(logical=True)}",font="Consolas 16",fg="green",bg="black").place(x=350,y=180)
myLabel1 = Label(text=f"Physical cores: {psutil.cpu_count(logical=False)}",font="Consolas 16",fg="green",bg="black").place(x=350,y=210)
myLabel2 = Label(text=f"RAM {total1} GB",font="Consolas 16",fg="green",bg="black").place(x=350,y=240)
myLabel2 = Label(text=f"Disk : {total2} GB",font="Consolas 16",fg="green",bg="black").place(x=350,y=270)
myLabel2 = Label(text=f"Version 1.1",font="Consolas 10",fg="green",bg="black").place(x=900,y=670)

cpuScore = 0
memoryScore = 0
diskScore = 0

def memory():
    a = []
    start = time.time()
    while True:
        a.append(list())
    #1 gb
        if a.__sizeof__() > 1073741824 :
            break
    print(f'memory use {time.time()-start} second')
    global memoryScore
    memoryScore = 1000000/(time.time()-start)
    overallUpdate()
    return Label(text=f"Score :{memoryScore:.2f}",font="Consolas 16",fg="green",bg="black").place(x=400,y=400)

def checkPrime(n):
    c = 0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return True
    return False

def cpu():
    start = time.time()
    i = 1
    while True:
        if i == 100000:
            break
        checkPrime(i)
        i += 1
    print(f"cpu  use {(time.time() - start)} second")
    global cpuScore
    cpuScore = 1000000/(time.time()-start)
    overallUpdate()
    return Label(text=f"Score :{cpuScore:.2f}",font="Consolas 16",fg="green",bg="black").place(x=400,y=330)
    
def disk():
    start = time.time()
    garbage = bytes(1073741824)
    if os.path.exists("file.xxx"):
        os.remove("file.xxx")
    with open("file.xxx", "wb+") as file:
        for _ in range(10):
            file.write(garbage)
    print(os.path.getsize("file.xxx"))
    file.close()
    print(f'disk use {time.time()-start} second')
    global diskScore
    diskScore = 1000000/(time.time()-start)
    overallUpdate()
    return Label(text=f"Score :{diskScore:.2f}",font="Consolas 16",fg="green",bg="black").place(x=400,y=470)

def overallUpdate():
    allScoreLabel = Label(text=f"Overall Score :{cpuScore + memoryScore + diskScore :.2f}",font="Consolas 16",fg="green",bg="black").place(x=400,y=540)
    return allScoreLabel

CPUbutton = Button(app, text = "Benchmark my CPU",width=20,height=2,font="Consolas 12",fg="green",bg="black",command=cpu).place(x=100,y=320)

Membutton = Button(app, text = "Benchmark my Memory",width=20,height=2,font="Consolas 12",fg="green",bg="black",command=memory).place(x=100,y=390)

Diskbutton = Button(app, text = "Benchmark my Disk",width=20,height=2,font="Consolas 12",fg="green",bg="black",command=disk).place(x=100,y=460)


app.mainloop()