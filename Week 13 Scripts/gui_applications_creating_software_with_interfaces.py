# Simple weather app using Tkinter
import tkinter as tk
from tkinter import ttk
import requests  # For API calls

def get_weather():
    city = city_entry.get()
    # In a real app, you would call a weather API here
    # This is simplified for the example
    weather_label.config(text=f"Getting weather for {city}...")
    
    # Update with "real" data
    temperature = "24°C"
    condition = "Partly Cloudy"
    weather_label.config(
        text=f"Weather in {city}:\n{temperature}\n{condition}")

# Create the main window
root = tk.Tk()
root.title("Simple Weather App")
root.geometry("300x200")

# Create input field and button
city_frame = ttk.Frame(root, padding="10")
city_frame.pack()

ttk.Label(city_frame, text="Enter city:").pack()
city_entry = ttk.Entry(city_frame, width=20)
city_entry.pack(pady=5)
city_entry.focus()

ttk.Button(city_frame, text="Get Weather", 
          command=get_weather).pack(pady=5)

# Display area for weather information
weather_label = ttk.Label(root, text="Enter a city to see the weather")
weather_label.pack(pady=20)

# Start the app
root.mainloop()
