from kivy.network.urlrequest import UrlRequest

def got_weather(req, results):
    for key, value in results['weather'][0].items():
        print(key, ': ', value)


if __name__ == '__main__':
  ID = 5391811
  URL = 'http://api.openweathermap.org/data/2.5/weather?q=San_Diego,CA&APPID='
  req = UrlRequest(URL, got_weather, debug=True)
  req.wait()
  print 'Done'