from tkinter import *
import time
import os
import psutil
import platform




app = Tk()
app.title("Benchmark by python")

# Add image file
bg = PhotoImage(file = "CPUTestBackground2.png")
  
# Show image using label
label1 = Label( app, image = bg)
label1.place(x = 0, y = 0)

# Screen manage
app.geometry("1200x675")
app.minsize("1200","675")
app.maxsize("1200","675")
app.config(bg="black")


user = platform.uname()
print(f"OS : {user.system}")
print(f"OS : {user.processor}")


print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

memory = psutil.virtual_memory()
total1 = round(memory.total/1024.0/1024.0/1024.0)


disk = psutil.disk_usage('/')
total2 = round(disk.total/1024.0/1024.0/1024.0)


myLabel1 = Label(text=f"Total cores : {psutil.cpu_count(logical=True)}",font="Consolas 18",fg="#21ef80",bg="black").place(x=270,y=320)
myLabel2 = Label(text=f"RAM {total1} GB",font="Consolas 18",fg="#ff63d8",bg="black").place(x=550,y=320)
myLabel2 = Label(text=f"Disk : {total2} GB",font="Consolas 18",fg="#ffd707",bg="black").place(x=760,y=320)
myLabel2 = Label(text=f"Version 2.0",font="Consolas 10",fg="green",bg="black").place(x=900,y=670)

cpuScore = 0
memoryScore = 0
diskScore = 0


def memory():
    a = []
    start = time.time()
    while True:
        a.append(list())
        #if a.__sizeof__() > 107345:
        if a.__sizeof__() > 1073741824 : 
            break
    print(f'memory use {time.time()-start} second')
    global memoryScore
    memoryScore = 300000/(time.time()-start)
    overallUpdate()
    Label(text=f"{memoryScore:.2f}",font="Consolas 16",fg="#21ef80",bg="#ff63d8").place(x=540,y=415)

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
        #if i == 10000:
        if i == 100000: 
            break
        checkPrime(i)
        i += 1
    print(f"cpu  use {(time.time() - start)} second")
    global cpuScore
    cpuScore = 1000000/(time.time()-start)
    overallUpdate()
    Label(text=f"{cpuScore:.2f}",font="Consolas 16",fg="#585eff",bg="#21ef80").place(x=310,y=415)
    
def disk():
    start = time.time()
    garbage = bytes(1073741824) 
    with open("file.xxx", "wb+") as file:
        for _ in range(10):
            file.write(garbage)
    global diskScore
    diskScore = 100000/(time.time()-start)
    overallUpdate()
    file.close()
    os.remove("file.xxx")
    print(f'disk use {time.time()-start} second')
    Label(text=f"{diskScore:.2f}",font="Consolas 16",fg="#585eff",bg="#ffd707").place(x=790,y=415)

def overallUpdate():
    return f"{(1.5*cpuScore + memoryScore + 0.5*diskScore)/3 :.2f}"

def start_bench():
    cpu()
    memory()
    disk()
    Label(text=f"{overallUpdate()}",font="Consolas 16",fg="#edb469",bg="#5ce6dd").place(x=665,y=515)


photo = PhotoImage(file = r"StartButtonFinal.png")
Startbutton = Button(app, image = photo,command=start_bench,borderwidth=0,bg = '#8488f4').place(x=465,y=226)

app.mainloop()