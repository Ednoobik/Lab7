import requests


# 1
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Krasnodar&appid=1a8c0131701f1da33a933c92d7648b7b&units=metric&lang=ru")
data = response.json()

if response.status_code == 200:
    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    print(f"Погода в Краснодаре: {weather}, температура: {temp}°C, давление: {pressure} гПа, влажность: {humidity} %")
else:
   print(f"Ошибка: {data.get('message', 'Неизвестная ошибка')}")


# 2
response = requests.get('http://api.open-notify.org/iss-now.json')
people = requests.get('http://api.open-notify.org/astros.json')
data = response.json()
data_people = people.json()
if (response.status_code == 200) and (response.status_code == 200):
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    number = data_people['number']
    print('Текущее местоположение МКС:')
    print(f'Широта: {latitude}, Долгота: {longitude}')
    print(f'Положение на карте: https://www.google.com/maps/@{latitude},{longitude}')
    if number > 0:
        print(f'Количетсво людей в космосе: {number}')
        print('Их имена и звания:')
        for person in data_people['people']:
            name = person['name']
            craft = person['craft']
            print(f'{name}, {craft}')
else:
    print(f'Ошибка получения данных МКС: {response.status_code} {people.status_code}')


# 3
import tkinter as tk
import random
from PIL import Image, ImageTk
from io import BytesIO


categories = ["neko", "kitsune", "husbando", "waifu"]
chosen_category = random.choice(categories)
api_url = f"https://nekos.best/api/v2/{chosen_category}"
def generate_image():

    response = requests.get(api_url)
    data = response.json()
    image_url = data["results"][0]["url"]
    img_response = requests.get(image_url, timeout=10)
    pil_image = Image.open(BytesIO(img_response.content))
    pil_image.thumbnail((400, 400), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(pil_image)

    label.config(image=tk_image)
    label.image = tk_image

def cancel():
    window.destroy()


window = tk.Tk()
window.title('Your image')
window.geometry('500x500')


label = tk.Label(window)
label.pack(pady=10, expand=True)

generate_button = tk.Button(
    window,
    text="Сгенерировать!",
    command=generate_image,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10
)
generate_button.pack(pady=20)


window.mainloop()