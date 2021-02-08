import requests

api_key = "Your API Key"
stadt = input("Gib deine Stadt ein: ") 

url = f"https://api.openweathermap.org/data/2.5/weather?q={stadt}&appid={api_key}&units=metric"

data = requests.get(url).json()

temperatur = data["main"]["temp"]
luftfeuchtigkeit = data["main"]["humidity"]



print("In", stadt, "beträgt die Temperatur derzeit:", temperatur,"°C und die Luftfeuchtigkeit",luftfeuchtigkeit,"%" )


input("Drücke Enter um die wetter App zu schließen.")
