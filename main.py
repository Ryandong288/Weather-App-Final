from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests
import os
import re

app = FastAPI()

#set up basic HTML template
templates = Jinja2Templates(directory="templates")

#set up static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

#API_KEY from weather app
API_KEY = "6285c8c26584f9a673fb5a498781ac1e"

#home page data for template
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#Inputing API into website
@app.get("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, location: str):
    if location == "NOAPI":
        return JSONResponse({"error": "API key not set"}, status_code=500)
    
    #Make sure API Key is set
    if not API_KEY:
        return JSONResponse({"error": "API key not set"}, status_code=500)

    #Check if input is a ZIP code or city name
    if re.match(r"^\d{5}(-d{4})?$", location):
        query_param = f"zip={location},us"
    else:
        query_param = f"q={location}"
    
    #Format the URL for API call and fetch response
    url = f"http://api.openweathermap.org/data/2.5/weather?{query_param}&appid={API_KEY}&units=imperial"
    response = requests.get(url)

    #Testing error codes for API 
    if response.status_code == 401:
        return JSONResponse({"error": "Unauthorized. Check your API key."}, status_code=401)
    elif response.status_code == 404:
        return JSONResponse({"error": "City not found"}, status_code=404)
    elif response.status_code != 200:
        return JSONResponse({"error": "Failed to fetch weather data"}, status_code=500)

    #Converts data from api call to store and convert to json
    weather_data = response.json()

    #Weather condition check
    weather_condition = weather_data["weather"][0]["main"].lower()
    weather_icons = {
        "rain": "rainy.png",
        "snow": "snowy.png",
        "thunderstorm": "stormy.png",
        "clear": "sunny.png",
        "clouds": "windy.png"
    }
    icon_path = f"/static/{weather_icons.get(weather_condition, 'sunny.png')}"
    
    #Final data to push to template
    print(weather_data)
    return templates.TemplateResponse(
        "weather.html",
        {
            "request": request, 
            "location": location, 
            "weather": weather_data,
            "icon_path": icon_path
        },
    )
