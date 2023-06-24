from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

# command-line instructions
# Pip install geopy
# Pip install timezonefinder
# Pip install pytz
# Pip install requests
# Pip install pillow


root = Tk()
root.title("Weather App")
root.geometry("940x570+300+200")
root.configure(bg="#000c66")
root.resizable(False,False)

def getWeather():
    city=textfield.get()

    geolocator= Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f"Latitude: {round(location.latitude,4)} \u00b0N,  Longitude: {round(location.longitude,4)} \u00b0E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")  # Updated format string
    clock.config(text=current_time)

    ##weather
    api_key="Your_Api_Key"
    api="https://api.openweathermap.org/data/2.5/forecast?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&appid="+api_key
    json_data= requests.get(api).json()


    try:
        current_data = json_data['list']
        temp = current_data[0]['main']['temp']
        description = current_data[0]['weather'][0]['description']
        wind = current_data[0]['wind']['speed']
        humidity = current_data[0]['main']['humidity']
        pressure = current_data[0]['main']['pressure']
        sealevel=current_data[0]['main']['sea_level']
        grndlevel=current_data[0]['main']['grnd_level']
        temp_min=current_data[0]['main']['temp_min']
        temp_max=current_data[0]['main']['temp_max']



        t1.config(text=(temp,"\u00b0 C"))
        t2.config(text=(humidity, "%"))
        t3.config(text=(pressure, "hPa"))
        t4.config(text=(wind, "m/s"))
        t5.config(text=(description))
        t6.config(text=(temp_min,"\u00b0 C"))
        t7.config(text=(temp_max,"\u00b0 C"))
        t8.config(text=(sealevel,"m"))
        t9.config(text=(grndlevel,"m"))

        #first box
        firstdayimage = current_data[0]['weather'][0]['icon']
        photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
        firstimage.config(image=photo1)
        firstimage.image=photo1

        mintemp1 = json_data['list'][0]['main']['temp_min']
        maxtemp1 = json_data['list'][0]['main']['temp_max']
        day1temp.config(text=f"Temp:\nMin:{mintemp1}\n Max:{maxtemp1}")

        #second box
        seconddayimage = current_data[1]['weather'][0]['icon']
        img=(Image.open(f"icon/{seconddayimage}@2x.png"))
        resized_image= img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_image)
        secondimage.config(image=photo2)
        secondimage.image=photo2

        mintemp2 = json_data['list'][1]['main']['temp_min']
        maxtemp2 = json_data['list'][1]['main']['temp_max']
        day2temp.config(text=f"Temp:\nMin:{mintemp2}\n Max:{maxtemp2}")

        # #third box
        thirddayimage = current_data[2]['weather'][0]['icon']
        img = (Image.open(f"icon/{thirddayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo3 = ImageTk.PhotoImage(resized_image)
        thirdimage.config(image=photo3)
        thirdimage.image = photo3

        mintemp3 = json_data['list'][2]['main']['temp_min']
        maxtemp3 = json_data['list'][2]['main']['temp_max']
        day3temp.config(text=f"Temp:\nMin:{mintemp3}\n Max:{maxtemp3}")

        # #fourth box
        fourthdayimage = current_data[3]['weather'][0]['icon']
        img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo4 = ImageTk.PhotoImage(resized_image)
        fourthimage.config(image=photo4)
        fourthimage.image = photo4

        mintemp4 = json_data['list'][3]['main']['temp_min']
        maxtemp4 = json_data['list'][3]['main']['temp_max']
        day4temp.config(text=f"Temp:\nMin:{mintemp4}\n Max:{maxtemp4}")

        # #fifth box
        fifthdayimage = current_data[4]['weather'][0]['icon']
        img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo5 = ImageTk.PhotoImage(resized_image)
        fifthimage.config(image=photo5)
        fifthimage.image = photo5

        mintemp5 = json_data['list'][4]['main']['temp_min']
        maxtemp5 = json_data['list'][4]['main']['temp_max']
        day5temp.config(text=f"Temp:\nMin:{mintemp5}\n Max:{maxtemp5}")

        # #sixth box
        sixthdayimage = current_data[5]['weather'][0]['icon']
        img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo6 = ImageTk.PhotoImage(resized_image)
        sixthimage.config(image=photo6)
        sixthimage.image = photo6

        mintemp6 = json_data['list'][5]['main']['temp_min']
        maxtemp6 = json_data['list'][5]['main']['temp_max']
        day6temp.config(text=f"Temp:\nMin:{mintemp6}\n Max:{maxtemp6}")

        # #seventh box
        seventhdayimage = current_data[6]['weather'][0]['icon']
        img = (Image.open(f"icon/{seventhdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo7 = ImageTk.PhotoImage(resized_image)
        seventhimage.config(image=photo7)
        seventhimage.image = photo7

        mintemp7 = json_data['list'][6]['main']['temp_min']
        maxtemp7 = json_data['list'][6]['main']['temp_max']
        day7temp.config(text=f"Temp:\nMin:{mintemp7}\n Max:{maxtemp7}")

        #days
        first=datetime.now()
        day1.config(text=first.strftime("%A"))

        second=first+timedelta(days=1)
        day2.config(text=second.strftime("%A"))

        third=first+timedelta(days=2)
        day3.config(text=third.strftime("%A"))

        fourth=first+timedelta(days=3)
        day4.config(text=fourth.strftime("%A"))

        fifth=first+timedelta(days=4)
        day5.config(text=fifth.strftime("%A"))

        sixth=first+timedelta(days=5)
        day6.config(text=sixth.strftime("%A"))

        seventh=first+timedelta(days=6)
        day7.config(text=seventh.strftime("%A"))


    except KeyError:
        print("Error: Failed to retrieve current weather data from the API.")



##logoicon###########
image_icon=PhotoImage(file="Images/logo.png")
root.iconphoto(False,image_icon)
##logoicon###########


### Rectangle Image black background #############
original_image = Image.open("Images/Rounded Rectangle 1.png")
# Resize the image
resized_image = original_image.resize((310, 235), Image.LANCZOS)
# Convert the resized image to PhotoImage
rounded_box = ImageTk.PhotoImage(resized_image)
# Create the label and display the resized image
label = Label(root, image=rounded_box, bg="#000c66")
label.place(x=30, y=80)
### Rectangle Image black background #############


####label#####################
label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#01040B")
label1.place(x=80,y=110)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#01040B")
label2.place(x=80,y=130)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#01040B")
label3.place(x=80,y=150)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#01040B")
label4.place(x=80,y=170)

label5=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#01040B")
label5.place(x=80,y=190)

label6=Label(root,text="Min Temp",font=('Helvetica',11),fg="white",bg="#01040B")
label6.place(x=80,y=210)

label7=Label(root,text="Max Temp",font=('Helvetica',11),fg="white",bg="#01040B")
label7.place(x=80,y=230)

label8=Label(root,text="Sea Level",font=('Helvetica',11),fg="white",bg="#01040B")
label8.place(x=80,y=250)

label9=Label(root,text="Ground Level",font=('Helvetica',11),fg="white",bg="#01040B")
label9.place(x=80,y=270)
####label##################################


###thpwd######
t1=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t1.place(x=180,y=110)

t2=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t2.place(x=180,y=130)

t3=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t3.place(x=180,y=150)

t4=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t4.place(x=180,y=170)

t5=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t5.place(x=180,y=190)

t6=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t6.place(x=180,y=210)

t7=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t7.place(x=180,y=230)

t8=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t8.place(x=180,y=250)

t9=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t9.place(x=180,y=270)

#############searchbar##########
search_image = tk.PhotoImage(file="Images/Rounded Rectangle 3.png")
# Create the label and display the image
myimage = Label(image=search_image, bg="#000c66")
myimage.place(x=380, y=120)



textfield=tk.Entry(root,justify='center',width=15,font=('poppins',30,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=400,y=130)
textfield.focus()

weat_image=PhotoImage(file="Images/Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=400,y=130)

search_icon=PhotoImage(file="Images/Layer 6.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=755,y=125)
#############searchbar##########


#######Bottom Bcakground Frame##########
frame=Frame(root,width=940,height=180,bg="#212120")
frame.pack(side=BOTTOM)
#######Bottom Background Frame##########



####Bottom boxes######

firstbox=PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")


Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)

####Bottom boxes########################

#########clock (time to place) #############
clock=Label(root,font=("Helvetica",30,"bold"),fg="white",bg="#000c66")
clock.place(x=50,y=20)

#####timezone###
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#000c66")
timezone.place(x=700,y=20)

##longitutude and latitude#####
long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#000c66")
long_lat.place(x=650,y=60)



##########down boxes######
##first box###
firstFrame=Frame(root,width=230,height=132,bg="#282829")
firstFrame.place(x=35,y=415)

day1=Label(firstFrame,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage=Label(firstFrame,bg="#282829")
firstimage.place(x=1,y=15)

day1temp=Label(firstFrame,bg="#282829",fg="#57adff",font="arail 15 bold")
day1temp.place(x=100,y=50)

##second box###
secondFrame=Frame(root,width=70,height=115,bg="#282829")
secondFrame.place(x=305,y=425)

day2=Label(secondFrame,bg="#282829",fg="#fff")
day2.place(x=10,y=5)

secondimage=Label(secondFrame,bg="#282829")
secondimage.place(x=7,y=20)

day2temp=Label(secondFrame,bg="#282829",fg="#fff")
day2temp.place(x=5,y=70)

##third box###
thirdFrame=Frame(root,width=70,height=115,bg="#282829")
thirdFrame.place(x=405,y=425)

day3=Label(thirdFrame,bg="#282829",fg="#fff")
day3.place(x=10,y=5)

thirdimage=Label(thirdFrame,bg="#282829")
thirdimage.place(x=7,y=20)

day3temp=Label(thirdFrame,bg="#282829",fg="#fff")
day3temp.place(x=10,y=70)

##fourth box###
fourthFrame=Frame(root,width=70,height=115,bg="#282829")
fourthFrame.place(x=505,y=425)

day4=Label(fourthFrame,bg="#282829",fg="#fff")
day4.place(x=10,y=5)

fourthimage=Label(fourthFrame,bg="#282829")
fourthimage.place(x=7,y=20)

day4temp=Label(fourthFrame,bg="#282829",fg="#fff")
day4temp.place(x=10,y=70)

##fifth box###
fifthFrame=Frame(root,width=70,height=115,bg="#282829")
fifthFrame.place(x=605,y=425)

day5=Label(fifthFrame,bg="#282829",fg="#fff")
day5.place(x=10,y=5)

fifthimage=Label(fifthFrame,bg="#282829")
fifthimage.place(x=7,y=20)

day5temp=Label(fifthFrame,bg="#282829",fg="#fff")
day5temp.place(x=10,y=70)

##sixth box###
sixthFrame=Frame(root,width=70,height=115,bg="#282829")
sixthFrame.place(x=705,y=425)

day6=Label(sixthFrame,bg="#282829",fg="#fff")
day6.place(x=10,y=5)

sixthimage=Label(sixthFrame,bg="#282829")
sixthimage.place(x=7,y=20)

day6temp=Label(sixthFrame,bg="#282829",fg="#fff")
day6temp.place(x=10,y=70)

##seventh box###
seventhFrame=Frame(root,width=70,height=115,bg="#282829")
seventhFrame.place(x=805,y=425)

day7=Label(seventhFrame,bg="#282829",fg="#fff")
day7.place(x=10,y=5)

seventhimage=Label(seventhFrame,bg="#282829")
seventhimage.place(x=7,y=20)

day7temp=Label(seventhFrame,bg="#282829",fg="#fff")
day7temp.place(x=10,y=70)

##########down boxes######




root.mainloop()