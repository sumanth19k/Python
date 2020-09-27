from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title("weather reporting")
root.geometry("700x300")
root.configure(bg="blue")



def search():
   
    try:
        
    
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() +"&distance=25&API_KEY=1999DBA3-8C94-432E-9D5F-5F037A9334DD")

        api = json.loads(api_request.content)
        value = api[0]['AQI']
        area    = api[0]['ReportingArea']
        quality = api[0]['Category']['Name']
    
        if quality == "Good":
            
        
            color="#0C0"
        elif quality == "Moderate":
        
            color="#FFFF00"
        elif quality == "Unhealthy for Sensitive Groups":
            color="#FF9900"
        elif quality == "Unhealthy":
            color="#990066"
        elif quality == "Moderate":
            color="#660000"
        root.configure(background=color) 
        my_label=Label(root,text=area +"  "+"temparature is "+" "+str(value)+" centigrate"+"  "+"and quality is"+" "+quality,background=color,font=("Helvetica",10))
        my_label.grid(row=2,column=0,columnspan=2)
        root.configure(bg="green")
    except Exception as e:
        
       api = "error"
    
      
    
    


zip =Entry(root,width=15)
zip.grid(row=0,column=0)

b = Button(root,text="search",command=search)
b.grid(row=0,column=1)


root.mainloop()