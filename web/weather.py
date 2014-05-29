'''weather.py -- get the weather, icon and some related bits
May 2014: Mendez
'''

import pyowm
import dateutil.parser
from pymendez.auth import auth

KEY = auth('openweathermap', 'ident')
LOCATION = 'San Diego, CA'

ICONMAP = {
  '01d':'wi-day-sunny',
  '02d':'wi-day-cloudy',
  '03d':'wi-cloudy',
  '04d':'wi-rain',
  '09d':'wi-showers',
  '10d':'wi-rain',
  '11d':'wi-thunderstorm',
  '13d':'wi-snow',
  '50d':'wi-fog',
  '01n':'wi-night-clear',
  '02n':'wi-night-cloudy',
  '03n':'wi-night-cloudy',
  '04n':'wi-night-rain',
  '09n':'wi-night-showers',
  '10n':'wi-night-rain',
  '11n':'wi-night-thunderstorm',
  '13n':'wi-night-snow',
  '50n':'wi-fog',
}

class Weather(object):
  """The weather panel"""
  
  def __init__(self, minutes=30):
    ''' minutes is how often to update'''
    self.minutes = minutes 
    self.owm = pyowm.OWM(KEY)
  
  def update(self):
    '''Get the data from the server'''
    loc = self.owm.weather_at(LOCATION)
    current = loc.get_weather()
    fc = self.owm.daily_forecast(LOCATION, limit=5)
    forecast = fc.get_forecast().get_weathers()
    
    # parse the forecast
    self.data = self.parse(current)
    self.data['forecast'] = [self.parse(w) for w in forecast]
    
  def display(self):
    '''Ready the template for display'''
    return self.data
  
  def parse(self, w):
    '''parse the owm weather object'''
    temp = w.get_temperature('fahrenheit')
    if 'temp_min' in temp:
      temp = dict(day=temp['temp'],
                  min=temp['temp_min'],
                  max=temp['temp_max'])
    icon = w.get_weather_icon_name()
    
    data = dict(
      date        = dateutil.parser.parse(w.get_reference_time('iso')),
      temp        = temp.get('day', 0),
      min         = temp.get('min', 0),
      max         = temp.get('max', 0),
      status      = w.get_status(),
      description = w.get_detailed_status(),
      code        = w.get_weather_code(),
      icon        = ICONMAP.get(icon,icon),
      sunrise     = dateutil.parser.parse(w.get_sunrise_time('iso')),
      sunset      = dateutil.parser.parse(w.get_sunset_time('iso')),
    )
    return data
