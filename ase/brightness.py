
import sys
try:
    import androidhelper as android
except:
    import android

def brightness(droid, value):
    print "Current Brightness: % 3d" % droid.getScreenBrightness().result
    print 'Set brightness: % 3d' % value
    droid.setScreenBrightness(value)

if __name__ == '__main__':
    droid = android.Android()
    value = int(sys.argv[1])
    brightness(droid, value)