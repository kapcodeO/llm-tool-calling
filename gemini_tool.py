from openai import OpenAI
from dotenv import load_dotenv 
import gradio as gr
import requests
import json
import os

load_dotenv(override=True)
client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai", api_key=os.environ["GEMINI_API_KEY"])

system_message = """
You are a helpful assistant which fetches the current temperature and the current date
of a location upon user request if it is not needed to elaborate then try your best to
keep your responses shorter upto 1 line only.
You call the tool get_weather_tool IF AND ONLY IF user has requested the temperature of a location.
You are made by Kapil Ojha. A 23 year old Btech Graduate who's an AI Enthusiast and is currently learning AI Engineering.
"""

class WeatherService:
    def __init__(self):
        self.geocode_city_url = "https://nominatim.openstreetmap.org/search"
        self.get_temperature_url = "https://api.open-meteo.com/v1/forecast"

    def geocode_city(self, location: str):
        params = {
            "q": location,
            "format": "json",
            "limit": 1
        }
        headers = {
            "User-Agent": "llm-tool-calling-project"
        }
        result = requests.get(self.geocode_city_url, params=params, headers=headers)
        data = result.json()
        try:
            return {
                "lat": data[0]["lat"], 
                "lon": data[0]["lon"]
                }
        except IndexError:
            return f"'{location}' is not a valid location, please enter a valid location."
        
    
    def get_temperature(self, coord):
        try:
            lat, lon = coord["lat"], coord["lon"]
            params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather" : True
            }
            result = requests.get(self.get_temperature_url, params=params)
            data = result.json()
            return data
        except TypeError:
            return coord
            
    
weather_service = WeatherService()

def get_weather_tool(location: str) -> str:
    coordinates = weather_service.geocode_city(location)
    data = weather_service.get_temperature(coordinates)
    try:
        current_temp = data["current_weather"]["temperature"]
        current_date = data["current_weather"]["time"].split("T")[0]
        return f"The current temperature of {location} as of {current_date} is {current_temp}°C"
    except TypeError:
        return data

function = {
    "name": "get_weather_tool",
    "description": "fetches the current temperature and date of city which user requested",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "the city which user has requested the temperature of"
            },
        },
        "required": ["location"],
        "additionalProperties": False
    }
}

tool = [{"type": "function", "function": function}]

def handle_tool_calls(assistant_message):
    result = []
    for tool_call in assistant_message.tool_calls:
        if tool_call.function.name == "get_weather_tool":
            arguments = json.loads(tool_call.function.arguments)
            location = arguments.get("location")
            response_content = get_weather_tool(location)
            response = {
                "role": "tool",
                "content": response_content,
                "tool_call_id": tool_call.id
            }
            result.append(response)
    return result

def chat(message, history):
    history = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    responses = client.chat.completions.create(model="gemini-2.5-flash-lite", messages=messages, tools=tool)

    assistant_message = responses.choices[0].message

    if assistant_message.tool_calls:
        messages.append(assistant_message.model_dump())
        tool_response = handle_tool_calls(assistant_message)
        messages.extend(tool_response)
        final_response = client.chat.completions.create(model="gemini-2.5-flash-lite", messages=messages)

        return final_response.choices[0].message.content
    return assistant_message.content

gr.ChatInterface(fn=chat, title="Chatbot").launch()
