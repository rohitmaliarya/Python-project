import tkinter as tk
from pathlib import Path
from PIL import Image,ImageTk #pip install pillow
import requests

def showtext():
    text = txt_box.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + text + "&appid=34aa61b195fe115fdac6b774c184873e&units=metric"
    data = requests.get(url)
    weather = data.json()
    detailslabel.config(text=f"Temperature is: {weather['main']['temp']}\nWeather: {weather['weather'][0]['main']}\n humidity: {weather['main']['humidity']}")
    

root=tk.Tk()

root.title("WEATHER APP")
root.geometry("600x500")



Img=Image.open(Path(r"C:\Users\user\Desktop\tk_project\my-venv\bg.jpg"))  
# Img=Img.resize(600,500)
Img_photo=ImageTk.PhotoImage(Img) 

bg_1b1=tk.Label(root,image=Img_photo)
bg_1b1.place(x=0,y=0,width=600,height=500)

txt_box=tk.Entry(root,font=('timesnew roman',25),width=18)
txt_box.place(x=150,y=230)

label = tk.Label(root, text="Enter City Name:", font=("algerian", 28), bg="#fae76a")
label.place(x=150, y=150)

button = tk.Button(root, text="SUBMIT", font=("Roboto", 18, "bold"), command=showtext)
button.place(x=250, y=280)

detailslabel = tk.Label(root, text="", font=("calibri", 15, "bold"))
detailslabel.place(x=200, y=350)


root.mainloop()