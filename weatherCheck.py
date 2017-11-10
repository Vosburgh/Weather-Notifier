import json
import requests
import TextMessage


class User(object):
    def __init__(self,name,phone,location):
        self.name = name
        self.phone = phone
        self.location = location

    def checkWeather(self):
        address = 'http://api.wunderground.com/api/[YOUR API KEY HERE]/forecast/q/[YOUR COUNTRY HERE]/[YOUR CITY HERE].json'
        response = requests.get(address)
        response.raise_for_status()
        weather = json.loads(response.text)

        pop = weather['forecast']['txt_forecast']['forecastday'][0]['pop']
        low = weather['forecast']['simpleforecast']['forecastday'][0]['low']['celsius']

        return [pop,low]


    def notifyUser(self):
        if self.checkWeather() != None:
            weather = self.checkWeather()
            TextMessage.SendText(TextMessage.createText(self.name,self.location,weather[0],weather[1]), self.phone)