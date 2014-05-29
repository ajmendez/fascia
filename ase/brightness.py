
import sys
try:
    import androidhelper as android
except:
    import android

def brightness(droid, value):
    droid.makeToast("Changing Brightness!") 
    # droid.wakeLockAcquireFull()
    # droid.notify('test','message')
    if not droid.checkScreenOn().result:
        print 'Turning on screen'
        print droid.wakeLockAcquireFull()
        # droid.wakeLockAcquireDim()
        # droid.setScreenState(1)
    else:
        print 'Screen On'
    # print 'Timeout: %s' % droid.getScreenTimeout().result
    
    print "Current Brightness: % 3d" % droid.getScreenBrightness().result
    print 'Set brightness: % 3d' % value
    droid.setScreenBrightness(value)

    print droid.wakeLockRelease()

if __name__ == '__main__':
    droid = android.Android()
    value = int(sys.argv[1])
    brightness(droid, value)