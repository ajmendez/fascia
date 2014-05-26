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


'''

#!/bin/sh
export PYTHONOPTIMIZE=2
export ANDROID_ROOT=/system
export ANDROID_CACHE=/cache
export ANDROID_DATA=/data
export ANDROID_ASSETS=/system/app
export ANDROID_PRIVATE=/data/data/com.hipipal.qpyplus/files
export ANDROID_STORAGE=/storage
export ANDROID_PROPERTY_WORKSPACE=8,65536

export ANDROID_PUBLIC=/storage/sdcard1/com.hipipal.qpyplus
export PYLOC=/data/data/com.hipipal.qpyplus/files
export SDLOC=/storage/sdcard1/com.hipipal.qpyplus/lib/python2.7/
export PATH=$PYLOC/bin:$PATH  
export PYTHONHOME=$PYLOC:$PYTHONHOME
export PYTHONPATH=$PYLOC/lib/python2.7/:$PYTHONPATH
export PYTHONPATH=$PYLOC/lib/python2.7/lib-dynload/:$PYTHONPATH
export PYTHONPATH=$PYLOC/lib/python2.7/site-package/:$PYTHONPATH
export PYTHONPATH=$SDLOC/site-packages/:$PYTHONPATH
export PYTHONSTARTUP=$SDLOC/site-packages/qpythoninit.py


export LD_LIBRARY_PATH=/data/data/com.hipipal.qpyplus/files/lib:/data/data/com.hipipal.qpyplus/files:/data/data/com.hipipal.qpyplus/lib
export TMPDIR=/storage/sdcard1/com.hipipal.qpyplus/cache



'''