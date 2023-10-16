import ttkbootstrap as ttk
import requests
from ttkbootstrap.constants import *
from PIL import Image,ImageTk
root = ttk.Window()
root.title("Weather Forecast")

def view():
    city = loc_entry.get()

    # Make an API request to OpenWeatherMap
    api_key = 'Use your api key'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        existing_items = display.get_children()
        if existing_items:
            display.delete(*existing_items)
        display.insert("", "end", values=[f"Weather in {city}"])
        display.insert("", "end", values=[f"Temperature: {temperature}°C"])
        display.insert("", "end", values=[f"Humidity: {humidity}%"])
        display.insert("", "end", values=[f"Description: {weather_description.capitalize()}"])
        display.insert("", "end", values=[f"Wind Speed: {wind_speed} m/s"])

        for item in display.get_children():
            display.item(item, tags=("lightblue",))

    else:
        existing_items = display.get_children()
        if existing_items:
            display.delete(*existing_items)
        display.insert("", "end", values=["Error: Unable to retrieve weather data"])


frame = ttk.Frame(root, style="Dark")
frame.pack(fill=ttk.BOTH, expand=True)

lb_frame = ttk.Labelframe(frame, text="Enter the location", style="info")
lb_frame.grid(row=0, column=0,padx=5, pady=5,sticky=ttk.W)

loc_entry = ttk.Entry(lb_frame, style="success",font=("Time in Roman",14))
loc_entry.grid(row=0, column=1, padx=10, pady=5)

view_bt = ttk.Button(frame, text="View", command=view, bootstyle="outline", style="success-outline")
view_bt.grid(row=1, column=0,columnspan=2, padx=10, pady=5)

display = ttk.Treeview(root, columns=("weather update",),show="headings", style="secondary")
display.heading("weather update", text="weather update")
display.pack(fill=ttk.BOTH, expand=True)
display.tag_configure("helvetica", font=("Helvetica", 14))

image = Image.open("C:/Users/Ali/PycharmProjects/pythonProject/weather-icon.jpg")
photo = ImageTk.PhotoImage(image)
root.iconphoto(False, photo)


for i in range(3):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(0, weight=1)
root.mainloop()
