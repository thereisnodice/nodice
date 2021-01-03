import requests
from .config import *
from aiocache import cached

@cached(ttl=60)
async def get_weather_short(city: str) -> str:
    weather_json=get_weather_json(city)
    weather=weather_json["result"]["weather"]
    temperature=weather_json["result"]['temperature_curr']
    return f'{city}当前天气{weather}，温度{temperature}'

@cached(ttl=60)
async def get_weather_desc(city: str) -> str:
  weather_json=get_weather_json(city)
  weather=weather_json["result"]["weather"]
  temperature=weather_json["result"]['temperature_curr']
  humidity=weather_json["result"]['humidity']
  wind=weather_json["result"]['wind']
  return f'{city}当前天气{weather}，温度{temperature}，空气湿度{humidity}，{wind}'

def get_weather_json(city: str):
  url = 'http://api.k780.com'
  params = {
  'app' : 'weather.today',
  'weaid' : city,
  'appkey' : WEATHER_KEY,
  'sign' : WEATHER_SIGN,
  'format' : 'json',
}
  json=requests.get(url,params).json()
  if json['success']=="1":
    return json