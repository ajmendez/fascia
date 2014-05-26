import android

def basic():
    droid = android.Android()
    droid.webViewShow('http://google.com')

def force():
    droid = android.Android()
    droid.webViewShow('index.html')
    while True:
      result = droid.waitForEvent('say').result
      droid.ttsSpeak(result['data'])


if __name__ == '__main__':
    # basic()
    force()
