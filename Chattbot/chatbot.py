from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import Image, ImageTk
import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('rate', 120)
engine.setProperty('volume', 0.9)
engine.setProperty('voice', voice[0].id)

window = Tk()
window.configure(bg='gray0')
window.title('ChatterBOT')
window.geometry('900x720-1+1')
bot = ChatBot('xox')
# bot_response = bot.get_response("hi")
# print(bot_response)

trainbot = ListTrainer(bot)
con = open('convo.txt')
trainbot.train(con.readlines())

"""while True:
    user = input()
    bot_response = bot.get_response(user)
    print(bot_response)
"""

Tops = Frame(window, bg="paleTurquoise4", height=100, bd=5, width=200, pady=4, padx=4, relief=RAISED)
Tops.pack(fill=X)
img = Image.open('robot.jpg')
img = img.resize((150, 70), Image.ANTIALIAS)
img_resize = ImageTk.PhotoImage(img)
lbl = Label(Tops, image=img_resize, bd=10)
lbl2 = Label(Tops, text='.....Hellow user i`m XOX..How may i help you !', font=("comic", 25, "bold"),
             fg='lawn green', bg='gray63', bd=5)
lbl2.pack(side=RIGHT)
lbl.pack(side=LEFT)

mainframe = Frame(window, bg="dark slate gray", bd=10, width=500, height=200, relief=RIDGE)
mainframe.pack(side=LEFT)


def convertation():
    user = que.get()
    answer = bot.get_response(user)
    msgs.insert(END, "YOU : " + user)
    msgs.insert(END, "XOX : " + str(answer))
    speak(answer)
    msgs.yview(END)

    que.delete(0, END)


def speak(word):
    engine.say(word)
    engine.runAndWait()


def enter_btn(event):
    btn.invoke()


topframe = Frame(mainframe, bd=5, bg="slate blue", relief=RAISED)
sc = Scrollbar(topframe)
msgs = Listbox(topframe, bg='gray12', fg='lawn green', font=("comic", 15, "bold"),
               width=75, height=20, yscrollcommand=sc.set)
sc.config(command=msgs.yview)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH)

topframe.grid(row=0, column=0)

btmframe = Frame(mainframe, bd=5, bg="gray6", relief=GROOVE)
que = Entry(btmframe, font=("comic", 15, "bold"), bg='gray63', fg='red4', width=65, bd=2, relief=SUNKEN)
que.pack(side=LEFT, fill=X, pady=10)
btn = Button(btmframe, text='send', bg='SteelBlue4', fg='lawn green', font=("comic", 15, "bold"), relief=GROOVE,
             width=10, bd=3, command=convertation)
btn.pack(side=RIGHT, padx=5)
btmframe.grid(row=1, column=0)

window.bind('<Return>', enter_btn)

window.mainloop()
