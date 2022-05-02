import tkinter
import requests
import bs4
from tkinter import *


global covid19
covid19 = Tk()
covid19.geometry("500x350")
covid19.title("COVID19")
bg = PhotoImage(file = "pic1.png")
label1 = Label( covid19, image = bg)
label1.place(x=0, y=0)
country = tkinter.StringVar()


def submit():
    sub = Toplevel(covid19)
    sub.geometry("500x350")
    sub.title("Details")
    sub.configure(bg="grey")
    name = country.get()
    r = requests.get("https://www.worldometers.info/coronavirus/#countries")
    s = bs4.BeautifulSoup(r.text, 'lxml')
    index = -1
    data = s.select('tr td')

    for i in range(len(data)):
        if data[i].text.lower() == name.lower():
            index = i
            break

    for i in range(7):
        if i == 0:
            Label(sub, text="Country:"+str(data[i + index].text), height='2',bg="grey", font =('freesans', '15')).grid(padx=1, pady=1)
        elif i == 1:
            Label(sub, text="Total cases:"+str(data[i + index].text), bg="grey", font =('freesans', '15')).grid(padx=1, pady=1)
        elif i == 2:
            if data[i + index].text == '':
                Label(sub, text="New cases: 0", height='2', bg="grey", font=('freesans', '15')).grid(padx=1, pady=1)
            else:
                Label(sub, text = "New cases:"+ str(data[i + index].text),height='2',bg="grey", font =('freesans','15')).grid(padx=1,pady=1)
        elif i == 3:
            Label(sub, text = "Total deaths:"+ str(data[i + index].text),height='2', bg="grey",font =('freesans','15')).grid(padx=1,pady=1)
        elif i == 4:
            if data[i + index].text == '':
                Label(sub, text = "New deaths: 0",height='2',bg="grey", font =('freesans','15')).grid(padx=1,pady=1)
            else:
                Label(sub, text = "New deaths:"+ str(data[i + index].text),height='2', bg="grey",font =('freesans','15')).grid(padx=1,pady=1)
        elif i == 5:
            Label(sub, text = "Total Recovered:"+ str(data[i + index].text),height='2', bg="grey",font =('freesans','15')).grid(padx=1,pady=1)
        elif i == 6:
            Label(sub, text = "Active cases:"+ str(data[i + index].text),height='2', bg="grey",font =('freesans','15')).grid(padx=1,pady=1)


Label(bg="#262626", text="COVID-19", height='1', fg='White', font=('lamo', '20', 'bold')).place(x=175,y=10)
name = Label(covid19, text="Country", height='1', font=('freesans', '18')).place(x=195,y=80)
e1 = Entry(covid19, textvariable=country, width='10', font =('freesans','12')).place(x=194,y=120)
submit = Button(covid19,bg='grey', text = "Submit",width='8' , font =('freesans','10'), command= submit).place(x=200,y=200)

covid19.mainloop()
