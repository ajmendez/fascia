from kivy.network.urlrequest import UrlRequest

def got_weather(req, results):
    for key, value in results['weather'][0].items():
        print(key, ': ', value)


if __name__ == '__main__':
  req = UrlRequest(
      'http://api.openweathermap.org/data/2.5/weather?q=San_Diego,CA',
      got_weather)
  req.wait()
  print 'Done'