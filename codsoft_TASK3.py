import  requests
from tkinter import*
from tkinter import ttk

def  get_data():
         city=cityname.get()
         data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=099e60f85b4c3e433478c4addbeccd31").json()
         weather1.config(text=data["weather"][0]["main"])
         Descrip1.config(text=data["weather"][0]["description"])
         temp1.config(text=str(data["main"]["temp"]-273.15))
         pres1.config(text=data["main"]["pressure"])

w=Tk()
w.title("WEATHER APP")
w.geometry("1100x400")
w.configure(bg="skyblue")
w.resizable(0,0)

head=Label(w,text="WEATHER APP",bg="skyblue",fg="white",font=("segeo print",20,"bold"))
head.place(x=150,y=50,height=50,width=800)

cityname=StringVar()
combobox=ttk.Combobox(w,font=("segeo print",10,"bold"),textvariable=cityname)
combobox["values"]=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
combobox.place(x=150,y=120,height=30,width=700)

weather=Label(w,text="WEATHER ",bg="blue",fg="white",font=("segeo print",10,"bold"))
weather.place(x=100,y=200,height=30,width=150)
weather1=Label(w,text="",bg="blue",fg="white",font=("segeo print",10,"bold"))
weather1.place(x=100,y=300,height=30,width=150)

Descrip=Label(w,text="DESCRIPTION",bg="blue",fg="white",font=("segeo print",10,"bold"))
Descrip.place(x=350,y=200,height=30,width=150)
Descrip1=Label(w,text="",bg="blue",fg="white",font=("segeo print",10,"bold"))
Descrip1.place(x=350,y=300,height=30,width=150)

temp=Label(w,text="TEMPERATURE",bg="blue",fg="white",font=("segeo print",10,"bold"))
temp.place(x=600,y=200,height=30,width=150)
temp1=Label(w,text="",bg="blue",fg="white",font=("segeo print",10,"bold"))
temp1.place(x=600,y=300,height=30,width=150)

pres=Label(w,text="PRESSURE ",bg="blue",fg="white",font=("segeo print",10,"bold"))
pres.place(x=850,y=200,height=30,width=150)
pres1=Label(w,text=" ",bg="blue",fg="white",font=("segeo print",10,"bold"))
pres1.place(x=850,y=300,height=30,width=150)

submit=Button(w,text="SUBMIT",bg="green",fg="white",font=("segeo print",10,"bold"),command=lambda:get_data())
submit.place(x=850,y=120,height=30,width=100)

w.mainloop()

