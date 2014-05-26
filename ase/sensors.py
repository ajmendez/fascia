
import sys
import time
import string
try:
    import androidhelper as android
except:
    import android

def sensors(droid, delta):
    droid.startSensingTimed(1, 250)
    time.sleep(1)
    
    droid.vibrate()

    # droid.batteryStartMonitoring()
    # # print droid.readBatteryData() # None
    # # print droid.batteryGetTemperature() # None
    # print droid.batteryGetStatus() # 2
    # print droid.batteryGetPlugType() # 2
    # print droid.batteryGetLevel() # 42
    # print droid.batteryGetHealth() # 2
    # droid.batteryStopMonitoring()
    
    # print droid.readSensors().result
    # print droid.sensorsGetAccuracy().result
    # print droid.sensorsGetLight().result # None
    # print droid.sensorsReadAccelerometer().result
    # print droid.sensorsReadMagnetometer().result # None
    # print droid.sensorsReadOrientation().result
    
    try:
        while True:
            tmp = dict(droid.readSensors().result)
            msg = u'x:%(xforce)+5.2f, y:%(yforce)+5.2f, z:%(zforce)+5.2f' % tmp
            print msg
            time.sleep(delta)
    except KeyboardInterrupt as e:
        print 'Done'
    except Exception as e:
        print e
    droid.stopSensing()
    
if __name__ == '__main__':
    droid = android.Android()
    delta = float(sys.argv[1])
    sensors(droid, delta)